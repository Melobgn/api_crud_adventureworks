from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from config import settings
import logging

# Configuration du logger
logger = logging.getLogger("auth")

router = APIRouter()

# Gestion des mots de passe
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Simuler une "base de données" à partir des paramètres
fake_users_db = {
    settings.USER1_USERNAME: {
        "username": settings.USER1_USERNAME,
        "hashed_password": pwd_context.hash(settings.USER1_PASSWORD),
    }
}

# Générer un token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    logger.info("Token JWT créé avec succès.")
    return token

# Décoder un token JWT
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise JWTError
        logger.info("Token JWT décodé avec succès.")
        return username
    except JWTError:
        logger.warning("Échec du décodage du token JWT.")
        return None

# Vérification de l'utilisateur actuel
def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_access_token(token)
    if username is None:
        logger.warning("Utilisateur non authentifié.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return username

# Endpoint de connexion
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint pour authentifier un utilisateur et générer un token JWT.
    """
    user = fake_users_db.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user["hashed_password"]):
        logger.warning("Tentative de connexion échouée pour l'utilisateur : %s", form_data.username)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password"
        )
    access_token = create_access_token(data={"sub": user["username"]})
    logger.info("Connexion réussie pour l'utilisateur : %s", user["username"])
    return {"access_token": access_token, "token_type": "bearer"}

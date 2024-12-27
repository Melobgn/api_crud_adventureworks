from sqlmodel import SQLModel, create_engine, Session
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    USER1_USERNAME: str
    USER1_PASSWORD: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

# Création de l'engine pour se connecter à la base de données
engine = create_engine(
    settings.DATABASE_URL, 
    echo=True  # Active les logs SQL
)

# Fonction pour gérer les sessions
def get_session():
    """
    Gère les sessions de base de données pour les endpoints.
    """
    with Session(engine) as session:
        yield session



# # Requête SQL enveloppée dans text()
# query = text("""
# SELECT COLUMN_NAME, CHARACTER_MAXIMUM_LENGTH
# FROM INFORMATION_SCHEMA.COLUMNS
# WHERE TABLE_NAME = 'Product' AND COLUMN_NAME = 'Size' AND TABLE_SCHEMA = 'SalesLT';
# """)

# # Exécution de la requête
# with Session(engine) as session:
#     result = session.execute(query)
#     columns_info = result.fetchall()

# # Affichage des résultats
# for row in columns_info:
#     print(f"Column Name: {row.COLUMN_NAME}, Max Length: {row.CHARACTER_MAXIMUM_LENGTH}")


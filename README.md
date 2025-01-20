# AdventureWorks API

## Description

AdventureWorks API est une application RESTful développée avec **FastAPI** et **SQLModel** pour gérer les produits de la base de données AdventureWorks. L'API propose des fonctionnalités CRUD (Create, Read, Update, Delete) sécurisées avec un système d'authentification basé sur JWT.

---

## Fonctionnalités

- **CRUD Produits** :
  - Lister tous les produits.
  - Obtenir les détails d'un produit spécifique.
  - Créer un nouveau produit.
  - Mettre à jour un produit existant.
  - Supprimer un produit.

- **Authentification** :
  - Connexion sécurisée avec des tokens JWT.
  - Protection des endpoints avec des rôles (`is_admin`).

- **Documentation Swagger** :
  - Documentation interactive accessible à `http://127.0.0.1:8000/docs`.

---

## Prérequis

- **Python** : Version 3.9 ou supérieure.
- **Base de données SQL Server** : Base de données `AdventureWorks` hébergée sur Azure ou en local.
- **Outils supplémentaires** : 
  - `pip` pour gérer les dépendances.
  - `Postman` ou `cURL` pour tester les endpoints (facultatif).

---

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-repo/adventureworks-api.git
   cd adventureworks-api
   ```


2. Créez un environnement virtuel : 
    ``` python -m venv .venv
        source .venv/bin/activate # Sous Windows : .venv\Scripts\activate
    ```


3. Installez les dépendances :
    ``` pip install -r requirements.txt ```


4. Configurez le fichier .env : Créez un fichier .env à la racine du projet et ajoutez les informations suivantes :
    ``` USER1_USERNAME=user1
        USER1_PASSWORD=password123
        SECRET_KEY=your_super_secret_key
        ACCESS_TOKEN_EXPIRE_MINUTES=30
        ALGORITHM=HS256
        SERVER_NAME=your-sql-server.database.windows.net
        BDD_NAME=your-bdd-name
        USER=your-db-user
        MDP=your-db-password
    ```


## Utilisation

1. Lancer le serveur : Démarrez l'application avec Uvicorn : 
    ``̀  python3 -m uvicorn main:app --reload ```
    Le serveur sera accessible à http://127.0.0.1:8000.


2. Documentation Swagger : Rendez-vous sur l'interface Swagger pour explorer les endpoints et tester l'API :
    ``` http://127.0.0.1:8000/docs ```


3. Authentification : Pour accéder aux routes protégées, suivez ces étapes : 
    1. Obtenez un token JWT :
        - Endpoint : POST /auth/login
        - Body (x-www-form-urlencoded):
        ``` {
            "username": "user1",
            "password": "password123"
            }
        ```
        - Réponse :
        ```
        {
        "access_token": "your_jwt_token",
        "token_type": "bearer"
        }
        ```
    
    2. Utilisez le token : Ajoutez un header Authorization avec la valeur :
        ``` Bearer your_jwt_token ```


4. Endpoints Principaux


| Méthode | Endpoint                 | Description                                  | Authentification |
|---------|--------------------------|----------------------------------------------|------------------|
| `POST`  | `/auth/login`            | Authentifier un utilisateur                  | ❌               |
| `GET`   | `/products`              | Récupérer tous les produits                  | ✅               |
| `GET`   | `/products/{product_id}` | Récupérer un produit par ID                  | ✅               |
| `POST`  | `/products`              | Créer un nouveau produit (admin requis)      | ✅               |
| `PUT`   | `/products/{product_id}` | Mettre à jour un produit (admin requis)      | ✅               |
| `DELETE`| `/products/{product_id}` | Supprimer un produit (admin requis)          | ✅               |



## Structure du projet

- **auth/**
  - `__init__.py` : Centralisation des dépendances d'authentification
  - `dependencies.py` : Gestion de l'authentification JWT
- **routes/**
  - `products.py` : Endpoints CRUD pour les produits
- `models.py` : Définition des modèles SQLModel
- `config.py` : Configuration et variables d'environnement
- `main.py` : Point d'entrée principal de l'application
- `requirements.txt` : Liste des dépendances Python
- `.env` : Variables d'environnement (non inclus dans le repo)
- `README.md` : Documentation du projet


## Tests

Vérifiez manuellement les endpoints avec Swagger, Postman, ou cURL.



# TP - Flask, Docker et GitHub CI/CD

## Objectifs

1. Créer une API Flask simple
2. Écrire des tests unitaires avec pytest
3. Dockeriser l'application
4. Configurer une CI/CD avec GitHub Actions

## Étapes

### 1. Compléter l'application Flask (`app.py`)

- Route GET "/" qui retourne `{ "message": "Hello TP" }`
- Route GET "/health" qui retourne `{ "status": "ok" }`

### 2. Compléter les tests (`test_app.py`)

- Tester le status code 200 pour les deux routes
- Tester le contenu JSON retourné

### 3. Compléter le Dockerfile

- Utiliser l'image `python:3.10-slim`
- Installer les dépendances depuis `requirements.txt`
- Exposer le port 5000
- Lancer l'application avec `flask run`

### 4. Tester localement

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer les tests
pytest

# Construire l'image Docker
docker build -t tp-flask .

# Lancer le container
docker run -p 5000:5000 tp-flask
```

### 5. Vérifier la CI/CD

- Pousser le code sur GitHub
- La CI/CD devrait se déclencher automatiquement
- Vérifier que tous les tests passent


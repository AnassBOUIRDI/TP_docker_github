# Solution -   Flask, Docker et GitHub CI/CD

## Application Flask

L'application expose deux routes :
- `GET /` : Retourne `{ "message": "Hello TP" }`
- `GET /health` : Retourne `{ "status": "ok" }`

## Tests

Les tests vérifient :
- Le status code 200 pour chaque route
- Le contenu JSON retourné

## Docker

L'image Docker :
- Utilise `python:3.10-slim`
- Installe les dépendances depuis `requirements.txt`
- Expose le port 5000
- Lance l'application avec `flask run`

## CI/CD

Le workflow GitHub Actions :
- Se déclenche sur chaque push
- Installe Python 3.10
- Installe les dépendances
- Lance les tests avec pytest
- Construit l'image Docker
- Vérifie que le build réussit

## Commandes utiles

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer les tests
pytest

# Construire l'image Docker
docker build -t tp-flask .

# Lancer le container
docker run -p 5000:5000 tp-flask

# Tester l'API
curl http://localhost:5000/
curl http://localhost:5000/health
```


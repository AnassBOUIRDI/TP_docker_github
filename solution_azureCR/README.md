# Solution Azure Container Registry

## Application Flask

- Route `GET /` : Retourne `{ "message": "Hello CI" }`
- Route `GET /health` : Retourne `{ "status": "ok" }`

## Tests

Les tests unitaires sont situés dans `tests/unit/test_app.py` et vérifient :
- Le status code 200 pour chaque route
- Le contenu JSON retourné
- L'endpoint health

## Docker

```bash
docker build -t tp-flask-azure .
docker run -p 5000:5000 tp-flask-azure
```

## CI/CD avec Azure Container Registry

- **Pull Request** : Exécute uniquement les tests
- **Push sur main** : Tests + Build + Push vers Azure Container Registry


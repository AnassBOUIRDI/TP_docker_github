import pytest
from app import app

@pytest.fixture
def client():
    # TODO: Créer un client de test Flask
    pass

# TODO: Tester la route "/"
def test_hello_route(client):
    # TODO: Faire une requête GET vers "/"
    # TODO: Vérifier le status code 200
    # TODO: Vérifier que le JSON retourné contient { "message": "Hello TP" }
    pass

# TODO: Tester la route "/health"
def test_health_route(client):
    # TODO: Faire une requête GET vers "/health"
    # TODO: Vérifier le status code 200
    # TODO: Vérifier que le JSON retourné contient { "status": "ok" }
    pass


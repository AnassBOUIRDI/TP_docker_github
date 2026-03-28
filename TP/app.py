from flask import Flask, jsonify

# TODO: Créer l'instance Flask
app = Flask(__name__)

# TODO: Créer la route GET "/" qui retourne { "message": "Hello TP" }
@app.route("/")
def hello():
    pass

# TODO: Créer la route GET "/health" qui retourne { "status": "ok" }
@app.route("/health")
def health():
    pass

# TODO: Ajouter le point d'entrée pour lancer l'application
if __name__ == "__main__":
    pass


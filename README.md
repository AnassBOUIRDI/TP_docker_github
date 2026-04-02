#  TP Flask, Docker et GitHub CI/CD

Ce projet contient un TP complet pour apprendre à :
- Créer une API Flask simple
- Écrire des tests unitaires avec pytest
- Dockeriser une application
- Configurer une CI/CD avec GitHub Actions
- Pousser automatiquement des images Docker vers Azure Container Registry

## Structure du projet

```
TP_flask_docker_github/
├── TP/                  # Version incomplète à compléter
├── SOLUTION/             # Solution complète
├── SOLUTION2/            # Solution avancée
├── solution_azureCR/     # Solution avec Azure Container Registry
└── .github/              # Configuration GitHub Actions
```

## Instructions

1. Travailler dans le dossier `TP/`
2. Compléter les fichiers marqués avec `TODO`
3. Consulter `SOLUTION/` pour vérifier vos réponses

## Configuration Azure Container Registry pour CI/CD

Pour activer le push automatique vers Azure Container Registry, configurez les secrets GitHub :

### 1. Créer un Azure Container Registry

1. Connectez-vous au [Portail Azure](https://portal.azure.com/)
2. Créez une nouvelle ressource **Container Registry**
3. Notez le nom du registre (ex: `myregistry.azurecr.io`)

### 2. Créer un Service Principal

1. Installez Azure CLI ou utilisez Azure Cloud Shell
2. Exécutez la commande suivante (remplacez les valeurs) :

```bash
az ad sp create-for-rbac --name "github-actions-sp" \
  --role contributor \
  --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group} \
  --sdk-auth
```

3. Copiez la sortie JSON complète

### 3. Ajouter les secrets dans GitHub

1. Allez dans votre repository GitHub
2. **Settings** → **Secrets and variables** → **Actions**
3. Cliquez sur **New repository secret**
4. Ajoutez deux secrets :
   - `AZURE_CREDENTIALS` : le JSON complet du Service Principal (étape 2)
   - `ACR_LOGIN_SERVER` : l'URL de votre ACR (ex: `myregistry.azurecr.io`)

### 4. Résultat

Lors d'un push sur `main`, le workflow :
- Exécute les tests pytest sur `solution_azureCR/tests/unit`
- Build l'image Docker depuis `solution_azureCR`
- Push l'image vers Azure Container Registry avec les tags :
  - `myregistry.azurecr.io/tp-flask-docker:latest`
  - `myregistry.azurecr.io/tp-flask-docker:<commit-sha>`

Lors d'une Pull Request, seul les tests sont exécutés (pas de build Docker).


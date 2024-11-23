# Monorepo Project

Ce monorepo contient un backend Django et un frontend Vue.js. Voici une explication de la structure du projet et des scripts utilisés.

## Prérequis
Pour travailler sur ce projet, vous devez avoir les outils suivants installés sur votre machine :

- **pnpm** : Gestionnaire de paquets pour Node.js.
- https://nodejs.org/en
  - **Installation** :
    ```bash
    npm install -g pnpm
    ```

- **pipenv** : Gestionnaire de paquets et d'environnements virtuels pour Python.
- https://www.python.org/
  - **Installation** :
    ```bash
    pip install pipenv
    ```

# Structure du Projet

## Backend

#### `./backend/secrets`
- **Description** : Contient les fichiers de configuration sensibles et secrets.
- **Sous-dossiers** :
  - `./backend/secrets/certs` : Certificats.
  - `./backend/secrets/keys` : Clés de chiffrement et autres clés sensibles.

#### `./backend/src`
- **Description** : Contient le code source de l'application backend.
- **Sous-dossiers** :
  - `./backend/src/apps` : Applications Django.
    - `./backend/src/apps/application` : Première application Django.
    - `./backend/src/apps/application2` : Deuxième application Django.
  - `./backend/src/plugins` : Plugins et extensions personnalisés.
  - `./backend/src/exceptions` : Exceptions personnalisées.
  - `./backend/src/utils` : Fonctions et classes utilitaires.

#### `./backend/tests`
- **Description** : Contient les tests pour le backend.

#### `./backend/scripts`
- **Description** : Contient les scripts utilitaires pour diverses tâches.

#### `./backend/fixtures`
- **Description** : Contient les fixtures de données pour les tests et le développement.

#### `./backend/docs`
- **Description** : Contient la documentation générée par Sphinx.
- **Sous-dossiers** :
  - `./backend/docs/source` : Fichiers source de la documentation.
  - `./backend/docs/build` : Documentation générée.
    - `./backend/docs/build/html` : Documentation HTML générée.
      - `./backend/docs/build/html/_sources` : Sources des fichiers HTML.
      - `./backend/docs/build/html/_static` : Fichiers statiques utilisés par la documentation.
      - `./backend/docs/build/html/.doctrees` : Arborescence des documents.
  - `./backend/docs/source/_templates` : Modèles de la documentation.
  - `./backend/docs/source/_static` : Fichiers statiques pour la documentation.

#### `./backend/specs`
- **Description** : Contient les spécifications et les documents de conception et les tests de validation.

#### `./backend/config`
- **Description** : Contient les fichiers de configuration pour divers outils et bibliothèques.

#### `./backend/logs`
- **Description** : Contient les fichiers de logs générés par l'application.

#### `./backend/main`
- **Description** : Contient les fichiers de configuration principaux de Django.

## Frontend

#### `./frontend/src`
- **Description** : Contient le code source de l'application frontend.
- **Sous-dossiers** :
  - `./frontend/src/views` : Composants de vue.
  - `./frontend/src/components` : Composants réutilisables.
    - `./frontend/src/components/__tests__` : Tests pour les composants.
    - `./frontend/src/components/icons` : Composants d'icônes.
  - `./frontend/src/stores` : Gestion de l'état avec Vuex.
  - `./frontend/src/assets` : Fichiers d'actifs statiques.
  - `./frontend/src/router` : Configuration du routeur Vue.

#### `./frontend/cypress`
- **Description** : Contient les tests end-to-end avec Cypress.
- **Sous-dossiers** :
  - `./frontend/cypress/fixtures` : Fixtures pour les tests.
  - `./frontend/cypress/e2e` : Tests end-to-end.
  - `./frontend/cypress/support` : Fichiers de support pour les tests.

#### `./frontend/public`
- **Description** : Contient les fichiers publics accessibles directement par le navigateur.

## Scripts

### Frontend (Vue.js avec pnpm)

Les scripts pour le frontend se trouvent dans le fichier `package.json` :


    - pnpm run dev : Lance un serveur de développement Vite sur le port 5173.
    - pnpm run build : Construit l'application pour la production.
    - pnpm run preview : Prévisualise la version construite de l'application.
    - pnpm run test:unit : Exécute les tests unitaires avec Vitest.
    - pnpm run test:e2e : Exécute les tests end-to-end avec Cypress.
    - pnpm run test:e2e:dev : Exécute les tests end-to-end avec Cypress en mode développement.
    - pnpm run build-only : Construit l'application sans démarrer le serveur de prévisualisation.
    - pnpm run type-check : Vérifie les types avec Vue TSC.
    - pnpm run lint : Vérifie et corrige les erreurs de style avec ESLint.
    - pnpm run format : Formate le code avec Prettier.
    - pnpm run storybook : Démarrer Storybook pour le développement de composants.
    - pnpm run build-storybook : Construit Storybook pour la production.

### Backend (Python)

Les scripts pour le backend se trouvent dans le dossier scripts et sont disponibles en versions .sh et .bat.
```./scripts/document.{sh/bat}``` : Génère la documentation Sphinx.

```./scripts/format.{sh/bat}``` : Formate le code avec Black.

```./scripts/lint.{sh/bat}``` : Vérifie le style du code avec Flake8.

```./scripts/run.{sh/bat}``` : Démarre le serveur de développement Django..

```./scripts/test.{sh/bat}``` : Exécute les tests Django.
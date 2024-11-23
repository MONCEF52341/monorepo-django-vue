@echo off
REM Ce script exécute les commandes Flake8 en utilisant pipenv

REM Activer l'environnement virtuel pipenv
call pipenv shell

REM Démarrer le serveur de développement Django
python manage.py runserver

REM Désactiver l'environnement virtuel pipenv
call pipenv shell

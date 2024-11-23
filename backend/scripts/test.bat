@echo off
REM Ce script exécute les commandes Flake8 en utilisant pipenv

REM Activer l'environnement virtuel pipenv
call pipenv shell

REM Exécuter les tests Django
python manage.py test src/apps tests/ specs/

REM Désactiver l'environnement virtuel pipenv
call pipenv shell

@echo off
REM Ce script exécute les commandes Flake8 en utilisant pipenv

REM Activer l'environnement virtuel pipenv
call pipenv shell

REM Exécuter Flake8 pour vérifier le style du code
flake8 --config=config/.flake8 .

REM Désactiver l'environnement virtuel pipenv
call pipenv shell

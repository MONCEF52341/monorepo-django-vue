

@echo off
REM Ce script construit la documentation Sphinx en utilisant pipenv

REM Activer l'environnement virtuel pipenv
call pipenv shell

REM Formater le code avec black
pipenv run black .

REM Désactiver l'environnement virtuel pipenv
call pipenv shell

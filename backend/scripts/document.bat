@echo off
REM Ce script construit la documentation Sphinx en utilisant pipenv

REM Activer l'environnement virtuel pipenv
call pipenv shell

REM Construire la documentation Sphinx
sphinx-build -b html docs/source docs/build/html

REM Désactiver l'environnement virtuel pipenv
call pipenv shell

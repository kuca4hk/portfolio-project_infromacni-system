# Registry-office

Informační systém pro školu, tenhle projekt je postaven na pythnu-3.10 django-rest-frameworku a postgresql databázi. Projekt měl řešit reporty pro Ministerstvo školství, správu uživatelů a  slovního hodnocení.


## Před spuštením

Před spuštěním aplikace je potřeba mít nainstalovaný DOCKER, conda(venv) a python 3.10

## Python
Projekt běží na pythonu 3.10

## Instalace requirements
pro instalaci requirements použijte následující příkaz:
```
pip install -r requirements.txt
```
## ENV
Pro správné fungování aplikace je potřeba mít nastavené proměnné, které najdete v souboru .env-sample, vytvořtes si nový soubour s názvem .env
## Docker
Pro to aby vám aplikace fungovala musíte nejdřiv z buildit docker image. To uděláte pomocí následujícího příkazu:
```
docker-compose build
```
Následně
```
docker-compose up
```
Pro spuštění jenom Databáse
```
docker-compose up db
```
Pro spuštění jenom Backendu
```
docker-compose up web
```
Pro smazaní vaší loaklní databáze
```
docker-compose down -v
```
## Migrace
Pro migrace DB použijte následující příkaz
```
python manage.py migrate
```
## Spuštění aplikace
Pro spuštění aplikace použijte následující příkaz
```
python manage.py runserver
```

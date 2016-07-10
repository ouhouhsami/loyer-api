# LoyerAPI

API over the confusing https://www.data.gouv.fr/fr/datasets/resultats-nationaux-des-observatoires-locaux-des-loyers/

To build the API, the CSV file has been refactored (see migrations directory)

## Install


```
git clone this repo
cd loyerapi
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
go to http://127.0.0.1:8000/
browse the API
```

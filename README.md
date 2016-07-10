# LoyerAPI

API over the confusing https://www.data.gouv.fr/fr/datasets/resultats-nationaux-des-observatoires-locaux-des-loyers/

To build the API, the CSV file has been refactored (see loyerapi/loyers/migrations directory)

## Install


```
git clone https://github.com/ouhouhsami/loyer-api
cd loyer-api/loyerapi
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then go to http://127.0.0.1:8000/ and browse the API.

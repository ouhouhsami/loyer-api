# loyer-api

API over the confusing https://www.data.gouv.fr/fr/datasets/resultats-nationaux-des-observatoires-locaux-des-loyers/

To build the API, the CSV file has been refactored (see loyerapi/loyers/migrations directory)


## Install

On linux, run the following command

```
$ git clone https://github.com/ouhouhsami/loyer-api
$ cd loyer-api
$ docker-compose up
```

Due to sync issues between containers, you may also need to migrate and create a superuser. See start_web.sh for more information.


If you want to recover data, fill the db with the appropriate dump

```
$ eval "$(docker-machine env loyer-api)"
$ docker-compose run db /srv/data/backup/restore_db.sh
```

## Help on docker

Create a docker machine

```
$ docker-machine create --driver virtualbox --virtualbox-memory 8096 loyer-api
```

List all docker machines

```
$ docker-machine ls
```

Stop a docker machine

```
$ docker-machine stop loyer-api
```

Start a docker machine

```
$ docker-machine start loyer-api
```
Set env variable the right way

```
$ eval "$(docker-machine env loyer-api)"
```

To get the VM IP address

```
$ docker-machine ip loyer-api
```

docker-compose

```
$ docker-compose build loyer-api
$ docker-compose build --no-cache loyer-api
$ docker-compose run loyer-api command
$ docker-compose up loyer-api
$ docker-compose stop
```


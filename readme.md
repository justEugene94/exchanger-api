# Installation

* #### Clone Project

```
cd /home/projects
sudo mkdir exchange_office
sudo chown {{YOUR_USER}}:{{YOUR_USER}} exchange_office

git clone git@github.com:justEugene94/exchanger-api.git
```

* #### Add `init.sql` file

```bash
cd docker/mysql/docker-entrypoint-initdb.d
cp init.sql.example init.sql
```

* #### Build Docker

```bash
sudo service nginx stop
sudo service mysql stop

docker-compose up --build
```

* #### Migrations, seeds and static for Django
Enter in python container:
```bash
docker-compose exec python bash
```

Migrations:
```bash
python3 manage.py migrate
```

Seeds:
```bash
python3 manage.py loaddata currencies commerce_value
python3 manage.py coefficient_seed --number=20
python3 manage.py purchase_seed --customers=10 --purchases=15
```

Functional tests:
```bash
xvfb-run python functional_tests.py
```

Static:
```bash
python3 manage.py collectstatic
```
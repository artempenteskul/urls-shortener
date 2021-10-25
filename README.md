## Urls-Shortener project

### Project running

1) download Docker on your PC
2) download or clone the repository from https://github.com/tommyfromche/urls-shortener
3) create .env files (.env.dev, .env.dev.db .env.prod, .env.prod.db)
   1) .env.dev should contains:
      1) DEBUG, SECRET_KEY, DJANGO_ALLOWED_HOSTS
      2) SQL_ENGINE, SQL_DATABASE, SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT, DATABASE
   2) .env.dev.db should contains:
      1) POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
   3) .env.prod should contains:
      1) DEBUG, SECRET_KEY, DJANGO_ALLOWED_HOSTS
      2) SQL_ENGINE, SQL_DATABASE, SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_PORT, DATABASE
   4) .env.prod.db should contains:
      1) POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
4) to run the service in the development mode:
   1) docker-compose up -d
   2) docker exec -it <container_id> python manage.py createsuperuser (user creation)
   3) docker-compose down (shut down the service)
5) to run the service in the production mode:
   1) docker-compose -f docker-compose.prod.yml up -d
   2) docker exec -it <container_id> python manage.py createsuperuser
   3) docker-compose -f docker-compose.prod.yml down (shut down the service)
6) to run the tests in both modes:
    1) docker exec -it <container_id> pytest
 
 ### Project scaling

In order to scale the project we can use more caching on the
website. We could use Django Cache framework (such as database 
caching). Also it will be great to serve all static content, 
which our website contains. Last but not least, we can configure 
throttling on our website, which protects us from ddos attacks.
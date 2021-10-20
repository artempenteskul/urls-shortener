## Urls-Shortener project

### Project running

1) download Docker on your PC
2) create .env files if needed (.env.dev, .env.prod, .env.prod.db)
3) to run the service in the development mode:
   1) docker-compose up -d
   2) docker exec -it <container_id> python manage.py createsuperuser (user creation)
   3) docker-compose down (shut down the service)
4) to run the service in the production mode:
   1) docker-compose -f docker-compose.prod.yml up -d
   2) docker exec -it <container_id> python manage.py collectstatic (serving static files)
   3) docker exec -it <container_id> python manage.py createsuperuser
   4) docker-compose -f docker-compose.prod.yml down (shut down the service)
5) to run the tests in both modes:
    1) docker exec -it <container_id> pytest
 
 ### Project scaling

In order to scale the project we can use more caching on the
website. We could use Django Cache framework (such as database 
caching). Also it will be great to serve all static content, 
which our website contains. Last but not least, we can configure 
throttling on our website, which protects us from ddos attacks.
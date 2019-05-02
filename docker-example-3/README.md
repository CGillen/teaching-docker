# Networks and Ports, Communicating with Docker

1. Examine `app/main.py` and `docker-compose.yml`. Try to understand how they are expecting the containers to communicate with each other
1. Run `docker-compose up` and see what happens. `Ctrl+C` when done to quit the running contianer  
  - Did the containers communicate?
  - How did this happen?
3. By default, docker-compose creates a network for all your services to talk to each other on. Find it in `docker network ls`
1. How would we do this without compose?  
  a. `docker network create my-net`  
  b. `docker (create|run) --network my-net --volume /path/to/docker-example-3/db-init:/docker-entrypoint-initdb.d --name db-service -d -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=my_data -e MYSQL_USER=user -e MYSQL_PASSWORD=password mariadb:5.5` Start after create if you didn't run it  
  c. `docker build -f ./Dockerfile -t network-example .`  
  d. `docker (create|run) --network my-net --volume /path/to/docker-example-3/app:/app network-example` Start after create if you didn't run it  
1. If you have a mysql client installed on the host, you can connect to the container database: `mysql my_data -h localhost -P 3306 -u user --password=password`  
  a. This is because of the `ports` definition in `docker-compose.yml`  
  b. To do this with just docker you can use the `--publish` option: `docker (create|run) --publish 3306:3306 --volume /path/to/docker-example-3/db-init:/docker-entrypoint-initdb.d --name db-service -d -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=my_data -e MYSQL_USER=user -e MYSQL_PASSWORD=password mariadb:5.5`

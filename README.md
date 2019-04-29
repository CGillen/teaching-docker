1. Let's start by pulling an image: `docker pull python:3.5.7`  
  a. `docker images`
  - What did we accomplish?
  - What's in an image?
2. Let's start a container: `docker run -it python:3.5.7 /bin/bash`  
  a. And take a look around  
  b. `python --version`  
  c. `pip list`  
  d. `pip install numpy`  
  e. `pip list`  
  f. Stop the container and compare `exit`  
  g. `python --version`  
  h. `pip list`  
1. Look at all running containers `docker ps`
1. But where's ours? Here's all containers that exist right now: `docker ps -a`
1. Exited? Let's start it again `docker start -ai <CONTAINER ID>`
 - Why didn't we need to specify `python:3.5.7` again?
 - Why didn't we need to specify `/bin/bash` again?

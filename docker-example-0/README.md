1. Look at Dockerfile and let's build that image: `docker build -f .\Dockerfile -t docker-example .`
1. Spin up a container based on our image `docker run --rm docker-example`
  - Why weren't we given a prompt?
  - How did it know what to run?
  - Is this what we want? How could this go wrong?
3. Make a change to app/main.py and run the container again
  - What happened?
  - Why?
4. Let's mount a volume
1. Share your drive if on windows
1. `docker run --rm -v '/path/to/docker-example-0/app:/app'`
  - How is this helpful?
  - Does this affect reproducibility? How?

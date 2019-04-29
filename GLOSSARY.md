# Image
Stateless and unchanging, an Image is the file system and configuration, comprised of many layers bundled together.

# Layer
An vaguely atomic change to the underlying filesystem of a base-image. Represented by a line in a Dockerfile.

# Dockerfile
A strict definition of changes to make to a base-image to create a new Image. Traditionally simply named `Dockerfile`

# Container
An instance of an Image. If an Image is an application installed on your computer, a container is running that application. You can have multiple "Notepads" running (container), doing different things, manipulating difference files, but they all run from one set of files (image).

# Volume
A shared file or folder between the host and container

# Host
The computer, OS, and environment running Docker. Typically your own computer.

# Network
A link between containers, initiated over "typical" network conectivity. Similar to connecting two machines together via RJ45 (ethernet) jack.

# Repository
A set of Images. Docker provides a local Repository to store all your pulled Images.

# Registry
A hosted service containing multiple Repositories. Docker Hub is the default, public Registry. By registering with Docker Hub you can register, build, and maintain your own repository on the Docker Hub registry.

# Compose File
A strict definition of multiple containers, volumes, networks, etc. Traditionally named `docker-compose.yml`

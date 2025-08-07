# Pi clusters
#### Written By Ben Peterson
This guide will go over a brief summary of what docker actually is, as well as how to use and install docker. 



## What is Docker?

Picture this: you want to install a program that let's you interface with the newest LLM's out there, but you dont want to go through all the pain of installing dependencies, installing packages, etc., and just want something that you can easily spin up and spin down. That's exactly what docker does! It allows you to run those applications in a portable manner, allowing you to run it on a variety of systems, and start the application up and shut it down super easily. In addition, docker isolates itself from the rest of your system, so, for example if your LLM interface requires a different version of C than your system has installed, it won't impart the version of C that is installed on your system! Pretty neat right?

## How does Docker work?

Docker has 3 main components, that being the DockerFile, the Docker Image, and the Docker Container. 

In short, the DockerFile is like the blueprints used to build the Docker Image, the Docker Image is like the template used to actually run the Docker Container, and the Docker Container is the thing that is actually running your application. So the steps are DockerFile->Docker Image-> Docker Container. 

When you first want to run a docker container, first you have to pull the already pre-made docker image.
So, for example, if you want to pull the image for ubuntu, the command that you would use would be **`sudo docker pull ubuntu:latest`**

Once you have it pulled, you can run the container by using the command **`sudo docker run -it ubuntu:latest:`**

To find out more about docker, use the `man` command. 

## How to install Docker?
Installation of docker varies per system, but on Raspberry PI OS (64 bit), the Debian installation instructions are followed.

Link To instructions: https://docs.docker.com/engine/install/debian/


1. Set up the Docker apt repository 
```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
```


2. Install the Docker packages

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
3. Verify by running `hello-world`
```bash
sudo docker run hello-world
```

## What can I do with Docker?
Here are a list of fun projects that you can do with Docker:
- Interface with AI models by using the `openwebui` container
- Install a mini HPC cluster that has databases, SLURM, and more! https://github.com/ubccr/hpc-toolset-tutorial/tree/master
- Run a database that connects with and application.
- Run a Raspberry PI cluster within Docker.

This list only scratches the surface of what you can do with Docker. If you have used an application (such as Discord, Firefox, etc.), odds are that a docker container exists for it!



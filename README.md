# How to use this project
This project is used for image recognigicion, the core functionality can be used in 2 differen ways.

1. With a HTTP API
2. With a standalone gui application

The API can be executed locally on linux or mac with the included `Makefile` on windows you will have to write the commands from the `Makefile` manually.

You can also use the `Dockerfile` to set up the API in an isolated environment.

## The local solution

### Requirements

A mongo db uri set up as an environment variable on the host machine eg.

```
export CDIO_MONGO_PASS='mongodb://localhost:27017'
```

Python and pip (version 3) 

### Setup

Go to the project folder and run

```
make init
```

which will install the required libraries used by the application

### Run the api locally

In the project folder run

```
make serve
```

### Run the gui application locally

```
make run
```

## The Docker solution

The easiest way to set up the api is to deploy it with docker.

### Requirements

A docker network with the name proxy

```
sudo docker network create proxy
```

A mongo db docker container with the name mongo and this uri

```
export CDIO_MONGO_PASS='mongodb://mongo:27017'
```

docker is also a requirement


### Build the docker image from source

in the project folder you can run

```
make build
```

which will use the `Dockerfile` in the root directory to build the image with all the required requirements.

or in the root directory with:

```
docker build -t cdio .
```

_It is also possible to get the official dockerimage from the groups online repository on dockerhub with the following command:_

```
sudo docker pull martinmaartensson/cdio
```

### Run with docker

If you made your own docker image with the name `cdio` then you can start it like this

```
sudo docker run --env CDIO_MONGO_PASS='mongodb://mongo:27017' --rm -dit --name cdio --network proxy cdio
```

You can also run a docker container with the official docker image and the official database.

```
sudo docker run --env CDIO_MONGO_PASS='mongodb://aladin:Cdio4Grp21!@mama.sh:27123' --rm -dit --name cdio --network proxy martinmaartensson/cdio
```

If you want to be able to access the API through your hostmachines ip address then you need to forward the port 80 from the docker container by adding this line to the command:

```
-p 8080:80
```



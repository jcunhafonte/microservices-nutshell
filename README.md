# MICROSERVICES-NUTSHELL

## Overview
This project aims to showcase how two different services can communicate between each other over GRPC.

- Insights service which is exposed over a REST API.
- Channels service which is exposed over a REST API.
- Authentication service which is exposed over a REST API.
- Permissions service which is exposed over gRPC.
- Kong API Gateway which communicates with Insights and Channels, validating the Authentication header over Authentication service.

![Architecture Diagram](/architecture.png "Architecture Diagram")

## Requirements
* [Docker](https://docs.docker.com/get-docker)
* [Docker Compose](https://docs.docker.com/compose/install/https://docs.localstack.cloud/get-started/#docker-compose)

## Installing
```sh
$ make install 
```

## Running
After completing the [installing](#installing) step, you're ready to start the project!

```sh
$ make start
```

## Scripts
```sh
$ make help
```

| Commands          | Description                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| help              | Available commands                                                     |
| protos-generate   | Generate protos                                                        |
| docker-build      | Docker build in detached mode                                          |
| docker-delete     | Docker delete images, volumes and its dependencies                     |
| docker-prune      | Docker image prune                                                     |
| docker-up         | Docker compose up                                                      |
| docker-down       | Docker compose down                                                    |
| start             | Start application                                                      |
| stop              | Stop application                                                       |
| install           | Install application                                                    |
| uninstall         | Uninstall application and its dependencies (images, volumes, networks) |
| recreate          | Recreate application                                                   |

## Uninstalling
```sh
$ sh make uninstall 
```

## Recreate
```sh
$ sh make recreate 
```

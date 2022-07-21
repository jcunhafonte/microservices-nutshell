.PHONY: help protos-create docker-build docker-delete docker-prune docker-up docker-down start stop install uninstall recreate

help: ## Available commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/:.*##\s*/##/g' | awk -F'##' '{ printf "%-14s %s\n", $$1, $$2 }'

protos-create: ## Create protos
	python3 -m grpc_tools.protoc -I ./protos --python_out=. --grpc_python_out=. ./protos/permission.proto

docker-build: ## Docker build in detached mode
	@docker compose up --build -d

docker-delete: ## Docker delete images, volumes and its dependencies
	@docker compose down --rmi all --volumes

docker-prune: ## Docker image prune
	@docker image prune --force

docker-up: ## Docker compose up
	@docker compose up

docker-down: ## Docker compose down
	@docker compose down

start: docker-up ## Start application

stop: docker-down ## Stop application

install: docker-build ## Install application

uninstall: docker-delete docker-prune ## Uninstall application and its dependencies (images, volumes, networks)

recreate: uninstall install ## Recreate application

migrations-run: ## Run migrations generating table and inserting data
	@docker exec -it permissions-database psql -h 0.0.0.0 -p 5433 -U permission-user -d permission -a -f init.sql
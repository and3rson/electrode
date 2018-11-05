#ECS_URL = 193635214029.dkr.ecr.eu-central-1.amazonaws.com/dunai

dev: | build
	docker-compose -f docker-compose.yml -p electrode up

prod: | build
	docker-compose -f docker-compose.yml -p electrode up

bash:
	docker-compose exec app bash

build:
	docker build -t electrode .

#deploy: | build
#    docker tag dunai ${ECS_URL}:latest
#    docker push ${ECS_URL}:latest


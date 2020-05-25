## build and run
build-and-run:
	docker rm -vf $$(docker ps -a -q) || true
	docker-compose build && docker-compose up

## run
run:
	docker rm -vf $$(docker ps -a -q) || true
	docker-compose up

#run to do migrations
migrate:
	docker-compose run python sh -c "python manage.py makemigrations && python manage.py migrate"

#run if app runns first time
first-time:migrate

#createsuperuser
migrate:
	docker-compose run python sh -c "python manage.py createsuperuser"


.PHONY: up down build logs migrate makemigrations shell test lint

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose up --build -d

logs:
	docker compose logs -f

migrate:
	docker compose exec web python manage.py migrate --noinput

makemigrations:
	docker compose exec web python manage.py makemigrations

shell:
	docker compose exec web python manage.py shell

test:
	docker compose exec web python manage.py test

lint:
	poetry run flake8

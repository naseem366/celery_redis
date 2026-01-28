build-app-flask:
	docker build . -t flask-app-api-image -f Dockerfile.production

run-app-flask:
	docker compose -f docker-compose-flask.yml up -d

stop-app-flask:
	docker compose -f docker-compose-flask.yml down

dev-run-flask:
	python3 app.py

restart:
	docker-compose-flask.yml down && docker-compose-flask.yml up

logs:
	docker compose logs -f

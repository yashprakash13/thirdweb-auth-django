server-build:
	poetry install

server-run:
	poetry run python manage.py runserver

web-build:
	cd web && npm install

web-run:
	cd web && npm run dev

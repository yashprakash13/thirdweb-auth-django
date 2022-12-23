server-run:
	python manage.py runserver

web-build:
	cd web && npm install

web-run:
	cd web && npm run dev

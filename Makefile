dev:
	docker build -t django-first-app .
	docker run --rm -it -p 8000:8000 django-first-app

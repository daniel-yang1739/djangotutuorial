dev:
	docker build -t djangotutorial .
	docker run --rm -it -v .:/djangotutorial -p 8000:8000 djangotutorial

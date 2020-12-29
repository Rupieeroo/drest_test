test:
	docker build . -t app && \
	docker run app

prune:
	docker system prune -af
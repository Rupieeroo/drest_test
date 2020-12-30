test:
	docker build . -t ios_event && \
	docker run ios_event

prune:
	docker system prune -af
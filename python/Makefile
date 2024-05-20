# Build Docker image
build:
	docker build -t drp-image .

# Run Docker container in interactive mode and mount current directory to /local
run: build
	docker run -it --rm -v $(shell pwd):/local drp-image

.PHONY: build run
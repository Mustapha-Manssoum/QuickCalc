FROM python:3.12-slim

WORKDIR /app

COPY . /app

EXPOSE 8080

# environment variable for host binding (0.0.0.0 for Docker)
ENV HOST=0.0.0.0
ENV PORT=8080

CMD ["python", "server.py"]
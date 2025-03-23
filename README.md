# Installation Guide

## Docker Setup


### Steps
```bash
git clone https://github.com/yourusername/yourproject.git
cd yourproject

docker-compose up -d

docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser
```

Application runs at `http://localhost:8000`

## API Documentation

API docs are generated with drf-spectacular and available at:

- Swagger UI: `http://localhost:8000/api/schema/swagger-ui/`



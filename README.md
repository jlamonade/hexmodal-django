# hexmodal-django

Django + DRF API for tracking LoRa/LoRaWAN devices and their payloads.

## Project layout

```
hexmodal-django/
├── config/       # Django project (settings, urls, wsgi, asgi)
├── hexmodal/     # App (models, views, serializers, admin)
├── manage.py
└── requirements.txt
```

## Startup

### 1. Clone and enter the project

```bash
git clone <repo-url>
cd hexmodal-django
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (for the admin and the browsable API)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The server starts at `http://localhost:8000/`.

## Endpoints

| URL | Purpose |
|---|---|
| `/admin/` | Django admin |
| `/api/` | DRF browsable API root |
| `/api/devices/` | Device list / create |
| `/api/devices/<id>/` | Device detail / update / delete |
| `/api/payloads/` | Payload list / create |
| `/api/payloads/<fCnt>/` | Payload detail / update / delete |

Authentication is `BasicAuth` — log in with the superuser credentials when hitting the browsable API.

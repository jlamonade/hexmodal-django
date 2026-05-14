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

```bash
git clone <repo-url>
cd hexmodal-django
make run
```

That's it. `make run` will:

1. Create a virtualenv (`venv/`) if missing
2. Install dependencies from `requirements.txt`
3. Apply migrations
4. Create a default superuser (`admin` / `admin`) if one doesn't exist
5. Start the dev server at `http://localhost:8989/`

Subsequent `make run`s skip steps 1–4 (they're idempotent) and just boot the server.

### Other targets

| Command | What it does |
|---|---|
| `make install` | Just create venv and install deps |
| `make migrate` | Run migrations |
| `make superuser` | Create the default `admin` / `admin` superuser |
| `make clean` | Wipe `db.sqlite3` and migrations (forces fresh schema next run) |

### Manual setup (no Make)

If you'd rather skip the Makefile:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # interactive
python manage.py runserver 8989
```

## Endpoints

| URL | Purpose |
|---|---|
| `/admin/` | Django admin |
| `/api/` | DRF browsable API root |
| `/api/devices/` | Device list / create |
| `/api/devices/<devEUI>/` | Device detail / update / delete |
| `/api/payloads/` | Payload list / create |
| `/api/payloads/<id>/` | Payload detail / update / delete |

Authentication is `BasicAuth` — log in with the superuser credentials when hitting the browsable API.

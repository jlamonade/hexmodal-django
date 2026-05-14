.PHONY: install migrate superuser run clean

VENV := venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PORT := 8989

install:
	@test -d $(VENV) || python3 -m venv $(VENV)
	@$(PIP) install -q -r requirements.txt

migrate: install
	@$(PY) manage.py makemigrations hexmodal
	@$(PY) manage.py migrate

superuser: migrate
	@DJANGO_SUPERUSER_USERNAME=admin \
	 DJANGO_SUPERUSER_PASSWORD=admin \
	 DJANGO_SUPERUSER_EMAIL=admin@example.com \
	 $(PY) manage.py createsuperuser --noinput 2>/dev/null || true

run: superuser
	@echo ""
	@echo "Server starting at http://localhost:$(PORT)/"
	@echo "Admin login:   admin / admin"
	@echo ""
	@$(PY) manage.py runserver $(PORT)

clean:
	rm -f db.sqlite3
	find hexmodal/migrations -name "0*.py" -delete
	rm -rf hexmodal/migrations/__pycache__

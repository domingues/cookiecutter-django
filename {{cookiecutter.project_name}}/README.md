# {{cookiecutter.project_title}}

{{cookiecutter.project_description}}

## Install and run

### Development

#### Install
```bash
git clone {{cookiecutter.project_repo}} {{cookiecutter.project_name}}
```
```bash
cd {{cookiecutter.project_name}}
```
```bash
pip install -e .
```

#### Config
```bash
cat > .env << DOTENV
SECRET_KEY=
DEBUG=true
INTERNAL_IPS=127.0.0.1
DOTENV
```

#### Prepare
```bash
./manage.py compilemessages
```
```bash
./manage.py migrate
```

#### Run
```bash
./manage.py runserver
```

### Production

#### Install
Replace `$VERSION` with the desired version number, e.g. `1.0.0`.
```bash
pip install {{cookiecutter.project_name}}@git+{{cookiecutter.project_repo}}@$VERSION
```

#### Config
Read the official [deployment checklist](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/).
```bash
export DJANGO_SETTINGS_MODULE={{cookiecutter.python_namespace}}.{{cookiecutter.project_slug}}.settings
```
```bash
cat > .env << DOTENV
SECRET_KEY=
ALLOWED_HOSTS=
DOTENV
```

#### Prepare
```bash
django-admin collectstatic
```
```bash
django-admin compilemessages
```
```bash
django-admin migrate
```

#### Run
```bash
gunicorn {{cookiecutter.python_namespace}}.{{cookiecutter.project_slug}}.wsgi
```
And serve static files of `$PWD/static/` and `$PWD/media/` on HTTP `/static/` and `/media/`.

# Environment variables

| Name             | Default value                    | Description |
| ---------------- | -------------------------------- | ----------- |
| PROJECT_BASE_DIR | `''` (current working directory) | Folder containing the project runtime files: `.env`, databases, media and collected statics. |
| LOAD_DOTENV      | `True`                           | Try to load environment variables from `$PROJECT_BASE_DIR/.env` file. |
| SECRET_KEY       |                                  | Django [`SECRET_KEY`](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) setting. |
| DEBUG            | `False`                          | Django [`DEBUG`](https://docs.djangoproject.com/en/3.2/ref/settings/#debug) setting. |
| ALLOWED_HOSTS    | `[]`                             | Django [`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts) setting. |
| INTERNAL_IPS     | `[]`                             | Django [`INTERNAL_IPS`](https://docs.djangoproject.com/en/3.2/ref/settings/#internal-ips) setting. Also used to activate the debug toolbar. |

Usage Instructions

Clone the structure and customize for your project
Set environment variables using the .env.example template
Install dependencies: pip install -r requirements/development.txt
Run migrations: python manage.py migrate
Create superuser: python manage.py setup_project
Start development server: python manage.py runserver --settings=config.settings.development

### Quick start
# 1. Create your project
django-admin startproject --template=this_structure myproject

# 2. Setup environment
cp .env.example .env
# Edit .env with your values

# 3. Install dependencies
pip install -r requirements/development.txt

# 4. Setup database
python manage.py migrate --settings=config.settings.development
python manage.py setup_project --settings=config.settings.development

# 5. Run development server
python manage.py runserver --settings=config.settings.development


### p=deployment
# Using Docker
docker-compose -f docker-compose.prod.yml up -d

# Or traditional deployment
pip install -r requirements/production.txt
python manage.py collectstatic --settings=config.settings.production
gunicorn --bind 0.0.0.0:8000 config.wsgi:application

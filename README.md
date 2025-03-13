# Website Developed During Django Girls Workshop

## Run locally
1. Create venv (vitual environment)
   ```
   python3 -m venv .venv
   ```
2. Activate it
   ```
   source .venv/bin/activate
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Create migration files
   ```
   python manage.py makemigrations
   ```
5. Apply migrations
   ```
   python manage.py migrate
   ```
6. Run dev server
   ```
   python manage.py runserver 0.0.0.0:8000
   ```

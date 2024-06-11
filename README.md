# mera-gurukul-backend-app

## Steps to run project

1. Clone repository

   ```bash
   git clone git@github.com:Hi-Cypher/mera-gurukul-backend-app.git
   ```

2. Create virtual environment

   ```bash
   python3 -m venv .venv
   ```

3. Activate virtual environment

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations

   ```bash
   python manage.py migrate
   ```

6. Run development server

   ```bash
   python manage.py runserver
   ```

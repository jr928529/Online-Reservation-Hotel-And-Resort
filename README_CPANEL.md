# Deployment Instructions for cPanel (Shared Hosting)

This guide explains how to deploy this Django project on cPanel hosting (e.g., Namecheap, Bluehost, HostGator) using the **"Setup Python App"** tool.

## Prerequisites

1. A cPanel hosting account.
2. Domain or Subdomain pointed to your hosting.
3. Your project files uploaded to the server (usually via FTP or Git).

## Deployment Steps

### 1. Create the Python App in cPanel
1. Log in to your cPanel dashboard.
2. Search for **"Setup Python App"** and open it.
3. Click **"Create Application"**.
4. Set the following:
   - **Python Version**: `3.10` or higher (recommended).
   - **Application Root**: The folder where you uploaded your project (e.g., `hotel_reservation_app`).
   - **Application URL**: Select your domain and path.
   - **Application Startup File**: `passenger_wsgi.py`
   - **Application Entry Point**: `application`
5. Click **"Create"**.

### 2. Configure Environment & Dependencies
1. Once created, cPanel will provide a command to enter your virtual environment. It looks like:
   `source /home/username/nodevenv/hotel_reservation_app/3.10/bin/activate && cd /home/username/hotel_reservation_app`
2. Connect to your server via **SSH** and run that command.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   pip install gunicorn  # Recommended for production
   ```

### 3. Setup Django Settings
Edit `hotel_reservation/settings.py` on your server:
- `DEBUG = False`
- `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']`
- Ensure `STATIC_ROOT` is defined:
  ```python
  STATIC_ROOT = os.path.join(BASE_DIR, 'public_html/static') # Or wherever your domain path is
  ```

### 4. Database & Static Files
In your SSH terminal (inside the virtual environment):
```bash
python manage.py migrate
python manage.py collectstatic
```

### 5. Passenger WSGI Configuration
Ensure the `passenger_wsgi.py` file is in your application root folder. This file tells the server how to run your Django app.

## Passenger WSGI Example
The `passenger_wsgi.py` file should look like this:
```python
import os
import sys

# Path to your project directory
sys.path.insert(0, os.getcwd())

# Path to your settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'hotel_reservation.settings'

from hotel_reservation.wsgi import application
```

## Troubleshooting
- **500 Internal Server Error**: Check the `stderr.log` file in your application root.
- **Static Files Not Loading**: Ensure `STATIC_ROOT` is correct and you ran `collectstatic`.
- **Database Errors**: If using SQLite, ensure the folder containing `db.sqlite3` has write permissions for the server user.

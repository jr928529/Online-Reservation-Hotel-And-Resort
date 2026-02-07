# Deployment Instructions for Render

This project is configured to be deployed as a **Web Service** on Render.

## Prerequisites

1. Create a [Render](https://render.com/) account.
2. Connect your GitHub/GitLab repository to Render.

## Deployment Steps

1. **Create a New Web Service**:
   - Select your repository.
   - **Language**: `Python`
   - **Branch**: `main` (or your preferred branch)
   - **Build Command**: `./render-build.sh`
   - **Start Command**: `gunicorn hotel_reservation.wsgi`

2. **Environment Variables**:
   Add the following environment variables in the Render dashboard:
   - `SECRET_KEY`: A long, random string (keep it secret!).
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render URL (e.g., `your-app.onrender.com`).
   - `PYTHON_VERSION`: `3.12.0` (optional, as specified in `runtime.txt`)
   - `DATABASE_URL`: If you decide to use a managed PostgreSQL database later, simply add its URL here. The app will automatically switch from SQLite.

3. **SQLite Note**:
   By default, this setup uses **SQLite** (`db.sqlite3`).
   > [!WARNING]
   > Render Web Services have an ephemeral filesystem. Any data saved to SQLite will be lost whenever the service restarts or redeploys. For production use, it is highly recommended to use a managed database like **Render PostgreSQL**.

## Local Testing

To test the production setup locally:

1. Install dependencies: `pip install -r requirements.txt`
2. Run build script (Unix/Mac): `chmod +x render-build.sh && ./render-build.sh`
3. Run with Gunicorn: `gunicorn hotel_reservation.wsgi`

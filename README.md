# Django Postgres Template with Ngrok and Social Auth

A versatile and pre-configured Django starter template designed to streamline your development process. This template includes all the essential configurations and tools needed for modern web applications.

---

## Features

- **Database**: Pre-configured for PostgreSQL.
- **Ngrok Integration**: Commands to easily start tunnels and update project settings dynamically.
- **Django Allauth**: Social account authentication for Google, GitHub, and Facebook.
- **Email Verification**: Integrated email verification for secure user registrations.
- **Custom User Model**: Includes a pre-built user model for flexibility.
- **Commands**:
  - `start_ngrok`: Start a Ngrok tunnel and expose your local server to the internet.
  - `get_ngrok_url`: Automatically updates `ALLOWED_HOSTS` and `BASE_URL` with the Ngrok public URL.
  - `configure_site`: Set up the site domain and name in the database.

---

## Installation and Setup

### Requirements

- **Python**: 3.13.0 (recommended).
- **Virtualenv**: Ensure `virtualenv` is installed before starting.
- **PostgreSQL**: A running PostgreSQL instance for the database.

---

### Step 1: Download the Template

1. Download the repository as a ZIP file from GitHub.
2. Extract the ZIP file and rename the folder to match your project name.

---

### Step 2: Create a Virtual Environment

```bash
virtualenv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure the Database

1. Create a new PostgreSQL database and user:

```sql
CREATE DATABASE your_database_name;
CREATE USER your_user_name WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user_name;
```

2. Fill out the .env file with your database credentials:

```env
DB_NAME='db_name_here'
DB_USER='db_user_here'
DB_PASSWORD='db_password_here'
DB_HOST='db_host_here'
DB_PORT='db_port_here'
```

---

### Step 5: Fill out the .env

```env
NGROK_AUTHTOKEN='your_ngrok_auth_token_here'
NGROK_API_KEY='your_ngrok_api_key_here'
FACEBOOK_CLIENT_ID='your_facebook_client_id_here'
FACEBOOK_CLIENT_SECRET='your_facebook_client_secret_here'
GOOGLE_CLIENT_ID='your_google_client_id_here'
GOOGLE_CLIENT_SECRET='your_google_client_secret_here'
GITHUB_CLIENT_ID='your_github_client_id_here'
GITHUB_CLIENT_SECRET='your_github_client_secret_here'
DJANGO_SECRET='your_django_secret_here'
APP_NAME='your_app_name_here'
```

---

### Step 6(optional): Start Ngrok

1. Start Ngrok:

```bash
python manage.py start_ngrok
```

2. Update URL Settings:

```bash
python manage.py get_ngrok_url
```

These commands dynamically update ALLOWED_HOSTS and BASE_URL to use your Ngrok public URL.

---

### Step 7: Initialize the Project

1. Run the site configuration command:

```bash
python manage.py configure_site
```

2. Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 8: Start the Server

```bash
python manage.py runserver
```

---

## License

This template is licensed under the MIT License. Feel free to use and modify it with attribution.

---

## Author

- **Gastón Gómez Cuello**
- [GitHub](https://github.com/gastongomezcuello)
- [Email](mailto:gastongomezcuello@gmail.com)

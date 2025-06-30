

# Show Main API

## Setup & Run Instructions

### 1. Clone the repository and enter the project directory

```sh
git clone <your-repo-url>
cd "show-main (1)/show-main"
```

### 2. Create and activate a virtual environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project root with the following content:

```
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your-very-secret-key
```

You can change these values as needed.

### 5. Set the Flask app environment variable

```sh
export FLASK_APP=server.app
```

### 6. Run database migrations (optional, if using Flask-Migrate)

```sh
flask db upgrade
```

### 7. Start the development server

```sh
flask run
```

The API will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Notes

- Make sure your Python interpreter matches the one used to install dependencies.
- If you use a different database, update `DATABASE_URL` in your `.env` file accordingly.
- For production, set a strong `JWT_SECRET_KEY` and configure your web server appropriately.

# 📰 CMS Backend

A FastAPI-based backend for a simple Content Management System (CMS).
Supports user authentication, article CRUD, and JWT-based access.

---

## 🚀 Features

* User registration and login with JWT
* Create, read, update, delete (CRUD) articles
* Seed fake articles using Faker
* RESTful API using FastAPI
* Dockerized with PostgreSQL

---

## 🧱 Tech Stack

* **Backend**: FastAPI, SQLAlchemy
* **Database**: PostgreSQL
* **Auth**: JWT
* **Testing**: Pytest
* **Containerization**: Docker, Docker Compose

---

## 📦 Getting Started

### ⚖️ Prerequisites

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

---

### ⚙️ Run the Backend

```bash
git clone https://github.com/yourname/cms-backend.git
cd cms-backend

# Build and run services
docker compose up --build
```

The API will be available at:
📍 `http://localhost:8000`

Docs:
📚 `http://localhost:8000/docs` (Swagger UI)

---

### 🧲 Run Tests (Locally)

If you want to test outside Docker:

```bash
# Create and activate virtualenv
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```

> ✅ Make sure your PostgreSQL DB is running and configured in `.env` or `database.py`.

---

### 🌱 Seeding the Database

To insert fake articles using Faker:

```bash
docker compose exec web python seed.py
```

You can adjust the number of articles in `seed.py`.

---

### 🧲 Example: Testing API with cURL

```bash
# Register a new user
curl -X POST http://localhost:8000/auth/register -H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass"}'

# Login and get token
curl -X POST http://localhost:8000/auth/login -H "Content-Type: application/json" \
-d '{"username": "testuser", "password": "testpass"}'

# Create article
curl -X POST http://localhost:8000/articles/ \
-H "Authorization: Bearer <your_token>" \
-H "Content-Type: application/json" \
-d '{"title": "My First Article", "content": "Hello world!"}'
```

---

## 🧼 Clean Up

```bash
docker compose down -v
```

---

## 📄 License

MIT – feel free to use, improve, and contribute 🎉

---

## 👤 Author

* [Your Name](https://github.com/yourgithub)

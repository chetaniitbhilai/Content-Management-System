# 🧠 CMS Backend API (FastAPI + Docker)

This is the backend service for the **CMS** (Content Management System) built using **FastAPI**, **PostgreSQL**, and **Docker**.
It supports user authentication, article CRUD, and tracking recently viewed articles.

---

## 📦 Tech Stack

* **FastAPI** - Web framework
* **PostgreSQL** - Database
* **SQLAlchemy** - ORM
* **Docker & Docker Compose** - Containerization
* **Pytest** - Testing

---

## 🚀 Getting Started with Docker

### ✅ Prerequisites

* [Docker](https://www.docker.com/) installed and running

### 🔧 Setup & Run

1. **Clone the repo**

```bash
git clone https://github.com/chetaniitbhilai/Content-Management-System.git
cd Content-Management-System
```

2. **Start containers**

```bash
docker compose up --build
```

* Web API will be running at: `http://localhost:8000`
* PostgreSQL exposed at: `localhost:5432`

---

## 🧪 Running Tests (via Docker)

```bash
docker compose exec app pytest
```

This runs all tests located in `tests/` using the container environment.

---

## 🧪 Seed Fake Articles

```bash
docker compose exec app python seed.py
```

---

## 📬 API Usage via `curl`

All endpoints are accessible at `http://localhost:8000`. Use the token returned from login for authorized routes.

### 1. 📝 Register

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'
```

### 2. 🔐 Login

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass"}'
```

Save the `token`:

```bash
export TOKEN=your_token_here
```

### 3. ➕ Create Article

```bash
curl -X POST http://localhost:8000/articles/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Article", "content": "This is the body."}'
```

### 4. ✏️ Update Article

```bash
curl -X PUT http://localhost:8000/articles/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title", "content": "Updated content"}'
```

### 5. 📄 Get Single Article

```bash
curl -X GET http://localhost:8000/articles/1 \
  -H "Authorization: Bearer $TOKEN"
```

### 6. 📚 Get All Articles

```bash
curl -X GET http://localhost:8000/articles/ \
  -H "Authorization: Bearer $TOKEN"
```

### 7. 👁️ Recently Viewed Articles

```bash
curl -X GET http://localhost:8000/articles/recently-viewed \
  -H "Authorization: Bearer $TOKEN"
```

---

## 🐳 Docker Compose Setup

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  db:
    image: postgres:15
    container_name: cms-db
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: cms
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  web:
    build: .
    container_name: cms-app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgres://user:password@db:5432/cms

volumes:
  pgdata:
```

### `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 👥 Contributions

PRs are welcome! Please run tests before submitting changes.

---

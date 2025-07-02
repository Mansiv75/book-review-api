
### 📄 `README.md`

```markdown
# 📚 Book Review API

A backend API built with **Flask**, supporting CRUD operations on books and reviews. Includes Redis caching, Swagger docs, error handling, and tests — all designed for scalability, clarity, and production-readiness.

---

## 🚀 Features

- Create and list books
- Create and list reviews for a book
- Redis caching for books list with graceful fallback
- Swagger (OpenAPI) documentation
- Automated unit and integration testing
- SQLite-based ORM with SQLAlchemy
- Error handling for bad requests, 404s, and server issues

---

## 📂 Project Structure

```

app/
├── **init**.py
├── models.py
├── cache.py
├── errors.py
├── routes/
│   ├── **init**.py
│   ├── books.py
│   └── reviews.py
tests/
├── **init**.py
├── test\_books.py
├── test\_cache.py
migrations/
app.py
config.py
requirements.txt
README.md

````

---

## 🛠️ Setup Instructions

### 🔧 Local Development

```bash
git clone https://github.com/Mansiv75/book-review-api
cd book-review-api
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
````

### 🔌 Environment Configuration

The default config uses SQLite. No `.env` needed unless customizing.

---

## 🧱 Database Setup

```bash
export FLASK_APP=app.py     # Windows: set FLASK_APP=app.py
flask db init               # Only once
flask db migrate -m "init"
flask db upgrade
```

---

## 🚀 Running the App

```bash
flask run
```

Your app will run at:

* **Base URL (Local)**: `http://localhost:5000/`
* **Swagger Docs**: `http://localhost:5000/apidocs/`

---

## 📘 API Documentation

### ✅ `GET /books`

* **Description**: Retrieve a list of all books.
* **Returns**: Array of book objects.
* **Cache**: Uses Redis cache (TTL = 60 sec)

**Live**: [GET /books](#)
**Swagger**: [Docs](http://localhost:5000/apidocs/#/Books/get_books_books_get)

---

### ✅ `POST /books`

* **Description**: Add a new book.
* **Payload Example**:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "published_date": "2018-10-16"
}
```

**Live**: [POST /books](#)
**Swagger**: [Docs](http://localhost:5000/apidocs/#/Books/create_book_books_post)

---

### ✅ `GET /books/<id>/reviews`

* **Description**: Fetch reviews for a specific book.
* **Path Param**: `id` – book ID
* **Returns**: Array of reviews.

**Live**: [GET /books/1/reviews](#)
**Swagger**: [Docs](http://localhost:5000/apidocs/#/Reviews/get_reviews_books__book_id__reviews_get)

---

### ✅ `POST /books/<id>/reviews`

* **Description**: Add a review to a book.
* **Payload Example**:

```json
{
  "rating": 5,
  "comment": "Masterpiece!"
}
```

**Live**: [POST /books/1/reviews](#)
**Swagger**: [Docs](http://localhost:5000/apidocs/#/Reviews/create_review_books__book_id__reviews_post)

---

## 🧪 Testing

### ✅ Run All Tests

```bash
pytest
```

Tests include:

* Creating and fetching books
* Adding and listing reviews
* Redis caching mock test
* Cache-miss DB fallback

---

## 🧰 Redis Setup (Optional)

### 📦 Run Redis Locally

```bash
docker run -p 6379:6379 redis
```

> If Redis is not running, the app automatically skips caching and hits the database — no crash.

---

## 🌍 Live Deployment (Add links here)

* **Base URL**: [https://your-api-url.com](#)
* **Swagger UI**: [https://your-api-url.com/apidocs](#)
* **Example**:

  * `GET /books` → [Try Now](#)
  * `POST /books` → [Try Now](#)

---

## 🎥 Suggested Demo Flow

1. Create a book → `POST /books`
2. Fetch books → `GET /books` (watch it cache)
3. Add a review → `POST /books/{id}/reviews`
4. Fetch reviews → `GET /books/{id}/reviews`
5. Kill Redis (optional) → show graceful fallback
6. Run tests → `pytest`

---

## 📌 Tech Stack

| Tool       | Purpose                 |
| ---------- | ----------------------- |
| Flask      | Web framework           |
| SQLAlchemy | ORM                     |
| SQLite     | Local DB                |
| Redis      | Caching                 |
| Flasgger   | Swagger docs            |
| Pytest     | Unit testing            |
| Fakeredis  | Redis mocking for tests |


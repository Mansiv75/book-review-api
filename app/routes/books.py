from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
from ..models import db, Book
from ..cache import get_cached_books, set_cached_books

books_bp = Blueprint("books", __name__)

@books_bp.route("/", methods=["GET"])
@swag_from({
    'tags': ['Books'],
    'responses': {
        200: {
            'description': 'List of books',
            'examples': {
                'application/json': [
                    {"id": 1, "title": "Book A", "author": "Author A"}
                ]
            }
        }
    }
})
def get_books():
    cached = get_cached_books()
    if cached:
        return jsonify(cached), 200

    books = Book.query.all()
    result = [
        {"id": b.id, "title": b.title, "author": b.author, "published_date": b.published_date.isoformat() if b.published_date else None}
        for b in books
    ]

    set_cached_books(result)
    return jsonify(result), 200


@books_bp.route("/", methods=["POST"])
@swag_from({
    'tags': ['Books'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'properties': {
                    'title': {'type': 'string'},
                    'author': {'type': 'string'},
                    'published_date': {'type': 'string', 'format': 'date'}
                },
                'required': ['title', 'author']
            }
        }
    ],
    'responses': {
        201: {'description': 'Book created successfully'}
    }
})
def create_book():
    data = request.get_json()
    if not data.get("title") or not data.get("author"):
        return jsonify({"error": "Missing title or author"}), 400

    book = Book(
        title=data["title"],
        author=data["author"],
        published_date=data.get("published_date")
    )
    db.session.add(book)
    db.session.commit()

    # Optional: clear cache to reflect new book
    set_cached_books(None)

    return jsonify({"message": "Book created", "id": book.id}), 201

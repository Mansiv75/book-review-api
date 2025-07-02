# app/routes/books.py

from flask import Blueprint

books_bp = Blueprint('books', __name__)

@books_bp.route("/", methods=["GET"])
def get_books():
    return {"message": "Books endpoint working"}

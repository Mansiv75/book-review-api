from flask import Blueprint, request, jsonify
from flasgger.utils import swag_from
from ..models import db, Review, Book

reviews_bp = Blueprint("reviews", __name__)

@reviews_bp.route("/<int:book_id>/reviews", methods=["GET"])
@swag_from({
    'tags': ['Reviews'],
    'parameters': [
        {
            'name': 'book_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
        }
    ],
    'responses': {
        200: {
            'description': 'List of reviews for the book',
            'examples': {
                'application/json': [
                    {"id": 1, "rating": 5, "comment": "Great!", "created_at": "2024-01-01T00:00:00"}
                ]
            }
        },
        404: {'description': 'Book not found'}
    }
})
def get_reviews(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    reviews = Review.query.filter_by(book_id=book_id).all()
    result = [
        {"id": r.id, "rating": r.rating, "comment": r.comment, "created_at": r.created_at.isoformat()}
        for r in reviews
    ]
    return jsonify(result), 200


@reviews_bp.route("/<int:book_id>/reviews", methods=["POST"])
@swag_from({
    'tags': ['Reviews'],
    'parameters': [
        {
            'name': 'book_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
        },
        {
            'name': 'body',
            'in': 'body',
            'schema': {
                'properties': {
                    'rating': {'type': 'integer'},
                    'comment': {'type': 'string'}
                },
                'required': ['rating']
            }
        }
    ],
    'responses': {
        201: {'description': 'Review created'},
        404: {'description': 'Book not found'}
    }
})
def create_review(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
    rating = data.get("rating")
    comment = data.get("comment", "")

    if rating is None:
        return jsonify({"error": "Rating is required"}), 400

    review = Review(book_id=book_id, rating=rating, comment=comment)
    db.session.add(review)
    db.session.commit()

    return jsonify({"message": "Review added", "id": review.id}), 201

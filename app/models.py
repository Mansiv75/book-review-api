from . import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    published_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    reviews = db.relationship("Review", backref="book", lazy=True)

    def __repr__(self):
        return f"<Book {self.title}>"

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(
        db.Integer, 
        db.ForeignKey("book.id"), 
        nullable=False,
        index=True  
    )
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Review Book {self.book_id} Rating {self.rating}>"

import random
from faker import Faker
from app import create_app, db
from app.models import Book, Review

fake = Faker()

def seed_data():
    app = create_app()
    with app.app_context():
        # Clean existing data
        Review.query.delete()
        Book.query.delete()
        db.session.commit()

        books = []
        for _ in range(15):
            book = Book(
                title=fake.sentence(nb_words=3),
                author=fake.name(),
                published_date=fake.date_between(start_date='-10y', end_date='today')
            )
            db.session.add(book)
            books.append(book)

        db.session.commit()

        review_count = 0
        for book in books:
            num_reviews = random.randint(0, 4)
            for _ in range(num_reviews):
                review = Review(
                    book_id=book.id,
                    rating=random.randint(1, 5),
                    comment=fake.sentence(nb_words=10)
                )
                db.session.add(review)
                review_count += 1

        db.session.commit()
        print(f"✅ Seeded: {len(books)} books, {review_count} reviews")

if __name__ == "__main__":
    seed_data()

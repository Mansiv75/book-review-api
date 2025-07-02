def test_create_book(client):
    res = client.post("/books/", json={
        "title": "Test Book",
        "author": "Test Author"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["message"] == "Book created"
    assert "id" in data

def test_get_books(client):
    client.post("/books/", json={"title": "T", "author": "A"})
    res = client.get("/books/")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_add_review_to_book(client):
    res = client.post("/books/", json={"title": "Test", "author": "Author"})
    book_id = res.get_json()["id"]

    review_res = client.post(f"/books/{book_id}/reviews", json={
        "rating": 5,
        "comment": "Loved it!"
    })

    assert review_res.status_code == 201
    review_data = review_res.get_json()
    assert review_data["message"] == "Review added"
    assert "id" in review_data

def test_get_reviews_for_book(client):
    res = client.post("/books/", json={"title": "B", "author": "A"})
    book_id = res.get_json()["id"]

    client.post(f"/books/{book_id}/reviews", json={
        "rating": 4,
        "comment": "Nice one"
    })

    res = client.get(f"/books/{book_id}/reviews")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["rating"] == 4

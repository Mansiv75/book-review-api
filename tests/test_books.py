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
    # Add one
    client.post("/books/", json={"title": "T", "author": "A"})
    res = client.get("/books/")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

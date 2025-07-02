import fakeredis
from app.cache import redis_client

def test_redis_mock(monkeypatch):
    fake_redis = fakeredis.FakeStrictRedis()
    monkeypatch.setattr(redis_client, "redis", fake_redis)

    redis_client.set("books", '["book1"]')
    result = redis_client.get("books")
    if isinstance(result, bytes):
        result = result.decode()
    assert result == '["book1"]'


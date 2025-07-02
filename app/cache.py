import json
from redis import Redis, RedisError

class RedisClient:
    def __init__(self):
        self.redis = None

    def init_app(self, app):
        try:
            self.redis = Redis(host="localhost", port=6379, decode_responses=True)
            self.redis.ping()
            print("Connected to Redis")
        except RedisError as e:
            print(f"Redis unavailable: {e}")
            self.redis = None

    def get(self, key):
        if not self.redis:
            return None
        try:
            return self.redis.get(key)
        except RedisError:
            return None

    def set(self, key, value, ex=60):
        if not self.redis:
            return
        try:
            self.redis.set(key, value, ex=ex)
        except RedisError:
            pass

redis_client = RedisClient()

def get_cached_books():
    data = redis_client.get("books")
    if data:
        return json.loads(data)
    return None

def set_cached_books(data):
    if data is None:
        redis_client.set("books", json.dumps([]), ex=0)  
    else:
        redis_client.set("books", json.dumps(data), ex=60)

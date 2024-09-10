from cachetools import TTLCache # https://github.com/tkem/cachetools

cache = TTLCache(maxsize=2, ttl=15)


if __name__ == "__main__":
    cache["key1"] = "Value for key1"

    print(cache.get("key1")) # value is cached 

    cache["key2"] = "Value for key2"
    print(cache.get("key2"))  # value is cached

    print(cache.get("key1"))  # key1 is not the least recently used key, it moved to the top of the cache
    cache["key3"] = "Value for key3"

    print(cache.get("key1")) # key1 is existed
    print(cache.get("key2")) # key2 is evicted from the cache, so it returns None
    print(cache.get("key3"))

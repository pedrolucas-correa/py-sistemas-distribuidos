#%% caching

class SimpleCache:
    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key, None)

    def set(self, key, value):
        self.cache[key] = value

cache = SimpleCache()
cache.set('a', 1)
print(cache.get('a'))

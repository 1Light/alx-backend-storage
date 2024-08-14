import requests
import redis
import time

# Initialize the Redis client
cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(expire_time=10):
    """Decorator to cache the page and track URL access count."""
    def decorator(func):
        def wrapper(url):
            cache_key = f"page:{url}"
            count_key = f"count:{url}"

            # Check if the page is in the cache
            cached_page = cache.get(cache_key)
            if cached_page:
                print(f"Cache hit for {url}")
                # Increment the access count
                cache.incr(count_key)
                return cached_page.decode('utf-8')

            print(f"Cache miss for {url}. Fetching from the web...")
            # Fetch the page from the web
            page_content = func(url)

            # Store the page content in the cache with expiration time
            cache.setex(cache_key, expire_time, page_content)

            # Initialize the count and increment
            cache.incr(count_key)

            return page_content
        return wrapper
    return decorator

@cache_page(expire_time=10)
def get_page(url: str) -> str:
    """Fetch the HTML content of the specified URL."""
    response = requests.get(url)
    return response.text

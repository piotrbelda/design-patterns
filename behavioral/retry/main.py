import random
import time
from functools import wraps
from typing import Any, Callable

import httpx

API_URL = "https://api.chucknorris.io/jokes/random"


def retry(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    def decorator[T](func: Callable[..., T]) -> Callable[..., T]:
        @wraps
        def wrapper(*args: Any, **kwargs: Any) -> T:
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries:
                        raise
                
                sleep_time = delay * (backoff ** attempt)
                print(f"Attempt {attempt} failed :(, retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)

        return wrapper

    return decorator


@retry()
def fetch_chuck_joke(threshold: float = 0.8) -> str:
    """Get random joke from Chuck Norris API"""
    if (random_value := random.random()) < threshold:
        raise ValueError(f"Value exceeded {random_value:0.3f}!")

    print(f"random value: {random_value:0.3f}")
    response = httpx.get(API_URL)
    data = response.json()
    return data["value"]


joke = fetch_chuck_joke()
print(f"The joke is: {joke}")

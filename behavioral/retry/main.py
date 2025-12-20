import random
import time
from typing import Callable

import httpx

API_URL = "https://api.chucknorris.io/jokes/random"


def fetch_chuck_joke(threshold: float = 0.8) -> str:
    if (random_value := random.random()) < threshold:
        raise ValueError(f"Value exceeded {random_value:0.3f}!")

    print(f"random value: {random_value:0.3f}")
    response = httpx.get(API_URL)
    data = response.json()
    return data["value"]


def retry[T](func: Callable[[], T], retries: int = 3, backoff: int = 1) -> T:
    try:
        return func()

    except Exception as e:
        if retries == 0:
            print("Cannot fetch result :(")
            raise

        print(f"Exception has occured: {str(e)}, trying again...")
        time.sleep(backoff)
        return retry(func, retries - 1, backoff)


joke = retry(fetch_chuck_joke)
print(f"The joke is: {joke}")

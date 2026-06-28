import requests, time, random
from config import HEADERS, TIMEOUT, MAX_RETRIES, MIN_DELAY, MAX_DELAY

def fetch(url):
    last_error = None
    for i in range(MAX_RETRIES):
        try:
            resp = requests.get(
                url,
                headers = HEADERS,
                timeout = TIMEOUT)
            resp.raise_for_status()
            return resp
        except requests.exceptions.RequestException as e:
            last_error = e 
            print(f"[Retry {i+1}] Failed: {url}")
            time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))
    print(f"[ERROR] {last_error}")
    return None


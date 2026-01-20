import time
import threading
import requests

def call_api(url: str, headers: dict = None, timeout_value: int = 10):
    start_time = time.time()

    try:
        response = requests.get(url=url, headers=headers, timeout=timeout_value)

    except requests.RequestException as exc:
        print(f"Request failed with exception: {exc}")

    end_time = time.time()
    print(f"{url} responded with status code: {response.status_code} and took {end_time-start_time} seconds\n")

apis = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/1",
]

print("\n\nMultithreading\n\n")

threads = []

start_time = time.time()

for api in apis:
    thread = threading.Thread(target=call_api, args=(api,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"Total Execution Time using Threading: {end_time-start_time} seconds\n\n")

print("\n\nSequential\n\n")

start_time = time.time()

for api in apis:
    call_api(api)

end_time = time.time()

print(f"Total Execution Time using Sequential: {end_time-start_time} seconds\n\n")

import time
import threading
import requests
import json


multithreading_results = []
lock = threading.Lock()


def call_api_multithreading(index: int, url: str, headers: dict = None, timeout_value: int = 10):
    start_time = time.time()

    try:
        response = requests.get(url=url, headers=headers, timeout=timeout_value)

    except requests.RequestException as exc:
        print(f"Request failed with exception: {exc}")

    end_time = time.time()
    with lock:
        multithreading_results.append({
            "index": index,
            "url": url,
            "status": response.status_code,
            "time": end_time - start_time,
            "thread_name": threading.current_thread().name,
            "thread_id": threading.get_ident(),
            "response": json.dumps(response.json(), indent=4, sort_keys=True),
        })


def call_api_sequential(index: int, url: str, headers: dict = None, timeout_value: int = 10):
    start_time = time.time()

    try:
        response = requests.get(url=url, headers=headers, timeout=timeout_value)

    except requests.RequestException as exc:
        print(f"Request failed with exception: {exc}")

    end_time = time.time()

    print(f"\n\n[{index}] Sequential\n\n")
    print(f"API       : {url}\n")
    print(f"Status    : {response.status_code}\n")
    print(f"Time Taken: {end_time - start_time} seconds\n")
    print(f"Response: ")
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print("\n")
    print("-" * 60)


def multithreading(apis):
    print(f"\n\n{'='*25} Multithreading {'='*25}")

    threads = []

    start_time = time.time()

    for index, api in enumerate(apis, start=1):
        thread = threading.Thread(target=call_api_multithreading, args=(index,api))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    for result in sorted(multithreading_results, key=lambda x: x["index"]):
        print(f"\n\n[{result['index']}] Multithreading\n\n")
        print(f"API        : {result['url']}\n")
        print(f"Status     : {result['status']}\n")
        print(f"Time Taken : {result['time']:.2f} seconds\n")
        print(f"Thread     : {result['thread_name']} (ID: {result['thread_id']})\n")
        print(f"Response:\n{result['response']}\n\n")
        print("-" * 60)

    print(f"\n\nTotal Execution Time using Threading: {end_time-start_time} seconds\n\n")


def sequential(apis):
    print(f"\n\n{'='*25} Sequential {'='*25}")

    start_time = time.time()

    for index, api in enumerate(apis,start=1):
        call_api_sequential(index, api)

    end_time = time.time()
    
    print(f"\n\nTotal Execution Time using Sequential: {end_time-start_time} seconds\n\n")


def main():
    apis = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/users/1",
    ]
    multithreading(apis)
    sequential(apis)


if __name__ == "__main__":
    main()
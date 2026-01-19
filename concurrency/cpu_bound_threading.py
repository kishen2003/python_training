import time
import threading

def cpu_task(n: int) -> None:
    total = 0
    for i in range(n):
        total += i * i

def main():
    start_time = time.time()
    threads = []
    for _ in range(3):
        thread = threading.Thread(target=cpu_task, args=(20_000_000,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Threaded execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

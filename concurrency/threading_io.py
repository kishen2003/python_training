import time
import threading

def io_task(task_id: int, delay: int) -> None:
    print(f"Task {task_id} started")
    time.sleep(delay)
    print(f"Task {task_id} finished")

def main():
    start_time = time.time()
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(
            target=io_task,
            args=(i, 2),
        )
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

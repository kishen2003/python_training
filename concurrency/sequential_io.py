import time

def io_task(task_id: int, delay: int) -> None:
    print(f"Task {task_id} started")
    time.sleep(delay)  # Simulates blocking I/O
    print(f"Task {task_id} finished")

def main():
    start_time = time.time()
    io_task(1, 2)
    io_task(2, 2)
    io_task(3, 2)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()

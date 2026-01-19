import time
from multiprocessing import Process

def cpu_task(n: int) -> None:
    total = 0
    for i in range(n):
        total += i * i

def main():
    start_time = time.time()
    processes = []
    for _ in range(3):
        process = Process(target=cpu_task, args=(20_000_000,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    end_time = time.time()
    print(f"Multiprocessing execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
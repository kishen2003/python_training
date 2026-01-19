import time

def cpu_task(n: int) -> int:
    total = 0
    for i in range(n):
        total += i * i
    return total

def main():
    start_time = time.time()
    cpu_task(20_000_000)
    cpu_task(20_000_000)
    cpu_task(20_000_000)
    end_time = time.time()
    print(f"Sequential execution time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
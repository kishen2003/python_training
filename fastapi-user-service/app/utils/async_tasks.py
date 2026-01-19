import asyncio

async def io_task(name: str, delay: int):
    await asyncio.sleep(delay)
    return f"Task {name} completed after {delay}s"

async def run_concurrent_tasks():
    results = await asyncio.gather(
        io_task("A", 2),
        io_task("B", 3),
        io_task("C", 1),
    )
    return results
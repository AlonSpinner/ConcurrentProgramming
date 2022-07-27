import asyncio
import time

async def async_sleep(n):
    print('before sleep', n)
    await asyncio.sleep(5)
    print('after sleep', n)

async def print_hello():
    print('hello')

async def main():
    start = time.time()
    await asyncio.gather(async_sleep(1), async_sleep(2), print_hello())
    print('total time:', time.time() - start)

if __name__ == "__main__":
    asyncio.run(main())

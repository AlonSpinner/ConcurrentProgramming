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
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(1),5), async_sleep(6), print_hello())
    except asyncio.TimeoutError:
        print('encountered a timeout error')
    
    print('total time:', time.time() - start)

if __name__ == "__main__":
    asyncio.run(main())

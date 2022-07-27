import asyncio

async def async_sleep():
    print('before sleep')
    await asyncio.sleep(5)
    print('after sleep')

async def print_hello():
    return 'hello'

async def main():
    await async_sleep()
    result = await print_hello()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import time
import requests
import aiohttp

async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def get_urls_with_requests(url):
    return requests.get(url).text

async def main():
    urls = ['https://google.com',
        'https://wikipedia.org/wiki/Concurrency',
        'https://python.org',
        'https://pypi.org/project/requests/',
        'https://docs.python.org/3/library/asyncio-task.html',
        'https://www.apple.com/',
        'https://medium.com']


    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_urls_with_requests(url)))
    async_text_response = await asyncio.gather(*tasks)
    end = time.time()
    print('requests took:', end - start, 'seconds')


    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))
    async_text_response = await asyncio.gather(*tasks)
    end = time.time()
    print('requests took:', end - start, 'seconds')

if __name__ == "__main__":
    asyncio.run(main())

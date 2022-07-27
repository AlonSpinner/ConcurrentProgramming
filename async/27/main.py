import asyncio


async def async_sleep(duration):
    await asyncio.sleep(duration)
    return duration

async def main():
    pending = set()
    for i in range(1,11):
        pending.add(asyncio.create_task(async_sleep(i)))

    while len(pending) > 0:
        done, pending = await asyncio.wait(pending, return_when = "FIRST_COMPLETED")
        print(done)
        print(pending)

if __name__ == "__main__":
    asyncio.run(main())

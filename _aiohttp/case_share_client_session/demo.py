import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results


async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/get",
        "https://httpbin.org/get",
    ]
    results = await fetch_all(urls)
    for i, result in enumerate(results):
        print(f"Result {i+1}: {result}")


# Run the main function
asyncio.run(main())

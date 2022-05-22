import asyncio

from aioairctrl import CoAPClient


async def main():
    client = await CoAPClient.create(host="192.168.0.213")
    print("GETTING INFO")
    print(await client.get_info())
    print("OBSERVING")
    async for s in client.observe_status():
        print("GOT STATE")
        print(s)
    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())

""" Httpx Async Client """
# pylint: disable=import-error
import asyncio
import httpx

async def main():
    """ Main """
    async with httpx.AsyncClient() as client:
        response = await client.get('https://pokeapi.co/api/v2/pokemon/45/')
        print(response.json())

asyncio.run(main())

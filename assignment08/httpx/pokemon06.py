import asyncio
import httpx

async def fetch_ability_list():
    url = "https://pokeapi.co/api/v2/ability/?limit=10"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()["results"]
async def fetch_ability_detail(ability):
    async with httpx.AsyncClient() as client:
        response = await client.get(ability["url"])
        data = response.json()
        return {
            "name": data["name"],
            "pokemon_count": len(data["pokemon"])
        }
def get_pokemon_count(item):
    return item["pokemon_count"]
async def main():
    ability_list = await fetch_ability_list()
    tasks = [fetch_ability_detail(a) for a in ability_list]
    results = await asyncio.gather(*tasks)
    sorted_results = sorted(results, key=get_pokemon_count, reverse=True)
    for a in sorted_results:
        print(f"{a['name']} → {a['pokemon_count']} Pokémon")
asyncio.run(main())

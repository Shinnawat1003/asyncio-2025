import asyncio
import httpx

# ดึง abilities 10 รายการแรกจาก API
async def fetch_ability_list():
    url = "https://pokeapi.co/api/v2/ability/?limit=10"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return data["results"]  # list of dicts: [{name, url}, ...]

# ดึงข้อมูล detail ของแต่ละ ability
async def fetch_ability_detail(ability):
    async with httpx.AsyncClient() as client:
        response = await client.get(ability["url"])
        data = response.json()
        return {
            "name": data["name"],
            "pokemon_count": len(data["pokemon"])
        }

# ฟังก์ชันช่วยเรียงจากมากไปน้อย 
def sort_by_pokemon_count(item):
    return item["pokemon_count"]

# main function
async def main():
    ability_list = await fetch_ability_list()
    
    tasks = [fetch_ability_detail(a) for a in ability_list]
    results = await asyncio.gather(*tasks)

    sorted_results = sorted(results, key=sort_by_pokemon_count, reverse=True)

    for ability in sorted_results:
        print(f"{ability['name']} → {ability['pokemon_count']} Pokémon")

asyncio.run(main())

import asyncio
import httpx

names = [
    "pikachu", "bulbasaur", "charmander", "squirtle", "eevee",
    "snorlax", "gengar", "mewtwo", "psyduck", "jigglypuff"
]

async def fetch_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return {
            "name": data["name"].title(),
            "id": data["id"],
            "base_experience": data["base_experience"]
        }

async def main():
    tasks = [fetch_pokemon_data(name) for name in names]
    results = await asyncio.gather(*tasks)

    # เรียงจาก base_experience มาก -> น้อย
    sorted_results = sorted(results, key=lambda x: x["base_experience"], reverse=True)

    # แสดงผล
    print("• Pokemon Data (sorted by base_experience):")
    for p in sorted_results:
        print(f"  {p['name']:12} | ID: {p['id']:3} | Base XP: {p['base_experience']}")

# รันโปรแกรม
asyncio.run(main())

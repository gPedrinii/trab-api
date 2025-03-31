import aiohttp
import asyncio
import json

def load_api_keys():
    with open("keys.json", "r") as file:
        keys = json.load(file)
    return keys["omdb_api_key"], keys["tmdb_api_key"]

async def fetch_omdb(title: str, year: int, omdb_api_key: str):
    url = f"http://www.omdbapi.com/?t={title}&y={year}&apikey={omdb_api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data.get("Plot", "Sinopse não encontrada")

async def fetch_tmdb_reviews(title: str, year: int, tmdb_api_key: str):
    search_url = f"https://api.themoviedb.org/3/search/movie?query={title}&year={year}&api_key={tmdb_api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url) as response:
            search_data = await response.json()
            if not search_data["results"]:
                return []

            movie_id = search_data["results"][0]["id"]
            reviews_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={tmdb_api_key}"
            async with session.get(reviews_url) as response:
                reviews_data = await response.json()
                return [review["content"] for review in reviews_data.get("results", [])[:3]]

async def main():
    title = input("Digite o título do filme: ")
    year = input("Digite o ano do filme: ")

    omdb_api_key, tmdb_api_key = load_api_keys()

    sinopse_task = fetch_omdb(title, int(year), omdb_api_key)
    reviews_task = fetch_tmdb_reviews(title, int(year), tmdb_api_key)

    sinopse, reviews = await asyncio.gather(sinopse_task, reviews_task)

    resultado = {
        "titulo": title,
        "ano": year,
        "sinopse": sinopse,
        "reviews": reviews
    }

    print(resultado)

    with open("output.json", "w") as output_file:
        json.dump(resultado, output_file, indent=4)

if __name__ == "__main__":
    asyncio.run(main())

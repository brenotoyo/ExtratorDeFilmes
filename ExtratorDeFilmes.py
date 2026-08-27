import requests
import time
import random
import concurrent.futures
import pandas as pd
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

MAX_THREADS = 10


def extract_movie_details(movie_link):
    time.sleep(random.uniform(0, 0.2))
    response = requests.get(movie_link, headers=headers, timeout=20)
    movie_soup = BeautifulSoup(response.content, "html.parser")

    detail_container = movie_soup.find("section", attrs={"data-testid": "movie-detail"})
    if detail_container is None:
        print(f"Detalhe do filme não encontrado: {movie_link}")
        return None

    title_tag = detail_container.find(attrs={"data-testid": "movie-title"})
    release_tag = detail_container.find(attrs={"data-testid": "movie-release"})
    rating_tag = detail_container.find(attrs={"data-testid": "movie-rating"})
    synopsis_tag = detail_container.find(attrs={"data-testid": "movie-synopsis"})

    title = title_tag.get_text(strip=True) if title_tag else None
    date = release_tag.get_text(strip=True).replace("Lançamento:", "").strip() if release_tag else None
    rating = rating_tag.get_text(strip=True).replace("Nota:", "").strip() if rating_tag else None
    plot_text = synopsis_tag.get_text(strip=True).replace("Sinopse:", "").strip() if synopsis_tag else None

    if all([title, date, rating, plot_text]):
        return {"Título": title, "Lançamento": date, "Nota": rating, "Sinopse": plot_text}
    return None


def extract_movies(soup):
    container = soup.find("section", attrs={"data-testid": "movies-list"})
    if container is None:
        print("Container principal não encontrado.")
        return []

    movies_table = container.find_all("article", attrs={"data-testid": "movie-item"})
    if not movies_table:
        print("Lista de filmes não encontrada.")
        return []

    movie_links = []
    for movie in movies_table:
        a_tag = movie.find("a", attrs={"data-testid": "movie-link"}, href=True)
        if a_tag:
            movie_links.append("https://havokkmorands.github.io/" + a_tag["href"])

    if not movie_links:
        print("Nenhum link de filme foi encontrado.")
        return []

    results = []
    threads = min(MAX_THREADS, len(movie_links))
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        for result in executor.map(extract_movie_details, movie_links):
            if result:
                results.append(result)

    return results


def extrair_filmes():
    """Função principal reutilizável: retorna um DataFrame com os filmes extraídos."""
    popular_movies_url = "https://havokkmorands.github.io/movie-catalog/"
    response = requests.get(popular_movies_url, headers=headers, timeout=20)

    soup = BeautifulSoup(response.content, "html.parser")
    dados = extract_movies(soup)

    return pd.DataFrame(dados)


def main():
    start_time = time.time()
    df = extrair_filmes()
    df.to_csv("Filmes.csv", index=False, encoding="utf-8")
    print(f"{len(df)} filmes salvos em Filmes.csv")
    print("Total time taken:", time.time() - start_time)


if __name__ == "__main__":
    main()
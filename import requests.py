import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
def decode_secret_message(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr")

    points = []

    for row in rows[1:]:  # skip header
        cols = row.find_all(["td", "th"])

        if len(cols) != 3:
            continue

        x = int(cols[0].get_text(strip=True))
        char = cols[1].get_text(strip=True)
        y = int(cols[2].get_text(strip=True))

        points.append((x, y, char))

    if not points:
        return

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, y, _ in points)

    grid = [[" " for _ in range(max_x + 1)]
            for _ in range(max_y + 1)]

    for x, y, char in points:
        grid[y][x] = char

    for row in grid:
        print("".join(row))
        
decode_secret_message(url)
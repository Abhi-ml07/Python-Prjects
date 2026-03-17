import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Title", "Price", "Availability"])

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find("p", class_="instock availability").text.strip()

            print("Title:", title)
            print("Price:", price)
            print("Availability:", availability)
            print("-" * 40)

            writer.writerow([title, price, availability])

    print("Data saved successfully to books_data.csv")

else:
    print("Failed to retrieve webpage")

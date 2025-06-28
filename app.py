from prefect import task, flow
import requests
from bs4 import BeautifulSoup

URL = "https://www.w3schools.com/python/python_intro.asp"

@task
def fetch_html():
    response = requests.get(URL)
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch URL: {response.status_code}")
    return response.content

@task
def extract_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    print("Links:")
    for link in links:
        print(link.get("href"))

@task
def extract_paragraphs(html):
    soup = BeautifulSoup(html, "html.parser")
    paras = soup.find_all("p")
    print("Paragraphs:")
    for p in paras:
        print(p.text.strip())

@task
def extract_images(html):
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")
    print("Images:")
    for i in imgs:
        print(i.get("src"))

@task
def extract_class_data(html, class_name):
    soup = BeautifulSoup(html, "html.parser")
    data = soup.find("div", class_=class_name)
    print(f"Data from class '{class_name}':\n{data}")

@flow
def scraping_pipeline():
    html = fetch_html()
    extract_links(html)
    extract_paragraphs(html)
    extract_images(html)
    extract_class_data(html, "footertext")
    extract_class_data(html, "classic")
    print("✅ Scraping finished!")

if __name__ == "__main__":
    scraping_pipeline()

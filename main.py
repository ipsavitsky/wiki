import requests
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from rich.console import Console
from rich.markdown import Markdown

console = Console()

URL = "https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9_%D1%83%D0%BD%D0%B8%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D1%82%D0%B5%D1%82"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "lxml")
body = soup.find("div", class_="mw-parser-output")


header_tag = soup.find("h1", class_="firstHeading")

for tag in body.find_all("table", class_="infobox"):
    tag.decompose()

for tag in body.find_all("div", class_="navbox"):
    tag.decompose()

for tag in body.find_all("table", class_="sidebar"):
    tag.decompose()

for tag in body.find_all("table", class_="metadata"):
    tag.decompose()

for tag in body.find_all("div", class_="metadata"):
    tag.decompose()

for tag in body.find_all("style"):
    tag.decompose()

for tag in body.find_all("span", class_="mw-editsection"):
    tag.decompose()

for tag in body.find_all("span", class_="mw-cite-backlink"):
    tag.decompose()

for tag in body.find_all("a"):
    tag["href"] = "https://ru.wikipedia.org" + tag["href"]

for tag in body.find_all("sup", class_="reference"):
    tag.string = tag.a.text


final_soup = BeautifulSoup()
final_soup.append(header_tag)
final_soup.append(body)
md = MarkdownConverter().convert_soup(final_soup)

markdown = Markdown(md, style="fruity")


console.print(markdown)

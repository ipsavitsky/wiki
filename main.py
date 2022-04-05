import requests
from bs4 import BeautifulSoup
from markdownify import markdownify
from rich.console import Console
from rich.markdown import Markdown

console = Console()

URL = "https://en.wikipedia.org/wiki/1973_Auburn_Tigers_football_team"
page = requests.get(URL)


soup = BeautifulSoup(page.content, 'lxml')
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

for tag in body.find_all("a"):
    tag["href"] = "https://en.wikipedia.org" + tag["href"]


md = markdownify(header_tag.decode() + body.decode())


markdown = Markdown(md)


console.print(markdown)


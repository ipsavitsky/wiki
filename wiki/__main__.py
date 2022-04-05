import argparse
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from rich.console import Console
from rich.markdown import Markdown
from soup_filters import filter_soup
from wikipedia import NoArticleFound, fetch_wiki_data

console = Console()

parser = argparse.ArgumentParser(description="Search a Wikipedia article and print it")
parser.add_argument("keyword", type=str, help="The keyword to search")
args = parser.parse_args()
# console.print(args)

try:
    page_info = fetch_wiki_data(args.keyword)
except NoArticleFound:
    console.print("No article found")
    exit(1)

soup = BeautifulSoup(page_info["text"]["*"], "lxml")

filtered_soup = filter_soup(page_info["title"], soup)

md = MarkdownConverter().convert_soup(filtered_soup)

markdown = Markdown(md)


console.print(markdown)

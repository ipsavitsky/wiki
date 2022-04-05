from bs4 import BeautifulSoup


def filter_soup(title: str, soup: BeautifulSoup) -> BeautifulSoup:
    body = soup.find("div", class_="mw-parser-output")
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
    header_tag = final_soup.new_tag("h1")
    header_tag.string = title
    final_soup.append(header_tag)
    final_soup.append(body)

    return final_soup

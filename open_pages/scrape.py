from bs4 import BeautifulSoup
from urllib.request import urlopen
from usp.tree import sitemap_tree_for_homepage
from open_pages.models import Pages

# gets all pages' links of website
tree = sitemap_tree_for_homepage('https://divan24.kz/')

# parses each page with loop
for page in tree.all_pages():
    url = page.url
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.string

    # saves new page in db
    new_page = Pages(url=url, title=title, html=html)
    new_page.save()

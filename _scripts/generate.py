from pywikibot.pagegenerators import CategorizedPageGenerator
from pywikibot import Site, Category
import json

site = Site('commons', 'commons')
cat = Category(site, 'Category:Images_from_Nordiska_museet:_2019-06')

pages = list()
for page in CategorizedPageGenerator(cat, recurse=False, namespaces=6):
    item = {}
    item['id'] = page.pageid
    print(page.title())
    item['title'] = str(page.title())
    if (('(2)' in item['title']) or ('(3)' in item['title'])):
        continue
    pages.append(item)

    with open('../static/pages.json', 'w') as outfile:
        json.dump(pages, outfile, ensure_ascii=False)

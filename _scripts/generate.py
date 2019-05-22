from pywikibot.pagegenerators import CategorizedPageGenerator
from pywikibot import Site, Category
import json

site = Site('commons', 'commons')
cat = Category(site, 'Category:Images_from_Nordiska_museet/Fashion_plates')

pages = list()
for page in CategorizedPageGenerator(cat, recurse=False, namespaces=6):
    pages.append(page.pageid)

    with open('../static/pages.json', 'w') as outfile:
        json.dump(pages, outfile)

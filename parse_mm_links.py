import requests
from bs4 import BeautifulSoup


def get_product(page_link):
    r = requests.get(page_link)
    soup = BeautifulSoup(r.text, 'html.parser')
    prod_set = set()
    prod_list = soup.find_all(class_='content')

    for prod in prod_list:
        try:
            link = prod.find('a').get('href')
            if "product" in link.split('/'):
                prod_set.add(str(link))
        except:
            continue
    return prod_set


all_prod = set()
p = 0

with open('mediamarkt_links.txt', 'r') as f:
    data = f.read().splitlines()
    for line in data:
        print(f'processing {line}')
        found = list(get_product(line))
        for f in found:
            all_prod.add(f)
            p += len(all_prod)
        print(f'found {len(found)} product links - total {p}')

products_list = list(all_prod)

with open('mmarkt_products.txt','w') as f:
    for product in products_list:
        f.write(product)

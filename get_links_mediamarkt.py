from requests_html import HTMLSession
from time import sleep


def get_cat_links(link, keyword='category'):
    session = HTMLSession()
    r = session.get(link)
    links = r.html.absolute_links
    start_links = set()
    for l in links:
        if keyword in l.split('/'):
            start_links.add(l)
            # print(f'{l} added')
    session.close()
    print(f'Retrieved {len(start_links)} links')
    return start_links


all_links = set()
entry = 'https://www.mediamarkt.hu/hu/category/_laptop-notebook-504819.html'

start_set = get_cat_links(entry)
r=len(start_set)
print(f'{r=}')
d=0
for s in start_set:                 #trying to loop through the first set to get additional new links
    new_set = get_cat_links(s)
    print(f'parsing {s}')
    for l in list(new_set):              #tyring to get the individual items of the set and add them to the big set
        all_links.add(l)
        i = len(all_links)
    d+=1
    print(f'{s} done... Total links gathered: {i}')
    print(f'remaining: {r-d}')
    sleep(1)
    if d==10: break

with open('mediamarkt_links.txt', 'w') as f:
    for l in list(all_links):
        f.write(l+'\n')
    print(f'{f=} has been written')

import requests
from bs4 import BeautifulSoup
import csv

def create_prod_line(prod_url):
    BASEURL = 'https://www.mediamarkt.hu'
    url = BASEURL + prod_url
    r = requests.get(url)
    print(f'status_code: {r.status_code}')
    if r.status_code in range(200, 299):
        soup = BeautifulSoup(r.text, 'html.parser')

    # parsing the product details
    item_name = soup.find('h1').text
    details = soup.find(class_='product-details').get_text().split('\n')
    key = ['Name']
    value = [item_name]
    # for v, i in enumerate(details[1:-1]):
    #     if v % 2 == 0:
    #         key.append(i.rstrip(':'))
    #     else:
    #         value.append(i)

    #Parsing the price details
    price_soup = soup.find(class_='price-sidebar')
    price=price_soup.find_all('meta')
    plist=list(price)
    pkey=[]
    pvalue=[]
    for p in plist:
        pvalue.append(str(p).split('"')[1].strip())
        pkey.append(str(p).split('"')[3].strip())

    product_to_table = dict(zip(key + pkey, value + pvalue))

    return product_to_table


with open('mmarkt_products.txt','r') as f:
    urls=f.read().splitlines()
    temp=[]
    c_url=0
    for url in urls:
        try:
            temp.append(create_prod_line(url))
            c_url+=1
            print(f'{c_url} products added to parse')
            if c_url>50:
                break
        except: continue


with open('mmarkt.csv','w',newline='') as f:
    c_line=0
    writer=csv.DictWriter(f,fieldnames=temp[0].keys())
    writer.writeheader()
    for t in temp:
        writer.writerow(t)
        c_line+=1
    print(f'{c_line} products added to the csv')
print(f'file saved')


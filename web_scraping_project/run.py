from os import system, environ, path, getuid, popen, listdir
from base64 import b64encode, b64decode
from bs4 import BeautifulSoup
from datetime import datetime
import codecs
import textwrap
import time
import sys
import requests
import subprocess
import re
import requests
import json
import math 
import glob
import openpyxl
import os

all_link_list=[]
id_form_all_link=[]
all_link_id_to_file=[]

def page_load(id_e,s_id):
    cookies = {
        '_gcl_au': '1.1.100277934.1624187046',
        '_ga_L36G369N3Y': 'GS1.1.1624552005.5.1.1624552046.0',
        '_ga': 'GA1.2.1643807057.1624187050',
        '_clck': '18p5h3s',
        '_fbp': 'fb.1.1624187056775.1203105405',
        '_gid': 'GA1.2.551853972.1624513089',
        '_clsk': '183q05h|1624552048302|3|1|eus/collect',
        '__accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiJiMzY5YjFiMC05YzBjLTRlMmItOWMxYy05M2YxYjI0MzRlMTQiLCJ0cyI6IjIwMjEtMDYtMjQgMTY6MjY6NDIiLCJpc19ndWVzdCI6dHJ1ZX0.dEVRSceYGN7vrUtRTjoQYGJcuOUeyHAy_dEZBqVeD0Y',
        '_gat_UA-192850196-1': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://shop.moreretail.in/?store=1191',
        'Upgrade-Insecure-Requests': '1',
        'TE': 'Trailers',
    }

    params = (
        ('id', f'{id_e}'),
        ('s_id', f'{s_id}'),
        ('store', '1191'),
    )

    return requests.get('https://shop.moreretail.in/product-listing', headers=headers, params=params, cookies=cookies)

def main_page_html():
    cookies = {
        '_fbp': 'fb.1.1623586032495.523310413',
        '_gcl_au': '1.1.898392279.1623586033',
        '_ga_L36G369N3Y': 'GS1.1.1624513071.11.1.1624513179.0',
        '_ga': 'GA1.1.1232709110.1623586033',
        '__accessToken': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiIwN2NkODcwNS0yNWIzLTRmNTYtYWYxNC1mMjIxM2FkZDIxN2MiLCJ0cyI6IjIwMjEtMDYtMjQgMDU6Mzc6NTEiLCJpc19ndWVzdCI6dHJ1ZX0.HrNQ9LrvPwU0EYt6ynDbDc_gEqzM0l_lwE3JNKkI3ZE',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Sec-GPC': '1',
        'Cache-Control': 'max-age=0',
    }

    params = (
        ('store', '1191'),
    )
    f=open("bin/main_page.html", "w+")
    f.write(f"");f.close()
    f=open("all_link/link", "w+")
    f.write(f"");f.close()
    response = requests.get('https://shop.moreretail.in/', headers=headers, params=params, cookies=cookies)
    soup=BeautifulSoup(response.text,'html.parser')
    for first_link in soup.find_all("section", class_="home_categories__2RYMC"):
        f=open("bin/main_page.html", "a")
        f.write(f"{first_link}")
        f.close()
        for link in first_link.find_all("a", class_="grid-listing_cardanchor__2lp3i"):
            id_form_all_link.append(link.get("href").replace("./product-listing","https://shop.moreretail.in/product-listing").split("&")[1].split("=")[1])
            all_link_list.append(link.get("href").replace("./product-listing","https://shop.moreretail.in/product-listing"))
    
    with open('all_link/link_id', 'w+') as f:
        for item in id_form_all_link:
            f.write("%s\n" % item)

    with open('all_link/link', 'w+') as f:
        for item in all_link_list:
            f.write("%s\n" % item)
    

def requests_to_api(id,skip_number):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://shop.moreretail.in/',
        'Content-Type': 'application/json',
        'x-access-token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI3YzkwMjNmMC05OTUxLTQxNTMtYjgyZi1lNWI5Nzc2MmI3ZGQiLCJ0cyI6IjIwMjEtMDYtMTMgMTI6MDc6MTAiLCJpc19ndWVzdCI6dHJ1ZX0.k8jVYKuGPwVNqAUZs3AguUtncjYRKsiMATpOEzFrvmU',
        'Origin': 'https://shop.moreretail.in',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Sec-GPC': '1',
    }

    params = (
        ('sub_category_id', f'{id}'), #b3ff2d3c-5ac5-4710-ba0c-3d2cb3ded469
        ('skip', f'{skip_number}'), #125
    )

    return requests.get('https://more-app-backend-uat.moreretail.in/web_app/api/v1/product_list', headers=headers, params=params)

def extract_link(all_link_list):
    print(f"\n\n\t\t\tExtracting Sub-menu Link\n")
    for x in all_link_list:
        print(f"URL : {x}")
        html=page_load((x.split("&")[0].split("=")[1]), (x.split("&")[1].split("=")[1]))
        soup=BeautifulSoup(html.text,'html.parser')
        for first_link in soup.find_all("script", {"id": "__NEXT_DATA__"}):
            json_dumps=(str(str(first_link).split(">")[1].split("<")[0]))
            content = json.loads(json_dumps)
            for product in content['props']['pageProps']['subcategories']:
                print(f"\t\t{product['_id']}")
                id_form_all_link.append(product['_id'])
        time.sleep(1)
    [all_link_id_to_file.append(x) for x in id_form_all_link if x not in all_link_id_to_file]
    with open('all_link/link_id', 'w+') as f:
        for item in list(filter(None,sorted(all_link_id_to_file))):
            f.write("%s\n" % item)



def get_json():
    row = 2
    excel = openpyxl.load_workbook('output.xlsx')
    sheet = excel['Sheet1']
    path = "bin/item/*.json"
    sheet['A1'] = 'Category'
    sheet['B1'] = 'Sub-Category'
    sheet['C1'] = 'Product-Name'
    sheet['D1'] = 'Quantity '
    sheet['E1'] = 'Original_Price'
    sheet['F1'] = 'Discount_Offer'
    sheet['G1'] = 'M.R.P'
    sheet['H1'] = 'Images'
    for idx, file in enumerate(glob.glob(path)):
        print(idx, file)
        file = open(file,)
        content = json.load(file)
        for product in content['content']['product_list']:
            for prices in product['units']:
                name = prices['name']
                price = math.floor(float(prices['price']))
                mrp = math.floor(float(prices['special_price']))
                discount = prices['discount']
                units = prices['units']
                category = prices['category_name']
                sub_category = prices['sub_category_name']
                images = prices['product_listing_images']
                sheet[f'A{row}'] = category
                sheet[f'B{row}'] = sub_category
                sheet[f'C{row}'] = name
                sheet[f'D{row}'] = units
                sheet[f'E{row}'] = price
                sheet[f'F{row}'] = discount
                if mrp:
                    sheet[f'G{row}'] = mrp
                if images:
                    sheet[f'H{row}'] = f"""=HYPERLINK(CONCATENATE("{images[0]}"),"Click Here")"""
                row += 1
    excel.save('output.xlsx')
    return

# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+ MAIN =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
# +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+= #
system("sudo rm -rf bin/")
os.makedirs("bin/item/new")

main_page_html()
extract_link(all_link_list)

all_link_list=list(filter(None,sorted(all_link_list)))
all_link_id_to_file=list(filter(None,sorted(all_link_id_to_file)))

system("clear")

for z in all_link_id_to_file:
    print("+"*70)
    time.sleep(1.5)
    for x in range(0, 501, 20):
        print(f"\t{z} : {x}")
        json_dump=(requests_to_api(z, x).text)
        if len(json_dump) <= 200:
            print("\n\t\t\t\t(DEAD)")
            break
        else:
            print("\t(LIVE)")
            o=open(f"bin/item/{z}_{x}.json", "w+")
            o.write(f"{json_dump}")
            o.close()
            system(f"cat bin/item/{z}_{x}.json | jq | tee bin/item/new/{z}_{x}.json > /dev/null 2>&1")

system("sudo rm -rf output.xlsx; cp all_link/new.xlsx output.xlsx")
get_json()

os.rename('output.xlsx',f"More_{datetime.today().strftime('%d-%m-%Y')}.xlsx")


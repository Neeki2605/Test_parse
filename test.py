import json
import pandas as pd
import openpyxl
import requests
import selenium
import undetected_chromedriver
import time
import sys
import os
from twocaptcha import TwoCaptcha
import asyncio
import aiohttp
# lst = [1, 2, 3]
# lst2 = [[111, 21, 321], [1, 2, 3], [22, 41, 55], [65, 73, 95]]
#
# data = pd.DataFrame(lst2, index=range(len(lst2)), columns=["Модель", "Магазин", "Цена"])
# print(data)
# #data.to_excel("example.xlsx", sheet_name='new_sheet_name')

#
# headers = {
#         'Content-Type': 'application/json',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept': '*/*',
#         'Cookie': 'session=.eJwdzMENwyAMAMBd_M4DDDE4y0TGBolHSUVpP1V2r9Qb4L4gY_VyrbMbHCAWq3BL4o0lNkvJrCWHEUNplJk4UVbnduUgXp0iB_VU0KK2PSJs8Omvvq75_wIR5uw2OJ91PmTUseBY813vH4tSJH0.ZCFhYQ.-DYjO-rSUdnSnh3qbE4WseNILaA; _gcl_au=1.1.668395072.1679909218; _gid=GA1.2.572824044.1680438754; _gat_gtag_UA_165338650_1=1; _ga=GA1.1.1162573884.1679909217; _ga_ZK01SYQ8J9=GS1.1.1680523723.23.0.1680523723.0.0.0'
#     }
# url = "https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/category/smartfony.json?inStock=true&slug=smartfony"
#

# with open("jsonformatter.json", encoding="utf-8") as file:
#     req = json.load(file)
# req = requests.get(url)
# print(req.status_code)
# print(req.json())
# topOffers = req["pageProps"]["topOffers"]
# print(topOffers)
# mobile_data = []
# for offer in topOffers:
#     mobile_data.append({
#         "name": offer["name"],
#         "merchant_name": offer["merchantName"],
#         "price": offer["price"]
#         })
# print(mobile_data)
#
#
# req = requests.get(url, headers=headers)
# response = req.json()
# print(response)

mobile_list = []

async def get_page_data(session, page):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Cookie': 'session=.eJwdzMENwyAMAMBd_M4DDDE4y0TGBolHSUVpP1V2r9Qb4L4gY_VyrbMbHCAWq3BL4o0lNkvJrCWHEUNplJk4UVbnduUgXp0iB_VU0KK2PSJs8Omvvq75_wIR5uw2OJ91PmTUseBY813vH4tSJH0.ZCFhYQ.-DYjO-rSUdnSnh3qbE4WseNILaA; _gcl_au=1.1.668395072.1679909218; _gid=GA1.2.2027630605.1680972371; _ga=GA1.2.1162573884.1679909217; _gat_gtag_UA_165338650_1=1; _ga_ZK01SYQ8J9=GS1.1.1680981238.26.1.1680984741.0.0.0'
    }

    url = f"https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/category/smartfony.json?inStock=true&slug=smartfony&page={page}"

    async with session.get(url=url, headers=headers) as response:
        response = await response.json()

        mobile_dict = response["pageProps"]["results"]
        mobile_urls = []
        for mobile in mobile_dict:
            mobile_urls.append("https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/product/" + mobile["slug"] + ".json?slug=" + mobile["slug"])

        for url in mobile_urls:
            response = getData(url)
            top_offers = response["pageProps"]["topOffers"]

            mobile_data = []
            for offer in top_offers:
                mobile_data.append({
                    "name": offer["name"],
                    "merchant_name": offer["merchantName"],
                    "price": offer["price"]
                })
            for val in mobile_data:
                mobile_list.append(val.values())

async def gather_data():
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Cookie': 'session=.eJwdzMENwyAMAMBd_M4DDDE4y0TGBolHSUVpP1V2r9Qb4L4gY_VyrbMbHCAWq3BL4o0lNkvJrCWHEUNplJk4UVbnduUgXp0iB_VU0KK2PSJs8Omvvq75_wIR5uw2OJ91PmTUseBY813vH4tSJH0.ZCFhYQ.-DYjO-rSUdnSnh3qbE4WseNILaA; _gcl_au=1.1.668395072.1679909218; _gid=GA1.2.2027630605.1680972371; _ga=GA1.2.1162573884.1679909217; _gat_gtag_UA_165338650_1=1; _ga_ZK01SYQ8J9=GS1.1.1680981238.26.1.1680984741.0.0.0'
    }

    url = "https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/category/smartfony.json?inStock=true&slug" \
        "=smartfony"
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        total_pages = response["pageProps"]["pagination"]["totalPages"]

        tasks = []

        for page in range(1, total_pages + 1):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)

            await asyncio.gather(*tasks)



def main():
    pass


if __name__ == "__main__":
    main()
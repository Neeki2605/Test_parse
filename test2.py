import json
import pandas as pd
import openpyxl
import requests
# lst = [1, 2, 3]
# lst2 = [[111, 21, 321], [1, 2, 3], [22, 41, 55], [65, 73, 95]]
#
# data = pd.DataFrame(lst2, index=range(len(lst2)), columns=["Модель", "Магазин", "Цена"])
# print(data)
# #data.to_excel("example.xlsx", sheet_name='new_sheet_name')


headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
    }

url = "https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/category/smartfony.json?inStock=true&slug=smartfony"
#

# with open("jsonformatter.json", encoding="utf-8") as file:
#     req = json.load(file)
req = requests.get(url)
print(req.status_code)
print(req.json())
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

# def getData(url):
#     headers = {
#         'Content-Type': 'application/json',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept': '*/*',
#     }
#     req = requests.get(url, headers)
#     response = req.json()
#     return response
#
# print(getData(url))
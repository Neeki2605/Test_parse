import requests
import pandas as pd

def getData(url):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Cookie': 'session=.eJwdzMENwyAMAMBd_M4DDDE4y0TGBolHSUVpP1V2r9Qb4L4gY_VyrbMbHCAWq3BL4o0lNkvJrCWHEUNplJk4UVbnduUgXp0iB_VU0KK2PSJs8Omvvq75_wIR5uw2OJ91PmTUseBY813vH4tSJH0.ZCFhYQ.-DYjO-rSUdnSnh3qbE4WseNILaA; _gcl_au=1.1.668395072.1679909218; _gid=GA1.2.2027630605.1680972371; _ga=GA1.2.1162573884.1679909217; _gat_gtag_UA_165338650_1=1; _ga_ZK01SYQ8J9=GS1.1.1680981238.26.1.1680984741.0.0.0'
    }
    req = requests.get(url, headers=headers)
    response = req.json()
    return response

src = "https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/category/smartfony.json?inStock=true&slug=smartfony"

response = getData(src)
#print(type(response))
#print(response.status_code)
#print(response)

mobile_list = []
total_pages = response["pageProps"]["pagination"]["totalPages"]
for i in range(1, total_pages + 1):
    url = f"https://www.kattabozor.uz/_next/data/mUUfUiY5GGDWtJ3zDkHf4/ru/category/smartfony.json?inStock=true&slug=smartfony&page={i}"
    response = getData(url)
    print(f"Номер страницы: {i}")
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

data = pd.DataFrame(mobile_list, index=range(1, len(mobile_list) + 1), columns=["Модель", "Магазин", "Цена"])
data.to_excel("example.xlsx")

import requests
import json
import time

WEBHOOK_URL = ''  

def send_to_discord(oy_oranlari, oy_sayilari):
    message = "Oy Oranları:\n"
    for oy_orani in oy_oranlari:
        message += f"{oy_orani['Adi']}: {oy_orani['ITOyOrani']}%\n"
    message += "\nOy Sayıları:\n"
    for oy_sayisi in oy_sayilari:
        message += f"{oy_sayisi['Adi']}: {oy_sayisi['ITOyAdedi']}\n"

    payload = {
        'content': message
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        print("Veriler Discord'a gönderildi.")
    else:
        print(f"Hata oluştu. İstek durumu: {response.status_code}")

def get_json_data():
    headers = {
        'authority': 'scdn.ankahaber.net',
        'accept': 'application/json',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,pt;q=0.6',
        'origin': 'https://secim.ankahaber.net/',
        'referer': 'https://secim.ankahaber.net/',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'accept-encoding': 'gzip',
    }

    response = requests.get('https://scdn.ankahaber.net/secimsonuc/site/ikincitur/web/cb-overview.json?v=1685289079494%27', headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print(f"Hata oluştu. İstek durumu: {response.status_code}")
        return None

def main():
    last_data = None
    while True:
        json_data = get_json_data()
        if json_data is not None and json_data != last_data:
            oy_oranlari = json_data['Sonuclar']
            oy_sayilari = json_data['Sonuclar']
            send_to_discord(oy_oranlari, oy_sayilari)
            last_data = json_data
        time.sleep(5) 

main()

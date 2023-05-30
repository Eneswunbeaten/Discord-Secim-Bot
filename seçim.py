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

    response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if response.status_code == 204:
        print("Veriler Discord'a gönderildi.")
    else:
        print(f"Hata oluştu. İstek durumu: {response.status_code}")

def get_json_data():
    response = requests.get('http://localhost/secim.php')
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
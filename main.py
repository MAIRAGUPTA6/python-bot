import requests
import random
import time
import os,sys

os.system("pip install requests")

def bin_checker(bin_number):
    api_url = f"https://lookup.binlist.net/{bin_number}"
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            country_name = data.get('country', {}).get('name')
            bank_name = data.get('bank', {}).get('name')
            
            if country_name == 'Bahrain' and bank_name == 'CAJA RURAL PROVINCIAL DE ALMERIA':
                return "SUCCESS", country_name, bank_name
            else:
                return "FAILED", country_name, bank_name
        else:
            return "API ERROR", None, None
    except requests.RequestException as e:
        return f"Failed - Error: {e}", None, None

if __name__ == "__main__":
    print("Example:\n Visa: 4\n Mastercard: 5 \n Amex: 3 \n Discovery: 6")

    bin_frist_digit = "4"
    
    
    
    print("***************Bin Checking**************")

    for _ in range(2000000000000):
        time.sleep(4) 
        bin = str(random.randint(11111, 99999))
        bin_number = bin_frist_digit+bin
        result, country_name, bank_name = bin_checker(bin_number)
        p = f"{result}: {bin_number} - Country: {country_name} - Bank: {bank_name}"
        bot_token = "6439214111:AAHyZpeIkmLkynT1J2T4nQwvuo7Iu5zUGQo"
        id = 815121690
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&text={p}")

        print(p)
        if result == "SUCCESS":
            print("Done")
            
            

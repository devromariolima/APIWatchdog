import requests
import time

# Configurações
TELEGRAM_BOT_TOKEN = ''
CHAT_ID = '-'
API_URLS = []
CHECK_INTERVAL = 60  

def check_api(url):
    try:
        response = requests.get(url, timeout=10)  
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return False

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    try:
        requests.post(url, data=payload)
    except requests.RequestException as e:
        print(f"Erro ao enviar mensagem para o Telegram: {e}")

def monitor_apis():
    while True:
        for api in API_URLS:
            if not check_api(api):
                send_telegram_message(f"⚠️ A API {api} está fora do ar ou respondendo com erro!")
            else:
                print(f"A API {api} está funcionando corretamente.")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_apis()

# executar o Script
# python3 APIWatchdog.py

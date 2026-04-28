import psutil
import requests
import time
import datetime

from config import TOKEN, CHAT_ID

def enviar_alerta_telegram(missatge):
    """Envia un missatge a Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={missatge}"
    try:
        requests.get(url)
    except Exception as e:
        print(f"Error enviant alerta a Telegram: {e}")

def monitoritzar_sistema():
    """Analitza recursos i envia alerta si els valors són crítics."""
    
    # 1. Obtenir dades
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    # 2. Lògica d'alerta
    alertes = []
    if cpu_usage > 90:
        alertes.append(f" ALERTA CPU: {cpu_usage}%")
    if ram_usage > 90: 
        alertes.append(f" ALERTA RAM: {ram_usage}%")
    
    # 3. Processar alertes
    if alertes:
        missatge_final = f" {datetime.datetime.now().strftime('%H:%M:%S')}\n" + "\n".join(alertes)
        enviar_alerta_telegram(missatge_final)
        print(f"Alerta enviada: {missatge_final}")
    else:
        print(f"Sistema OK. CPU: {cpu_usage}%, RAM: {ram_usage}%")

if __name__ == "__main__":
    print("Iniciant SentryBot... (Ctrl+C per aturar)")
    try:
        while True:
            monitoritzar_sistema()
            # Espera 5 minuts abans de la següent revisió
            time.sleep(300) 
    except KeyboardInterrupt:
        print("\nSentryBot aturat.")
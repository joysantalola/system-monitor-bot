import psutil
import requests
import time
import datetime
import os  # Necessari per gestionar fitxers

from config import TOKEN, CHAT_ID

# --- CONFIGURACIÓ DE LOGS ---
LOG_FILE = "sistem-monitor_log.txt"

def registrar_log(missatge):
    """Escriu el missatge en un fitxer de text amb la data actual."""
    marca_temps = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, "a") as f:
        f.write(f"[{marca_temps}] {missatge}\n")

def enviar_alerta_telegram(missatge):
    """Envia un missatge a Telegram i registra l'intent al log."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={missatge}"
    try:
        requests.get(url)
        registrar_log(f"ALERTA ENVIADA A TELEGRAM: {missatge.replace(chr(10), ' ')}")
    except Exception as e:
        registrar_log(f"ERROR enviant alerta a Telegram: {e}")

def monitoritzar_sistema():
    """Analitza recursos i envia alerta si els valors són crítics."""
    
    # 1. Obtenir dades
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    # 2. Lògica d'alerta
    alertes = []
    if cpu_usage > 90:
        alertes.append(f"ALERTA CPU: {cpu_usage}%")
    if ram_usage > 90: 
        alertes.append(f"ALERTA RAM: {ram_usage}%")
    
    # 3. Processar alertes
    if alertes:
        missatge_final = f"{datetime.datetime.now().strftime('%H:%M:%S')} - " + ", ".join(alertes)
        enviar_alerta_telegram(missatge_final)
        print(f"Alerta enviada: {missatge_final}")
    else:
        print(f"Sistema OK. CPU: {cpu_usage}%, RAM: {ram_usage}%")

if __name__ == "__main__":
    registrar_log("sistem-monitorBot iniciat.") # Log d'inici
    print("Iniciant sistem-monitorBot... (Ctrl+C per aturar)")
    try:
        while True:
            monitoritzar_sistema()
            time.sleep(300) 
    except KeyboardInterrupt:
        registrar_log("sistem-monitorBot aturat manualment.") # Log d'aturada
        print("\nsistem-monitorBot aturat.")
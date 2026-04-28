import psutil
import requests
import time
import datetime
import os

from config import TOKEN, CHAT_ID

def obtenir_nom_log():
    """Genera el nom del fitxer basat en la data d'avui."""
    data_avui = datetime.datetime.now().strftime('%Y-%m-%d')
    return f"system-monitor_{data_avui}.log"

def registrar_log(missatge):
    """Escriu el log en un fitxer diari."""
    nom_fitxer = obtenir_nom_log()
    marca_temps = datetime.datetime.now().strftime('%H:%M:%S')
    with open(nom_fitxer, "a") as f:
        f.write(f"[{marca_temps}] {missatge}\n")

def enviar_alerta_telegram(missatge):
    """Envia alerta a Telegram."""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={missatge}"
    try:
        requests.get(url)
        registrar_log(f"ALERTA TELEGRAM: {missatge.replace(chr(10), ' ')}")
    except Exception as e:
        registrar_log(f"ERROR TELEGRAM: {e}")

def monitoritzar_sistema():
    """Analitza recursos, registra heartbeat i avisa si cal."""
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    
    # 1. Heartbeat: Registrem sempre el consum al log cada 5 minuts
    registrar_log(f"HEARTBEAT - CPU: {cpu_usage}% | RAM: {ram_usage}%")
    
    # 2. Lògica d'alerta
    alertes = []
    if cpu_usage > 90:
        alertes.append(f"CPU: {cpu_usage}%")
    if ram_usage > 90: 
        alertes.append(f"RAM: {ram_usage}%")
    
    if alertes:
        missatge_final = f"ALERTA! {', '.join(alertes)}"
        enviar_alerta_telegram(missatge_final)
        print(f"Alerta enviada: {missatge_final}")
    else:
        print(f"Sistema OK. CPU: {cpu_usage}%, RAM: {ram_usage}%")

if __name__ == "__main__":
    print("Iniciant system-monitor-bot... (Ctrl+C per aturar)")
    registrar_log("Inici del bot.")
    try:
        while True:
            monitoritzar_sistema()
            # El sleep ja el tenies a 300 segons (5 minuts)
            time.sleep(300) 
    except KeyboardInterrupt:
        registrar_log("Bot aturat per l'usuari.")
        print("\nSystem-Monitor Bot aturat.")
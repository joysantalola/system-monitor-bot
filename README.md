# System Monitor Bot

Eina d'automatització en Python per a la monitorització de recursos del sistema (CPU i RAM) amb notificacions d'alerta en temps real via Telegram.

## Funcionalitats
* **Monitorització en temps real:** Comprova l'estat de la CPU i la RAM del sistema.
* **Alertes intel·ligents:** Envia notificacions immediates a Telegram quan els recursos superen un llindar crític (90%).
* **Estructura professional:** Dissenyat amb bona gestió de dependències i seguretat.

## Requisits
* Python 3.x
* Llibreries: `psutil`, `requests`

Instal·la les dependències necessàries:
```bash
pip install psutil requests
```

## Configuració
Perquè el bot funcioni, necessites crear un fitxer anomenat `config.py` a l'arrel del projecte amb les següents dades:

```python
# config.py
TOKEN = "EL_TEU_TOKEN_AQUI"
CHAT_ID = "EL_TEU_ID_AQUI"
```

*Obtén el teu token mitjançant [@BotFather](https://t.me/botfather) a Telegram.*

## Ús
Executa l'script des de la teva terminal:
```bash
python alertes_telegram.py
```

## Autor
Desenvolupat per **Oleguer Esteo** com a eina d'administració de sistemes i automatització IT.

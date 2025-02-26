# main.py
from device_info import get_local_device_info, parse_user_agent

# Informazioni dispositivo locale
print("Info dispositivo locale:", get_local_device_info())

# Esempio di analisi User-Agent senza framework web
user_agent_test = "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
print("Tipo dispositivo da User-Agent test:", parse_user_agent(user_agent_test))
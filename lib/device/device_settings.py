from lib.logger.logger import log
import subprocess
from lib.exceptions.exceptions import handle_exception, CustomException

def menu_impostazioni_dispositivo():
    while True:
        print("\n=== IMPOSTAZIONI DISPOSITIVO ===")
        print("1. Abilita/disabilita Wi-Fi")
        print("2. Abilita/disabilita Bluetooth")
        print("3. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            toggle_wifi()
        elif scelta == "2":
            toggle_bluetooth()
        elif scelta == "3":
            break
        else:
            print("Opzione non valida! Riprova.")

def toggle_wifi():
    try:
        stato_wifi = subprocess.check_output("svc wifi state", shell=True).strip()
        if stato_wifi == b'Wi-Fi is enabled':
            subprocess.run("svc wifi disable", shell=True)
            log("Wi-Fi disabilitato.", level="INFO")
        else:
            subprocess.run("svc wifi enable", shell=True)
            log("Wi-Fi abilitato.", level="INFO")
    except subprocess.CalledProcessError as e:
        handle_exception(CustomException(f"Errore durante la modifica dello stato del Wi-Fi: {e}"))

def toggle_bluetooth():
    try:
        stato_bluetooth = subprocess.check_output("svc bluetooth state", shell=True).strip()
        if stato_bluetooth == b'Bluetooth is enabled':
            subprocess.run("svc bluetooth disable", shell=True)
            log("Bluetooth disabilitato.", level="INFO")
        else:
            subprocess.run("svc bluetooth enable", shell=True)
            log("Bluetooth abilitato.", level="INFO")
    except subprocess.CalledProcessError as e:
        handle_exception(CustomException(f"Errore durante la modifica dello stato del Bluetooth: {e}"))
from logger import log
import subprocess

def menu_impostazioni_dispositivo():
    """
    Mostra un menu per le impostazioni del dispositivo.
    """
    while True:
        print("\n=== IMPOSTAZIONI DISPOSITIVO ===")
        print("1. Abilita/disabilita Wi-Fi")
        print("2. Abilita/disabilita Bluetooth")
        print("3. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

       
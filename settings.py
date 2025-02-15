import json
import os
from logger import log  # Importa la funzione di logging

def load_settings():
    """
    Carica le impostazioni da un file JSON.
    """
    settings_file = "settings.json"
    default_settings = {
        "clear_call_log": True,
        "secure_delete": True,
        "apps_to_clear": {
            "whatsapp": True,
            "telegram": True,
            "signal": True,
            "facebook_messenger": True,
            "viber": True
        }
    }

    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r") as f:
                return json.load(f)
        except Exception as e:
            log(f"❌ Errore durante il caricamento delle impostazioni: {e}", level="ERROR")
            return default_settings
    else:
        with open(settings_file, "w") as f:
            json.dump(default_settings, f, indent=4)
        return default_settings

def menu_impostazioni():
    """
    Mostra un menu per modificare le impostazioni.
    """
    settings = load_settings()
    while True:
        print("\n=== IMPOSTAZIONI ===")
        print("1. Cancella cronologia chiamate: " + ("✅" if settings["clear_call_log"] else "❌"))
        print("2. Cancellazione sicura: " + ("✅" if settings["secure_delete"] else "❌"))
        print("3. App da cancellare:")
        for app, enabled in settings["apps_to_clear"].items():
            print(f"   - {app}: " + ("✅" if enabled else "❌"))
        print("4. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            settings["clear_call_log"] = not settings["clear_call_log"]
        elif scelta == "2":
            settings["secure_delete"] = not settings["secure_delete"]
        elif scelta == "3":
            for app in settings["apps_to_clear"]:
                settings["apps_to_clear"][app] = not settings["apps_to_clear"][app]
        elif scelta == "4":
            break
        else:
            print("Opzione non valida! Riprova.")

    # Salva le impostazioni modificate
    with open("settings.json", "w") as f:
        json.dump(settings, f, indent=4)
    log("Impostazioni aggiornate.", level="INFO")  # Ora funzionerà

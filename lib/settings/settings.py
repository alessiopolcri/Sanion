import json
import os
from lib.logger.logger import log
from lib.exceptions.exceptions import handle_exception

def load_settings():
    settings_file = "settings.json"
    default_settings = {
        "auto_start": False,
        "notifications": True,
        "auto_update": True,
        "theme": "Chiaro",
        "auto_backup": True,
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
        save_settings(default_settings)
        return default_settings

def save_settings(settings):
    settings_file = "settings.json"
    try:
        with open(settings_file, "w") as f:
            json.dump(settings, f, indent=4)
        log("Impostazioni salvate.", level="INFO")
    except Exception as e:
        handle_exception(e)

def menu_impostazioni():
    settings = load_settings()
    while True:
        print("\n=== IMPOSTAZIONI ===")
        print("1. Cancella cronologia chiamate: " + ("✅" if settings["clear_call_log"] else "❌"))
        print("2. Cancellazione sicura: " + ("✅" if settings["secure_delete"] else "❌"))
        print("3. App da cancellare:")
        for app, enabled in settings["apps_to_clear"].items():
            print(f"   - {app}: " + ("✅" if enabled else "❌"))
        print("4. Avvio automatico all'accensione: " + ("✅" if settings["auto_start"] else "❌"))
        print("5. Notifiche: " + ("✅" if settings["notifications"] else "❌"))
        print("6. Aggiornamenti automatici: " + ("✅" if settings["auto_update"] else "❌"))
        print("7. Tema: " + settings["theme"])
        print("8. Backup automatico: " + ("✅" if settings["auto_backup"] else "❌"))
        print("9. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            settings["clear_call_log"] = not settings["clear_call_log"]
        elif scelta == "2":
            settings["secure_delete"] = not settings["secure_delete"]
        elif scelta == "3":
            for app in settings["apps_to_clear"]:
                settings["apps_to_clear"][app] = not settings["apps_to_clear"][app]
        elif scelta == "4":
            toggle_auto_start(settings)
        elif scelta == "5":
            toggle_notifications(settings)
        elif scelta == "6":
            toggle_auto_update(settings)
        elif scelta == "7":
            toggle_theme(settings)
        elif scelta == "8":
            toggle_auto_backup(settings)
        elif scelta == "9":
            break
        else:
            print("Opzione non valida! Riprova.")

        save_settings(settings)
    log("Impostazioni aggiornate.", level="INFO")

def toggle_auto_start(settings):
    try:
        settings["auto_start"] = not settings["auto_start"]
        if settings["auto_start"]:
            enable_auto_start()
        else:
            disable_auto_start()
        log("Avvio automatico all'accensione aggiornato.", level="INFO")
    except Exception as e:
        handle_exception(CustomException(f"Errore durante la modifica dell'avvio automatico: {e}"))

def enable_auto_start():
    # Implementazione specifica per abilitare l'avvio automatico all'accensione
    pass

def disable_auto_start():
    # Implementazione specifica per disabilitare l'avvio automatico all'accensione
    pass

def toggle_notifications(settings):
    try:
        settings["notifications"] = not settings["notifications"]
        log("Notifiche aggiornate.", level="INFO")
    except Exception as e:
        handle_exception(CustomException(f"Errore durante la modifica delle notifiche: {e}"))

def toggle_auto_update(settings):
    try:
        settings["auto_update"] = not settings["auto_update"]
        log("Aggiornamenti automatici aggiornati.", level="INFO")
    except Exception as e:
        handle_exception(CustomException(f"Errore durante la modifica degli aggiornamenti automatici: {e}"))

def toggle_theme(settings):
    try:
        settings["theme"] = "Scuro" if settings["theme"] == "Chiaro" else "Chiaro"
        log("Tema aggiornato.", level="INFO")
    except Exception as e:
        handle_exception(CustomException(f"Errore durante la modifica del tema: {e}"))

def toggle_auto_backup(settings):
    try:
        settings["auto_backup"] = not settings["auto_backup"]
        log("Backup automatico aggiornato.", level="INFO")
    except Exception as e:
        handle_exception(CustomException(f"Errore durante la modifica del backup automatico: {e}"))
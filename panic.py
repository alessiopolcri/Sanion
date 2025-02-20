from logger import log
import os
import sys
from settings import load_settings
import subprocess

def secure_delete(file_path):
    """
    Sovrascrive il file con dati casuali prima di eliminarlo definitivamente.

    Args:
        file_path (str): Il percorso del file da sovrascrivere ed eliminare.
    """
    if os.path.exists(file_path):
        log(f"Sovrascrittura sicura del file: {file_path}", level="INFO")
        try:
            subprocess.run(["dd", "if=/dev/urandom", f"of={file_path}", "bs=4K", "count=10"], check=True)
            os.remove(file_path)
            log(f"✅ File {file_path} eliminato in modo sicuro.", level="SUCCESS")
        except subprocess.CalledProcessError as e:
            log(f"❌ Errore durante la sovrascrittura del file: {e}", level="ERROR")

def panic_button(risultati_analisi):
    """
    Attiva il Panic Button utilizzando i risultati dell'analisi delle app installate.

    Args:
        risultati_analisi (dict): I risultati dell'analisi delle app installate.
    """
    settings = load_settings()

    log("!!! PANIC BUTTON ATTIVATO !!!", level="ALERT")

    try:
        if settings["clear_call_log"]:
            log("Eliminazione della cronologia chiamate...", level="INFO")
            try:
                subprocess.run(["content", "delete", "--uri", "content://call_log/calls"], check=True)
                log("✅ Cronologia chiamate eliminata con successo.", level="SUCCESS")
            except subprocess.CalledProcessError as e:
                log(f"❌ Errore nell'eliminazione della cronologia chiamate: {e}", level="ERROR")

        # Cancella i file delle app di messaggistica trovate
        for app_name, app_info in risultati_analisi.items():
            if app_info.get("installata", False) and settings.get(f"clear_{app_name}", False):
                log(f"Eliminazione file di {app_name}...", level="INFO")
                for file in app_info.get("file_da_cancellare", []):
                    if settings["secure_delete"]:
                        secure_delete(file)
                    else:
                        try:
                            os.remove(file)
                            log(f"✅ File {file} eliminato.", level="SUCCESS")
                        except Exception as e:
                            log(f"❌ Errore durante l'eliminazione di {file}: {e}", level="ERROR")

        log("Chiusura immediata delle operazioni critiche...", level="INFO")
        sys.exit()

    except Exception as e:
        log(f"❌ Errore nell'attivazione del Panic Button: {e}", level="ERROR")

    log("🔒 Sicurezza ripristinata.", level="INFO")
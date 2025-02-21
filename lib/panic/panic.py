from lib.logger.logger import log
import os
import sys
import subprocess
from lib.settings.settings import load_settings
from lib.exceptions.exceptions import handle_exception, SecurityException, FileNotFoundError

def secure_delete(file_path):
    if os.path.exists(file_path):
        log(f"Sovrascrittura sicura del file: {file_path}", level="INFO")
        try:
            subprocess.run(["dd", "if=/dev/urandom", f"of={file_path}", "bs=4K", "count=10"], check=True)
            os.remove(file_path)
            log(f"✅ File {file_path} eliminato in modo sicuro.", level="SUCCESS")
        except subprocess.CalledProcessError as e:
            handle_exception(SecurityException(f"Errore durante la sovrascrittura del file: {e}"))

def panic_button(risultati_analisi):
    settings = load_settings()
    log("!!! PANIC BUTTON ATTIVATO !!!", level="ALERT")
    try:
        if settings["clear_call_log"]:
            log("Eliminazione della cronologia chiamate...", level="INFO")
            try:
                subprocess.run(["content", "delete", "--uri", "content://call_log/calls"], check=True)
                log("✅ Cronologia chiamate eliminata con successo.", level="SUCCESS")
            except subprocess.CalledProcessError as e:
                handle_exception(SecurityException(f"Errore nell'eliminazione della cronologia chiamate: {e}"))
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
                            handle_exception(FileNotFoundError(file))
        log("Chiusura immediata delle operazioni critiche...", level="INFO")
        sys.exit()
    except Exception as e:
        handle_exception(e)
    log("🔒 Sicurezza ripristinata.", level="INFO")
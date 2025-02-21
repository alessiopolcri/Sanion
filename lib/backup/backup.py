import os
import shutil
from lib.logger.logger import log
from lib.exceptions.exceptions import handle_exception, BackupException, RestoreException

def backup_dati(source_dir, backup_dir):
    log(f"Inizio backup dati da {source_dir} a {backup_dir}...", level="INFO")
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        for item in os.listdir(source_dir):
            s = os.path.join(source_dir, item)
            d = os.path.join(backup_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)
        log("Backup completato con successo.", level="SUCCESS")
    except Exception as e:
        handle_exception(BackupException(f"Errore durante il backup dei dati: {e}"))

def ripristina_dati(backup_dir, restore_dir):
    log(f"Inizio ripristino dati da {backup_dir} a {restore_dir}...", level="INFO")
    try:
        if not os.path.exists(restore_dir):
            os.makedirs(restore_dir)
        for item in os.listdir(backup_dir):
            s = os.path.join(backup_dir, item)
            d = os.path.join(restore_dir, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)
        log("Ripristino completato con successo.", level="SUCCESS")
    except Exception as e:
        handle_exception(RestoreException(f"Errore durante il ripristino dei dati: {e}"))
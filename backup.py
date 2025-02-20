import os
import shutil
from logger import log

def backup_dati(source_dir, backup_dir):
    """
    Esegue il backup dei dati dalla directory di origine alla directory di backup.

    Args:
        source_dir (str): La directory di origine dei dati.
        backup_dir (str): La directory di destinazione del backup.
    """
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
        log(f"❌ Errore durante il backup dei dati: {e}", level="ERROR")

def ripristina_dati(backup_dir, restore_dir):
    """
    Ripristina i dati dalla directory di backup alla directory di ripristino.

    Args:
        backup_dir (str): La directory di backup.
        restore_dir (str): La directory di destinazione per il ripristino.
    """
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
        log(f"❌ Errore durante il ripristino dei dati: {e}", level="ERROR")
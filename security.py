import os
import subprocess
from logger import log

def cerca_app_installate():
    """
    Cerca le app installate sul dispositivo utilizzando il comando di sistema `pm list packages`.
    Restituisce un dizionario con i pacchetti trovati.

    Returns:
        dict: Un dizionario con i pacchetti delle app di messaggistica trovate.
    """
    log("Avvio ricerca delle app installate...", level="INFO")
    risultati = {}
    try:
        comando = "pm list packages"
        output = subprocess.check_output(comando, shell=True, text=True)
        pacchetti = [linea.strip().replace("package:", "") for linea in output.splitlines()]
        app_di_messaggistica = {
            "whatsapp": "com.whatsapp",
            "telegram": "org.telegram.messenger",
            "signal": "org.thoughtcrime.securesms",
            "facebook_messenger": "com.facebook.orca",
            "viber": "com.viber.voip"
        }
        for nome_app, pacchetto in app_di_messaggistica.items():
            if pacchetto in pacchetti:
                log(f"Trovata app: {nome_app} ({pacchetto})", level="INFO")
                risultati[nome_app] = {
                    "installata": True,
                    "pacchetto": pacchetto,
                    "percorso": f"/data/data/{pacchetto}",
                    "file_da_cancellare": [
                        f"/data/data/{pacchetto}/databases/msgstore.db",
                        f"/data/data/{pacchetto}/databases/wa.db",
                        f"/data/data/{pacchetto}/cache",
                        f"/data/data/{pacchetto}/files",
                    ]
                }
            else:
                log(f"App non trovata: {nome_app} ({pacchetto})", level="INFO")
                risultati[nome_app] = {"installata": False}
        log("Ricerca delle app installate completata.", level="INFO")
        return risultati
    except subprocess.CalledProcessError as e:
        log(f"❌ Errore durante l'esecuzione del comando di sistema: {e}", level="ERROR")
        return {}

def ricerca_tracce(directory):
    """
    Ricerca tracce in una directory.

    Args:
        directory (str): La directory da analizzare.

    Returns:
        list: Una lista di file trovati.
    """
    log(f"Ricerca tracce nella directory '{directory}'...")
    file_trovati = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', errors='ignore') as f:
                    file_trovati.append(file_path)
            except Exception as e:
                log(f"Errore durante la lettura del file {file_path}: {e}", level="ERROR")
    if file_trovati:
        log(f"Trovati {len(file_trovati)} file.", level="INFO")
        for file in file_trovati:
            print(file)
    else:
        log("Nessun file trovato.", level="INFO")
    return file_trovati

def pulizia_tracce():
    """
    Esegue la pulizia delle tracce.
    """
    log("Avvio pulizia tracce...", level="INFO")
    try:
        file_da_cancellare = ["/sdcard/temp_file1.txt", "/sdcard/temp_file2.log"]
        for file_path in file_da_cancellare:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    log(f"✅ File {file_path} eliminato.", level="SUCCESS")
                except Exception as e:
                    log(f"❌ Errore durante l'eliminazione di {file_path}: {e}", level="ERROR")
            else:
                log(f"File {file_path} non trovato.", level="WARNING")
        log("Pulizia tracce completata.", level="INFO")
    except Exception as e:
        log(f"❌ Errore durante la pulizia delle tracce: {e}", level="ERROR")
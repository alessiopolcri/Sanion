import os
import subprocess
from lib.logger.logger import log
from lib.exceptions.exceptions import handle_exception, FileNotFoundError

def cerca_app_installate():
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
        handle_exception(e)
        return {}

def ricerca_tracce(directory):
    log(f"Ricerca tracce nella directory '{directory}'...")
    file_trovati = []
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', errors='ignore') as f:
                        file_trovati.append(file_path)
                except Exception as e:
                    handle_exception(FileNotFoundError(file_path))
        if file_trovati:
            log(f"Trovati {len(file_trovati)} file.", level="INFO")
        else:
            log("Nessun file trovato.", level="INFO")
        return file_trovati
    except Exception as e:
        handle_exception(e)
        return []

def pulizia_tracce():
    log("Avvio pulizia tracce...", level="INFO")
    try:
        file_da_cancellare = ["/sdcard/temp_file1.txt", "/sdcard/temp_file2.log"]
        for file_path in file_da_cancellare:
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    log(f"✅ File {file_path} eliminato.", level="SUCCESS")
                except Exception as e:
                    handle_exception(FileNotFoundError(file_path))
            else:
                log(f"File {file_path} non trovato.", level="WARNING")
        log("Pulizia tracce completata.", level="INFO")
    except Exception as e:
        handle_exception(e)
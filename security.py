import os
import subprocess
from logger import log
from search import cerca_nome_cognome

def cerca_app_installate():
    """
    Cerca le app installate sul dispositivo utilizzando il comando di sistema `pm list packages`.
    Restituisce un dizionario con i pacchetti trovati.
    """
    log("Avvio ricerca delle app installate...", level="INFO")
    risultati = {}

    try:
        # Esegue il comando per ottenere l'elenco dei pacchetti installati
        comando = "pm list packages"
        output = subprocess.check_output(comando, shell=True, text=True)

        # Elabora l'output per ottenere i nomi dei pacchetti
        pacchetti = [linea.strip().replace("package:", "") for linea in output.splitlines()]

        # Filtra i pacchetti per cercare app di messaggistica
        app_di_messaggistica = {
            "whatsapp": "com.whatsapp",
            "telegram": "org.telegram.messenger",
            "signal": "org.thoughtcrime.securesms",
            "facebook_messenger": "com.facebook.orca",  # Aggiunto Facebook Messenger
            "viber": "com.viber.voip"  # Aggiunto Viber
        }

        for nome_app, pacchetto in app_di_messaggistica.items():
            if pacchetto in pacchetti:
                log(f"Trovata app: {nome_app} ({pacchetto})", level="INFO")
                risultati[nome_app] = {
                    "installata": True,
                    "pacchetto": pacchetto,
                    "percorso": f"/data/data/{pacchetto}",
                    "file_da_cancellare": [
                        f"/data/data/{pacchetto}/databases/msgstore.db",  # WhatsApp
                        f"/data/data/{pacchetto}/databases/wa.db",        # WhatsApp
                        f"/data/data/{pacchetto}/cache",                 # Cache generale
                        f"/data/data/{pacchetto}/files",                 # File multimediali
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

def ricerca_tracce(directory, nome, cognome):
    """
    Ricerca tracce di un nome e cognome in una directory.
    """
    log(f"Ricerca tracce per '{nome} {cognome}' nella directory '{directory}'...")
    file_trovati = cerca_nome_cognome(directory, nome, cognome)
    if file_trovati:
        log(f"Trovati {len(file_trovati)} file.", level="INFO")
        for file in file_trovati:
            print(file)
    else:
        log("Nessun file trovato.", level="INFO")

def pulizia_tracce():
    """
    Esegue la pulizia delle tracce.
    """
    log("Avvio pulizia tracce...", level="INFO")
    
    try:
        # Aggiungi qui la logica per la pulizia delle tracce
        # Esempio: Cancella file temporanei o log
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

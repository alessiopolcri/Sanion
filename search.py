import os
import re
from logger import log
import threading

ESTENSIONI_MULTIMEDIALI = {
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp',  
    '.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a',  
    '.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm',  
    '.pdf', '.zip', '.rar', '.tar', '.gz', '.7z',  
}

def is_file_multimediale(file_path):
    _, estensione = os.path.splitext(file_path)
    return estensione.lower() in ESTENSIONI_MULTIMEDIALI

def cerca_in_file(file_path, pattern):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            contenuto = f.read()
            if pattern.search(contenuto):
                return file_path
    except (PermissionError, IsADirectoryError, UnicodeDecodeError) as e:
        log(f"Errore durante la lettura di {file_path}: {e}", level="WARNING")
    return None

def cerca_nome_cognome(directory, nome, cognome):
    pattern = re.compile(rf'\b{nome}\b.*\b{cognome}\b|\b{cognome}\b.*\b{nome}\b', re.IGNORECASE)
    file_trovati = []
    log(f"Inizio ricerca nella directory: {directory}")

    # Utilizza una cache per evitare di scansionare ripetutamente la stessa directory
    cache = set()

    def worker(root, files):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path in cache:
                continue  # Salta i file già analizzati
            cache.add(file_path)

            if is_file_multimediale(file_path):
                log(f"Ignoro file multimediale: {file_path}", level="DEBUG")
                continue
            risultato = cerca_in_file(file_path, pattern)
            if risultato:
                file_trovati.append(risultato)
                log(f"Trovato in: {risultato}", level="INFO")

    threads = []
    for root, dirs, files in os.walk(directory):
        thread = threading.Thread(target=worker, args=(root, files))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return file_trovati

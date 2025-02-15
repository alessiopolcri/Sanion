from search import cerca_nome_cognome
from logger import log
import time
import os

def ricerca_e_pulizia_tracce():
    print("\n--- Ricerca e Pulizia Tracce ---")
    
    directory_da_cercare = input("Inserisci la directory da cercare: ")
    if not os.path.exists(directory_da_cercare):
        print("❌ Directory non valida!")
        return

    nome = input("Inserisci il nome da cercare: ")
    cognome = input("Inserisci il cognome da cercare: ")
    if not nome or not cognome:
        print("❌ Nome e cognome sono obbligatori!")
        return

    log(f"Cerco '{nome} {cognome}' nella directory '{directory_da_cercare}'...")
    inizio_tempo = time.time()

    file_trovati = cerca_nome_cognome(directory_da_cercare, nome, cognome)

    tempo_impiegato = time.time() - inizio_tempo
    log(f"Ricerca completata in {tempo_impiegato:.2f} secondi.")

    if file_trovati:
        log("\nFile trovati:", level="INFO")
        for file in file_trovati:
            print(file)
        pulizia = input("Vuoi eliminare questi file? (s/n): ")
        if pulizia.lower() == 's':
            for file in file_trovati:
                try:
                    os.remove(file)
                    log(f"File {file} eliminato.", level="INFO")
                except Exception as e:
                    log(f"Errore durante l'eliminazione di {file}: {e}", level="ERROR")
    else:
        log("\nNessun file trovato.", level="INFO")

import os
from panic import panic_button
from security import ricerca_tracce, pulizia_tracce, cerca_app_installate
from settings import menu_impostazioni, load_settings
from logger import log

# Variabile globale per memorizzare i risultati dell'analisi
RISULTATI_ANALISI = None

def menu_principale():
    global RISULTATI_ANALISI

    # Esegui la ricerca delle app installate all'avvio
    RISULTATI_ANALISI = cerca_app_installate()

    while True:
        print("\n=== MENU PRINCIPALE ===")
        print("1. Sicurezza dispositivo")
        print("2. Ricerca e pulizia tracce")
        print("3. 🔴 PANIC BUTTON 🔴 (Numero emergenza)")
        print("4. Impostazioni")
        print("5. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            analizza_sicurezza()
        elif scelta == "2":
            sotto_menu_tracce()
        elif scelta == "3":
            conferma = input("⚠ Sei sicuro di voler attivare il PANIC BUTTON? (s/n): ")
            if conferma.lower() == "s":
                panic_button(RISULTATI_ANALISI)
        elif scelta == "4":
            menu_impostazioni()
        elif scelta == "5":
            log("Uscita dal programma.", level="INFO")
            break
        else:
            print("Opzione non valida! Riprova.")

def sotto_menu_tracce():
    while True:
        print("\n--- RICERCA E PULIZIA TRACCE ---")
        print("1. Ricerca Tracce")
        print("2. Pulizia Tracce")
        print("3. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            directory = input("Inserisci la directory da analizzare: ")
            if not os.path.exists(directory):
                print("❌ Directory non valida!")
                continue
            nome = input("Inserisci il nome: ")
            cognome = input("Inserisci il cognome: ")
            if not nome or not cognome:
                print("❌ Nome e cognome sono obbligatori!")
                continue
            ricerca_tracce(directory, nome, cognome)
        elif scelta == "2":
            conferma = input("⚠ Sei sicuro di voler pulire tutte le tracce? (s/n): ")
            if conferma.lower() == "s":
                pulizia_tracce()
        elif scelta == "3":
            break
        else:
            print("Opzione non valida! Riprova.")

if __name__ == "__main__":
    menu_principale()
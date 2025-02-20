import os
from panic import panic_button
from security import ricerca_tracce, pulizia_tracce, cerca_app_installate
from settings import menu_impostazioni, load_settings
from device_settings import menu_impostazioni_dispositivo
from security_analysis import analizza_sicurezza_app
from backup import backup_dati, ripristina_dati
from real_time_monitoring import monitoraggio_tempo_reale
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
        print("5. Impostazioni dispositivo")
        print("6. Analisi sicurezza app")
        print("7. Backup e ripristino")
        print("8. Monitoraggio in tempo reale")
        print("9. Esci")

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
            menu_impostazioni_dispositivo()
        elif scelta == "6":
            analizza_sicurezza_app_menu()
        elif scelta == "7":
            menu_backup_ripristino()
        elif scelta == "8":
            monitoraggio_tempo_reale()
        elif scelta == "9":
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
            ricerca_tracce(directory)
        elif scelta == "2":
            conferma = input("⚠ Sei sicuro di voler pulire tutte le tracce? (s/n): ")
            if conferma.lower() == "s":
                pulizia_tracce()
        elif scelta == "3":
            break
        else:
            print("Opzione non valida! Riprova.")

def analizza_sicurezza():
    print("Analisi della sicurezza del dispositivo...")

def analizza_sicurezza_app_menu():
    while True:
        print("\n--- ANALISI SICUREZZA APP ---")
        print("1. Analizza sicurezza di un'app")
        print("2. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            package_name = input("Inserisci il nome del pacchetto dell'app: ")
            risultati = analizza_sicurezza_app(package_name)
            if 'error' not in risultati:
                print(f"Analisi della sicurezza completata: {risultati}")
            else:
                print(f"Errore nell'analizzare la sicurezza dell'app: {risultati['error']}")
        elif scelta == "2":
            break
        else:
            print("Opzione non valida! Riprova.")

def menu_backup_ripristino():
    while True:
        print("\n--- BACKUP E RIPRISTINO ---")
        print("1. Backup dati")
        print("2. Ripristino dati")
        print("3. Torna al menu principale")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            source_dir = input("Inserisci la directory di origine dei dati: ")
            backup_dir = input("Inserisci la directory di destinazione del backup: ")
            backup_dati(source_dir, backup_dir)
        elif scelta == "2":
            backup_dir = input("Inserisci la directory del backup: ")
            restore_dir = input("Inserisci la directory di destinazione per il ripristino: ")
            ripristina_dati(backup_dir, restore_dir)
        elif scelta == "3":
            break
        else:
            print("Opzione non valida! Riprova.")

if __name__ == "__main__":
    try:
        menu_principale()
    except KeyboardInterrupt:
        log("Programma interrotto dall'utente.", level="WARNING")
    except Exception as e:
        log(f"Errore inatteso: {e}", level="ERROR")
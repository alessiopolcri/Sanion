import argparse
from lib.panic.panic import panic_button
from lib.security.security import ricerca_tracce, pulizia_tracce, cerca_app_installate
from lib.settings.settings import menu_impostazioni
from lib.device.device_settings import menu_impostazioni_dispositivo
from lib.security.security_analysis import analizza_sicurezza_app
from lib.backup.backup import backup_dati, ripristina_dati
from lib.real_time_monitoring.real_time_monitoring import monitoraggio_tempo_reale
from lib.logger.logger import log
from utils.strings import STRINGS
from colorama import Fore, Style, init
import inquirer

init(autoreset=True)

def mostra_logo():
    logo = r"""
    ____              _             
   / __ \            (_)            
  | |  | |_ __   __ _ _ _ __   __ _ 
  | |  | | '_ \ / _` | | '_ \ / _` |
  | |__| | | | | (_| | | | | | (_| |
   \____/|_| |_|\__, |_|_| |_|\__, |
                 __/ |         __/ |
                |___/         |___/ 
    """
    print(Fore.CYAN + logo)

def main():
    mostra_logo()

    parser = argparse.ArgumentParser(description="Sanion CLI")
    parser.add_argument('--sicurezza', action='store_true', help=STRINGS['sicurezza_dispositivo'])
    parser.add_argument('--tracce', action='store_true', help=STRINGS['ricerca_e_pulizia_tracce'])
    parser.add_argument('--panic', action='store_true', help=STRINGS['panic_button'])
    parser.add_argument('--impostazioni', action='store_true', help=STRINGS['impostazioni'])
    parser.add_argument('--impostazioni-dispositivo', action='store_true', help=STRINGS['impostazioni_dispositivo'])
    parser.add_argument('--analisi-app', action='store_true', help=STRINGS['analisi_sicurezza_app'])
    parser.add_argument('--backup', action='store_true', help=STRINGS['backup_e_ripristino'])
    parser.add_argument('--monitoraggio', action='store_true', help=STRINGS['monitoraggio_tempo_reale'])

    args = parser.parse_args()

    if args.sicurezza:
        analizza_sicurezza()
    elif args.tracce:
        sotto_menu_tracce()
    elif args.panic:
        conferma = input("⚠ Sei sicuro di voler attivare il PANIC BUTTON? (s/n): ")
        if conferma.lower() == "s":
            panic_button(cerca_app_installate())
    elif args.impostazioni:
        menu_impostazioni()
    elif args.impostazioni_dispositivo:
        menu_impostazioni_dispositivo()
    elif args.analisi_app:
        analizza_sicurezza_app_menu()
    elif args.backup:
        menu_backup_ripristino()
    elif args.monitoraggio:
        monitoraggio_tempo_reale()
    else:
        menu_principale()

def menu_principale():
    questions = [
        inquirer.List('menu',
                      message="Seleziona un'opzione",
                      choices=[
                          STRINGS['sicurezza_dispositivo'],
                          STRINGS['ricerca_e_pulizia_tracce'],
                          STRINGS['panic_button'],
                          STRINGS['impostazioni'],
                          STRINGS['impostazioni_dispositivo'],
                          STRINGS['analisi_sicurezza_app'],
                          STRINGS['backup_e_ripristino'],
                          STRINGS['monitoraggio_tempo_reale'],
                          STRINGS['esci']
                      ]),
    ]
    risposta = inquirer.prompt(questions)

    if risposta['menu'] == STRINGS['sicurezza_dispositivo']:
        analizza_sicurezza()
    elif risposta['menu'] == STRINGS['ricerca_e_pulizia_tracce']:
        sotto_menu_tracce()
    elif risposta['menu'] == STRINGS['panic_button']:
        conferma = input("⚠ Sei sicuro di voler attivare il PANIC BUTTON? (s/n): ")
        if conferma.lower() == "s":
            panic_button(cerca_app_installate())
    elif risposta['menu'] == STRINGS['impostazioni']:
        menu_impostazioni()
    elif risposta['menu'] == STRINGS['impostazioni_dispositivo']:
        menu_impostazioni_dispositivo()
    elif risposta['menu'] == STRINGS['analisi_sicurezza_app']:
        analizza_sicurezza_app_menu()
    elif risposta['menu'] == STRINGS['backup_e_ripristino']:
        menu_backup_ripristino()
    elif risposta['menu'] == STRINGS['monitoraggio_tempo_reale']:
        monitoraggio_tempo_reale()
    elif risposta['menu'] == STRINGS['esci']:
        log(STRINGS['uscita_dal_programma'], level="INFO")

def sotto_menu_tracce():
    questions = [
        inquirer.List('menu_tracce',
                      message="Seleziona un'opzione",
                      choices=[
                          "1. Ricerca Tracce",
                          "2. Pulizia Tracce",
                          "3. Torna al menu principale"
                      ]),
    ]
    risposta = inquirer.prompt(questions)

    if risposta['menu_tracce'] == "1. Ricerca Tracce":
        directory = input("Inserisci la directory da analizzare: ")
        if not os.path.exists(directory):
            print(Fore.RED + "❌ Directory non valida!")
            return
        ricerca_tracce(directory)
    elif risposta['menu_tracce'] == "2. Pulizia Tracce":
        conferma = input("⚠ Sei sicuro di voler pulire tutte le tracce? (s/n): ")
        if conferma.lower() == "s":
            pulizia_tracce()
    elif risposta['menu_tracce'] == "3. Torna al menu principale":
        menu_principale()

def analizza_sicurezza():
    print("Analisi della sicurezza del dispositivo...")

def analizza_sicurezza_app_menu():
    questions = [
        inquirer.List('menu_analisi_app',
                      message="Seleziona un'opzione",
                      choices=[
                          "1. Analizza sicurezza di un'app",
                          "2. Torna al menu principale"
                      ]),
    ]
    risposta = inquirer.prompt(questions)

    if risposta['menu_analisi_app'] == "1. Analizza sicurezza di un'app":
        package_name = input("Inserisci il nome del pacchetto dell'app: ")
        risultati = analizza_sicurezza_app(package_name)
        if 'error' not in risultati:
            print(f"Analisi della sicurezza completata: {risultati}")
        else:
            print(Fore.RED + f"Errore nell'analizzare la sicurezza dell'app: {risultati['error']}")
    elif risposta['menu_analisi_app'] == "2. Torna al menu principale":
        menu_principale()

def menu_backup_ripristino():
    questions = [
        inquirer.List('menu_backup',
                      message="Seleziona un'opzione",
                      choices=[
                          "1. Backup dati",
                          "2. Ripristino dati",
                          "3. Torna al menu principale"
                      ]),
    ]
    risposta = inquirer.prompt(questions)

    if risposta['menu_backup'] == "1. Backup dati":
        source_dir = input("Inserisci la directory di origine dei dati: ")
        backup_dir = input("Inserisci la directory di destinazione del backup: ")
        backup_dati(source_dir, backup_dir)
    elif risposta['menu_backup'] == "2. Ripristino dati":
        backup_dir = input("Inserisci la directory del backup: ")
        restore_dir = input("Inserisci la directory di destinazione per il ripristino: ")
        ripristina_dati(backup_dir, restore_dir)
    elif risposta['menu_backup'] == "3. Torna al menu principale":
        menu_principale()
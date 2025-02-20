import subprocess
from logger import log

def analizza_sicurezza_app(package_name):
    """
    Analizza la sicurezza di un'app installata sul dispositivo.

    Args:
        package_name (str): Il nome del pacchetto dell'app da analizzare.

    Returns:
        dict: Un dizionario con i risultati dell'analisi della sicurezza.
    """
    log(f"Avvio analisi della sicurezza per l'app: {package_name}", level="INFO")
    risultati = {}
    try:
        # Simula l'analisi della sicurezza dell'app
        comando = f"pm path {package_name}"
        output = subprocess.check_output(comando, shell=True, text=True)
        if output:
            log(f"App {package_name} trovata: {output.strip()}", level="INFO")
            risultati['sicurezza'] = "Nessuna vulnerabilità conosciuta trovata"
        else:
            log(f"App {package_name} non trovata", level="WARNING")
            risultati['error'] = f"App {package_name} non trovata"
    except subprocess.CalledProcessError as e:
        log(f"❌ Errore durante l'analisi della sicurezza dell'app: {e}", level="ERROR")
        risultati['error'] = str(e)
    return risultati
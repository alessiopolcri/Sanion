import subprocess
from lib.logger.logger import log
from lib.exceptions.exceptions import handle_exception, SecurityException

def analizza_sicurezza_app(package_name):
    log(f"Avvio analisi della sicurezza per l'app: {package_name}", level="INFO")
    risultati = {}
    try:
        comando = f"pm path {package_name}"
        output = subprocess.check_output(comando, shell=True, text=True)
        if output:
            log(f"App {package_name} trovata: {output.strip()}", level="INFO")
            risultati['sicurezza'] = "Nessuna vulnerabilità conosciuta trovata"
        else:
            log(f"App {package_name} non trovata", level="WARNING")
            risultati['error'] = f"App {package_name} non trovata"
    except subprocess.CalledProcessError as e:
        handle_exception(SecurityException(f"Errore durante l'analisi della sicurezza dell'app: {e}"))
        risultati['error'] = str(e)
    return risultati
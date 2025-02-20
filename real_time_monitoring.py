import time
import psutil
from logger import log

def monitoraggio_tempo_reale():
    """
    Monitora le attività del sistema in tempo reale.
    """
    log("Avvio monitoraggio in tempo reale delle attività del sistema...", level="INFO")
    try:
        while True:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            log(f"Utilizzo CPU: {cpu_percent}%", level="INFO")
            log(f"Utilizzo memoria: {memory_info.percent}%", level="INFO")
            time.sleep(5)
    except KeyboardInterrupt:
        log("Monitoraggio in tempo reale interrotto dall'utente.", level="WARNING")
    except Exception as e:
        log(f"❌ Errore durante il monitoraggio in tempo reale: {e}", level="ERROR")
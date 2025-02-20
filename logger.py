import logging
from cryptography.fernet import Fernet

# Configurazione del logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s [%(levelname)s] %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')

# Genera una chiave di crittografia (salvala in un file sicuro)
chiave = Fernet.generate_key()
cipher_suite = Fernet(chiave)

def log(message, level="INFO"):
    """
    Registra un messaggio nel file di log.

    Args:
        message (str): Il messaggio da registrare.
        level (str): Il livello di severità del log. Default è "INFO".
    """
    log_entry = f"{message}\n"
    log_entry_cifrata = cipher_suite.encrypt(log_entry.encode())

    if level == "DEBUG":
        logging.debug(log_entry_cifrata.decode())
    elif level == "INFO":
        logging.info(log_entry_cifrata.decode())
    elif level == "WARNING":
        logging.warning(log_entry_cifrata.decode())
    elif level == "ERROR":
        logging.error(log_entry_cifrata.decode())
    elif level == "CRITICAL":
        logging.critical(log_entry_cifrata.decode())
import time
import os
from cryptography.fernet import Fernet

LOG_FILE = "app.log"

# Genera una chiave di crittografia (salvala in un file sicuro)
chiave = Fernet.generate_key()
cipher_suite = Fernet(chiave)

def log(message, level="INFO"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    print(log_entry, end="")
    
    # Crittografa il log prima di scriverlo
    log_entry_cifrata = cipher_suite.encrypt(log_entry.encode())
    with open(LOG_FILE, "ab") as f:
        f.write(log_entry_cifrata)

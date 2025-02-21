from lib.logger.logger import log

class CustomException(Exception):
    """
    Classe base per tutte le eccezioni personalizzate.
    """
    def __init__(self, message, level="ERROR"):
        super().__init__(message)
        self.message = message
        self.level = level
        log(self.message, self.level)

class FileNotFoundError(CustomException):
    """
    Eccezione per file non trovati.
    """
    def __init__(self, file_path):
        message = f"File non trovato: {file_path}"
        super().__init__(message, level="ERROR")

class SecurityException(CustomException):
    """
    Eccezione per errori di sicurezza.
    """
    def __init__(self, message="Errore di sicurezza"):
        super().__init__(message, level="CRITICAL")

class BackupException(CustomException):
    """
    Eccezione per errori di backup.
    """
    def __init__(self, message="Errore durante il backup"):
        super().__init__(message, level="WARNING")

class RestoreException(CustomException):
    """
    Eccezione per errori di ripristino.
    """
    def __init__(self, message="Errore durante il ripristino"):
        super().__init__(message, level="WARNING")

def handle_exception(e):
    if isinstance(e, CustomException):
        log(e.message, e.level)
    else:
        log(f"Errore non gestito: {e}", level="ERROR")
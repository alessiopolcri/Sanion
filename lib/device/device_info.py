# device_info.py
import platform
import os
import socket
import re

def get_local_device_info():
    """
    Restituisce informazioni generali sul dispositivo locale.
    """
    info = {
        'os': platform.system(),
        'os_version': platform.release(),
        'architecture': platform.architecture()[0],
        'hostname': socket.gethostname(),
        'processor': platform.processor(),
        'device_type': _guess_local_device_type()
    }
    return info

def _guess_local_device_type():
    """
    Cerca di determinare il tipo di dispositivo locale basandosi sull'OS.
    """
    system = platform.system().lower()
    
    if system == 'linux':
        if _is_android():
            return 'mobile'
        return 'desktop'
    elif system == 'windows':
        return 'desktop/tablet'  # Windows può essere entrambi
    elif system == 'darwin':
        return 'desktop'  # macOS, iOS non supporta Python standard
    return 'unknown'

def _is_android():
    """
    Verifica se il sistema è Android.
    """
    try:
        with open('/system/build.prop', 'r') as f:
            return True
    except FileNotFoundError:
        pass
    
    uname = os.uname()
    if 'android' in uname.version.lower():
        return True
    return False

def parse_user_agent(user_agent):
    """
    Analizza una stringa User-Agent per determinare il tipo di dispositivo.
    """
    ua = user_agent.lower()
    
    # Dispositivi mobili
    if re.search(r'mobile|android|iphone|windows phone', ua):
        return 'mobile'
    
    # Tablet
    if re.search(r'ipad|tablet|kindle|silk', ua) and not re.search(r'mobile', ua):
        return 'tablet'
    
    # Desktop
    if re.search(r'windows nt|macintosh|linux|x11|mac os', ua):
        return 'desktop'
    
    # Bot/Crawler
    if re.search(r'bot|crawler|spider|facebookexternalhit', ua):
        return 'bot'
    
    return 'unknown'

# Esempio di utilizzo
if __name__ == '__main__':
    print("Local Device Info:", get_local_device_info())
    
    test_agents = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; SM-T860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    ]
    
    for ua in test_agents:
        print(f"User Agent: {ua[:60]}... → Device Type:", parse_user_agent(ua))
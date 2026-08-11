from datetime import datetime
from .config import LOG_PATH

def write_log(message, separator=False):
    """
    Registra un mensaje, identificando fecha y hora, en el archivo audit_log.txt y luego muestra el mensaje en la terminal
    
    Args:
        message (str)
        separator (bool, optional)
    
    Returns:
        str
    """
    
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
    
    log_message = (
        f"[{timestamp}] {message}\n"
    )
    
    if separator:
    
        log_message += (
            "=" * 90 + "\n"
        )
        
    with open(
        LOG_PATH,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(log_message)
    
    return log_message
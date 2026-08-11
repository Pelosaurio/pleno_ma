from .write_log import write_log
from .show_log import show_log

def log_message(message, separator=False):
    """
    Registra un mensaje en audit_log y lo muestra en la terminal
    
    Args:
        message (str)
        separator (bool)
        
    Returns:
        None
    """

    log_message = write_log(
        message,
        separator=separator
    )
    
    show_log(log_message)
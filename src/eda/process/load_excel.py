import pandas as pd

from ..utils.logging import log_message

def load_excel(path, sheet_name=None, log=True):
    """
    Carga una o multiples hojas de un archivo Excel
    
    Args:
        path (str)
        sheet_name (str | list | None)
        log (bool)
        
    Returns:
        DataFrame | dict 
    """
    
    data = pd.read_excel(
        path,
        sheet_name=sheet_name
    )
    
    if log:
        log_message(
            (
                f"El archivo Excel ha sido cargado correctamente | \n"
                f"Ruta del archivo: {path} \n"
            ),
            separator=True
        )
    
    return data



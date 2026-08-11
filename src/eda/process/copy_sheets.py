from ..utils.logging import log_message

def copy_sheets(data, log=True):
    """
    Crea copia de las hojas de un archivo Excel y su contenido
    
    Args:
        data (dict)
        log (bool)
        
    Returns:
        dict
    """
    
    copied_data = {
        sheet: df.copy()
        for sheet, df in data.items()
    }
    
    if log:
        log_message(
            (
                f"Se ha creado una copia de todas las hojas del Excel | \n"
                f"Numero de hojas copiadas: {len(copied_data)} | \n"
            ),
            separator=True
        )
    
    return copied_data
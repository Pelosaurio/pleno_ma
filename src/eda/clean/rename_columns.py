from ..process import get_columns
from ..utils.logging import log_message

def rename_columns(df, new_columns, log=True):
    """
    Renombra columnas de un DataFrame
    
    Args:
        df (DataFrame)
        new_columns (list)
        
    Returns:
        DataFrame
    """
    
    df.columns = new_columns
    
    columns = get_columns(df)
    
    if log:
        log_message(
            (
                f"Se han actualizado los nombres de las columnas del DataFrame | \n"
                f"Nombres de columnas actualizados: \n"
                f"{columns} | \n"          
            ),
            separator=True
        )
    
    return df
from ..process import get_columns
from ..utils.logging import log_message

def select_columns(df, columns_range, log=True):
    """
    Selecciona las columnas de un DataFrame por posicion
    
    Args:
        df (DataFrame)
        columns_range (tuple)
        log (bool)
        
    Returns:
        DataFrame
    """
        
    start, end = columns_range
    
    selected_columns = df.iloc[:, start:end]
    
    columns = get_columns(selected_columns)
    
    if log:
        log_message(
            (
                f"Se ha aplicado un filtrado de columnas sobre el DataFrame | \n"
                f"Columnas originales: {df.shape[1]} | \n"          
                f"Rango seleccionado: ({start}, {end}) | \n"
                f"Columnas finales: {selected_columns.shape[1]} \n"
                f"{columns} | \n"
            ),
            separator=True
        )
    
    return selected_columns
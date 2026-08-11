import pandas as pd

from .mean_group import mean_group
from .median_group import median_group
from .mode_group import mode_group
from ..utils.logging import log_message

def central_t(df, group_column, column_names, log=True):
    """
    Calcula las medidas de tendencia central para columnas numericas agrupadas por una variable categorica
    
    Args:
        df (DataFrame)
        group_column (str)
        column_names (list)
        log (bool)
        
    Returns:
        dict
    """
    
    mean_result = mean_group(df, group_column, column_names)
    
    median_result = median_group(df, group_column, column_names)
    
    mode_result = mode_group(df, group_column, column_names)
    
    if log:
        log_message(
            (
                f"Medidas de tendencia central agrupadas calculadas exitosamente | \n"
                f"Columnas analizadas = {column_names} | \n"
                f"Agrupadas por: {group_column} | \n"
            ),
            separator=True
        )
    
    return {
        "promedio": mean_result,
        "mediana": median_result,
        "moda": mode_result
        }
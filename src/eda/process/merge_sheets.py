import pandas as pd

from .add_column import add_column
from ..utils.logging import log_message

def merge_sheets(data, valid_sheets, id_column, position=None, log=True):
    """
    Une multiples hojas Excel y agrega columna identificadora
    
    Args:
        data (dict)
        valid_sheets (list)
        id_column (str)
        
    Returns:
        DataFrame
    """
    
    dfs = []
    
    for sheet in valid_sheets:
        
        df = data[sheet]
        
        df = add_column(
            df,
            id_column,
            sheet,
            position=position
        )
        
        dfs.append(df)
        
    merged_df = pd.concat(
        dfs,
        ignore_index=True
    )
    
    if log:
        log_message(
            (
                f"Se han unificado las hojas válidas correctamente | \n "
                f"Hojas procesadas: {len(valid_sheets)} | \n "
                f"Filas: {merged_df.shape[0]} | \n "
                f"Columnas: {merged_df.shape[1]} | \n "
                f"Nueva columna agregada: '{id_column}' | \n "
            ),
            separator=True
        )
    
    return merged_df
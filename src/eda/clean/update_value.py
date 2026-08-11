from ..utils.validators import validate_columns
from ..utils.logging import log_message

def update_value(df, row_index, column_name, new_value, log=True):
    """
    Actualiza un valor especifico de un DataFrame y registra su correccion
    
    Args:
        df (DataFrame)
        row_index (int)
        column_name (str)
        new_value (int)
        
    Returns:
        DataFrame
    """
    
    validate_columns(df, column_name)
    
    old_value = df.loc[
        row_index,
        column_name
    ]
    
    df.loc[
        row_index,
        column_name
    ] = new_value
    
    if log: 
        log_message(
            (
                f"Se ha actualizado un valor en el DataFrame | \n"
                f"Fila : {row_index} | \n" 
                f"Columna: {column_name} | \n" 
                f"Valor antiguo: {old_value} | \n"
                f"Valor actualizado: {new_value} | \n"  
            ),
            separator=True
        )

    return df
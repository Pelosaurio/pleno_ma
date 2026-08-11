from ..analysis import count_missing_values
from ..utils.logging import log_message

def fill_nan(df, log=True):
    """
    Detecta valores nulos y los reemplaza con 0
    
    Args:
        df (DataFrame)
        log (bool)
        
    Returns:
        DataFrame
    """
    missing = count_missing_values(df)
    
    if missing == 0:
        if log:
            log_message(
                (
                    f"No se detectaron valores nulos en el DataFrame 😎 | \n"
                ),
                separator=True
            )
    
    else:
        for col in df.select_dtypes(include=['int64', 'float64']).columns:
            df[col] = df[col].fillna(0)
        
        new_count = count_missing_values(df)
        
        if log:
            log_message(
                (
                    f"Limpieza de valores nulos completada | \n"
                    f"Valores nulos detectados: {missing} | \n"
                    f"Valores reemplazados por: 0 | \n"
                    f"Valores nulos actuales: {new_count}  | \n"
                ),
                separator=True
            )
    
    return df


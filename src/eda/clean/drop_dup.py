from ..analysis import count_duplicates
from ..utils.logging import log_message

def drop_dup(df, log=True):
    """
    Elimina filas duplicadas del DataFrame
    
    Args:
        df (DataFrame)
        log (bool)
        
    Returns:
        DataFrame
    """
    
    duplicates = count_duplicates(df)
    
    if duplicates == 0:
        if log:
            log_message(
                (
                    f"No se detectaron registros duplicados en el Dataframe 😎 | \n"
                ),
                separator=True
            )
    
    else:
        df.drop_duplicates(inplace=True)
        
        if log:
            log_message(
                (
                    f"Limpieza de datos realizada | \n"
                    f"N° de duplicados detectados: {duplicates} | \n"
                    f"Filas actuales: {df.shape[0]}  | \n"
                ),
                separator=True
            )
    
    return df
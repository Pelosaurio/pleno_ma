from ..utils.validators import validate_columns, validate_numeric_columns
from ..utils.logging import log_message

def vote_rates(df, column_name, group_column, vote_cols, log=True, percentage=True):
    """
    Calcula la tasa de ocurrencia de los votos emitidos por convencional para una variable categorica
    
    Args:
        df (DataFrame)
        column_name (str)
        group_column (str)
        vote_cols (list)
        log (bool)
        percentage (bool)
        
    Returns:
        DataFrame
    """
    
    validate_columns(df, [column_name, group_column])
    validate_numeric_columns(df, vote_cols)
    
    vote_rates = (df.groupby(
        [column_name, group_column]
        )
        [vote_cols]
        .mean()
        .reset_index()
    )
    
    if percentage:
        vote_rates[vote_cols] = (vote_rates[vote_cols] * 100)
        
    if log:
        log_message(
            (
                f"Tasa de ocurrencia de votaciones calculada | \n"
                f"Columnas analizadas = {vote_cols}  | \n"
                f"Filas analizadas = {len(df)} | \n"
                f"Agrupadas por las columnas: '{column_name}' - '{group_column}' | \n"
                f"Convencionales únicos = {df[column_name].nunique()} | \n"
                f"Colectivos únicos = {df[group_column].nunique()} | \n"
                f"Registros generados = {len(vote_rates)} | \n"
                f"Escala aplicada = Porcentaje  | \n"
            ),
            separator=True
        )
    
    return vote_rates
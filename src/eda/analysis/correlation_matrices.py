from ..utils.validators import validate_numeric_columns, validate_columns
from ..utils.logging import log_message

def correlation_matrices(df, column_name, group_column, vote_cols, log=True):
    """
    Calcula matrices de correlacion entre colectivos para cada tipo de voto
    
    Args:
        df (DataFrame)
        column_name (str)
        group_column (str)
        vote_cols (list)
        log (bool)
        
    Returns:
        dict
    """
    validate_columns(df, [column_name, group_column])
    validate_numeric_columns(df, vote_cols)
    
    matrices = {}
    
    for vote_col in vote_cols:
    
        pivot_df = df.pivot_table(
            index=column_name,
            columns=group_column,
            values=vote_col,
            aggfunc="mean"
        )
        
        matrices[vote_col] = pivot_df.corr()
        
    if log:
        log_message(
            (
                f"Matrices de correlación entre colectivos calculadas | \n"
                f"Variables analizadas = {vote_cols} | \n"
                f"Artículos analizados = {pivot_df.shape[0]} | \n"
                f"Colectivos analizados = {pivot_df.shape[1]} | \n"
                f"Matrices calculadas = {len(vote_cols)} | \n"
            ),
            separator=True
        )
    
    return matrices
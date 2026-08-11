from ..utils.validators import validate_columns
from ..utils.logging import log_message

def exclude_categories(df, group_column, excluded_categories, log=True):
    """
    Excluye datos correspondientes a categorias innecesarias de una columna 
    
    Args:
        df (DataFrame)
        group_column (str)
        excluded_categories (list)
        log (bool)
        
    Returns:
        DataFrame
    """
    
    validate_columns(df, group_column)
    
    if excluded_categories is None:
        excluded_categories = []
    
    filtered_df =  df[~df[group_column].isin(excluded_categories)]
    
    df_rows = df.shape[0]
    
    filtered_df_rows = filtered_df.shape[0]
    
    if log:
        if len(excluded_categories) == 0:
            log_message(
                (
                    f"No se aplicaron filtros de categoría en el DataFrame | \n"
                ),
                separator=True
            )
        
        elif len(excluded_categories) == 1:
            log_message(
                (
                    f"Ha sido excluida {len(excluded_categories)} categoria correctamente | \n"
                    f"Categoria excluida = {excluded_categories} | \n"
                    f"Registros eliminados = {df_rows - filtered_df_rows} | \n"
                ),
                separator=True
            )
        
        else:
            log_message(
                (
                    f"Han sido excluidas {len(excluded_categories)} categorias correctamente | \n"
                    f"Categorias excluidas = {excluded_categories} | \n"
                    f"Registros eliminados = {df_rows - filtered_df_rows} | \n"
                ),
                separator=True
            )
    
    return filtered_df
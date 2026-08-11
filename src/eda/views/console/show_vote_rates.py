from .show_title import show_title
from .show_separator import show_separator

def show_vote_rates(df, group_column, value_columns, sort_column):
    """
    Muestra las tasas de votacion agrupadas por colectivo
    
    Args:
        df (DataFrame)
        group_column(str)
        value_columns(list)
    
    Returns:
        None
    """
    
    grouped_rates = (
        df.groupby(group_column)[value_columns]
        .mean()
        .sort_values(sort_column, ascending=False)
    )
    
    show_title(f"Tasas de votación por colectivo \n")
    
    print(grouped_rates.to_string(float_format="%.2f"))
    
    print()
    
    show_separator()
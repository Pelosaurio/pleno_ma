from .boxplot import plot_boxplot
from .heatmap import plot_heatmap
from .barplot import plot_barplot

PLOT_DISPATCHER = {
    "boxplot": plot_boxplot,
    "heatmap": plot_heatmap,
    "barplot": plot_barplot
}

def plot_factory(df, plot_type, column_or_columns, config):
    """
    Genera graficos especializados a partir de un DataFrame segun el tipo solicitado
    
    Args:
        df (DataFrame)
        plot_type (str)
        column_or_columns (tuple | None)
        config (dict)
    
    Returns:
        None
    """
    
    if plot_type not in PLOT_DISPATCHER:
        raise ValueError(f"Tipo de grafico no soportado: {plot_type}")
    
    plot_function = PLOT_DISPATCHER[plot_type]
    
    if plot_type == "boxplot":
        group_column, value_column = column_or_columns
        
        plot_function(df=df, group_column=group_column, value_column=value_column, config=config)
        
    elif plot_type == "heatmap":
        plot_function(df=df, config=config)
        
    elif plot_type == "barplot":
        group_column, value_columns = column_or_columns
        
        plot_function(df=df, group_column=group_column, value_columns=value_columns, config=config)
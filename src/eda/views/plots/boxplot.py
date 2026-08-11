import seaborn as sns 
import matplotlib.pyplot as plt
    
from ...utils.validators import validate_numeric_columns, validate_columns
from .base import render_or_save_plot, prepare_plot
from ...utils.logging import log_message

def plot_boxplot(df, group_column, value_column, config, log=True):
    """
    Genera un boxplot para analizar la cohesión de voto entre colectivos mediante la distribución de tasas de votación
    
    Args:
        df (DataFrame)
        group_column (str)
        value_column (str)
        config (dict)
        log (bool)
    
    Returns:
        None
    """
    
    validate_columns(df, [group_column, value_column])
    validate_numeric_columns(df, value_column)
    
    # Configuracion del grafico
    title = config.get('title', f"Cohesión de {value_column} por colectivo")
    xlabel = config.get('xlabel', value_column)
    ylabel = config.get('ylabel', group_column)
    show_grid = config.get('show_grid', True)
    linestyle = config.get('linestyle', '--')
    alpha = config.get('alpha', 0.5)
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    figsize = config.get('figsize', (12, 6))
    showfliers = config.get('showfliers', True)
    width = config.get("width", 0.6)
    linewidth = config.get("linewidth", 1)
    boxprops = config.get('boxprops')
    medianprops = config.get('medianprops')
    whiskerprops = config.get('whiskerprops')
    capprops = config.get('capprops')
    flierprops = config.get('flierprops')
    sort_by = config.get('sort_by', 'median')
    
    if sort_by == 'median':
        order = (
            df.groupby(group_column)[value_column]
            .median()
            .sort_values()
            .index
        )
        
    else:
        order = None
        
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', f"{value_column.lower().replace(' ', '_')}_boxplot.{format}")
    
    plt.figure(figsize=figsize)
    
    sns.boxplot(
        data = df, 
        y = group_column,
        x = value_column, 
        order = order,
        showfliers = showfliers,
        width=width,
        linewidth=linewidth,
        boxprops = boxprops,
        medianprops = medianprops,
        whiskerprops = whiskerprops,
        capprops = capprops,
        flierprops = flierprops
    )
    prepare_plot(title, xlabel, ylabel, show_grid, linestyle, alpha)
    render_or_save_plot(output_dir, filename, format, dpi)
    
    if log:
        log_message(
            (
                f"¡Boxplot generado exitosamente! | \n"
                f"Título = {title} | \n"
                f"Columna analizada = {value_column} | \n"
                f"Agrupado por = {group_column} | \n"
                f"Filas analizadas = {len(df)} | \n"
                f"Ordenado por = {sort_by} | \n"
                f"Archivo generado = {filename} | \n"
            ),
            separator=True
        )
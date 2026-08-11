import seaborn as sns
import matplotlib.pyplot as plt      

from .base import prepare_plot, render_or_save_plot
from ...utils.logging import log_message

def plot_heatmap(df, config, log=True):
    """
    Genera un heatmap para visualizar una matriz de correlacion
    
    Args:
        df (DataFrame)
        config (dict)
        log (bool)
    
    Returns:
        None
    """
    
    title = config.get('title', f"Heatmap de correlación entre colectivos")
    annot = config.get('annot', True)
    fmt = config.get('fmt', '.1f')
    cmap = config.get('cmap')
    cbar = config.get('cbar', True)
    figsize = config.get('figsize', (12, 10))
    format = config.get('format', 'png')
    dpi = config.get('dpi', 300)
    output_dir = config.get('output_dir', None)
    filename = config.get('filename', f"correlation_heatmap.{format}")
    
    plt.figure(figsize=figsize)
    
    sns.heatmap(df, annot=annot, fmt=fmt, cmap=cmap, cbar=cbar, vmin=-1, vmax=1)
    
    prepare_plot(title=title)
    
    render_or_save_plot(output_dir, filename, format, dpi)
    
    if log:
        log_message(
            (
                f"¡Heatmap generado exitosamente! | \n"
                f"Título = {title} | \n"
                f"Filas matriz = {df.shape[0]} | \n"
                f"Columnas matriz = {df.shape[1]} | \n"
                f"Color del mapa = {cmap} | \n"
                f"Archivo generado = {filename} | \n"
            ),
            separator=True
        )
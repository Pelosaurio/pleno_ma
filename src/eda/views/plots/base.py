import matplotlib.pyplot as plt
from ...utils import generate_output_path

def prepare_plot(
    title=None, 
    xlabel=None, 
    ylabel=None,
    show_grid=True,
    linestyle='--',
    alpha=0.5,
    legend=False
):
    """
    Aplica configuraciones generales de presentación a un gráfico
    
    Args:
        title (str, optional)
        xlabel (str, optional)
        ylabel (str, optional)
        show_grid (bool, optional)
        linestyle (str, optional)
        alpha (float, optional)
        legend (bool, optional)
        
    Returns:
        None
    """
    
    if title:
        plt.title(title)
    if xlabel:
        plt.xlabel(xlabel)
    if ylabel:
        plt.ylabel(ylabel)
    if show_grid:
        plt.grid(True, linestyle=linestyle, alpha=alpha)
    if legend:
        plt.legend()
        
    plt.tight_layout()
    
    
def render_or_save_plot(output_dir, filename, format='png', dpi=300):
    """
    Guarda un grafico en disco o lo muestra en pantalla
    
    Args:
        output_dir (Path | None)
        filename (str | None)
        format (str)
        dpi (int)
        
    Returns:
        None
    """
    
    if output_dir and filename:
        output_path = generate_output_path(output_dir, filename)
        plt.savefig(output_path, format=format, dpi=dpi, bbox_inches="tight")
        plt.close()   
        
    else:
        plt.show()
        plt.close()

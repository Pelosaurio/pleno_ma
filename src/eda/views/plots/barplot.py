import seaborn as sns
import matplotlib.pyplot as plt

from .base import prepare_plot, render_or_save_plot
from ...utils.validators import validate_numeric_columns, validate_columns
from ...process.sort_dataframe import sort_dataframe
from ...utils.logging import log_message

def plot_barplot(df, group_column, value_columns, config, log=True):
    """
    Genera un barplot para visualizar la distribucion de votaciones por colectivo
    
    Args:
        df (DataFrame)
        group_column (str)
        value_columns (list)
        config (dict)
        log (bool)
        
    Returns:
        None
    """
    
    validate_columns(df, [group_column, *value_columns])
    validate_numeric_columns(df, value_columns)
    
    title = config.get("title", "Distribución de votaciones por Colectivo")
    xlabel = config.get("xlabel", group_column)
    ylabel = config.get("ylabel", "Tasa %")
    figsize = config.get("figsize", (12, 6))
    palette = config.get("palette")
    sort_column = config.get("sort_column")
    ascending = config.get("ascending", False)
    legend_loc = config.get("legend_loc", "upper left")
    legend_bbox = config.get("legend_bbox", (1.02, 1))
    stacked = config.get("stacked", True)
    format = config.get("format", "png")
    dpi = config.get("dpi", 300)
    edgecolor = config.get("edgecolor")
    linewidth = config.get("linewidth", 1)
    output_dir = config.get("output_dir", None)
    filename = config.get("filename", f"barplot.{format}")
    
    plt.figure(figsize=figsize)
    
    df_grouped = (
        df.groupby(group_column)[value_columns]
        .mean()
        .reset_index()
        )
    
    if stacked:
        if sort_column is not None:
            df_grouped = sort_dataframe(df_grouped, column=sort_column, ascending=ascending)
        
        bottom = None
        
        if sort_column in value_columns:
            stack_order = [sort_column] + [
                col for col in value_columns
                if col != sort_column
            ]
        else:
            stack_order = value_columns
        
        for col in stack_order:
            plt.bar(
                df_grouped[group_column],
                df_grouped[col],
                bottom=bottom,
                color=palette[col],
                label=col,
                alpha=0.85,
                edgecolor=edgecolor,
                linewidth=linewidth
            )
            
            if bottom is None:
                bottom = df_grouped[col]
            else:
                bottom += df_grouped[col]
                
    else:
        if sort_column is not None:
            df_grouped = sort_dataframe(df_grouped, column=sort_column, ascending=ascending)
            
        df_grouped = (
            df_grouped.melt(id_vars=group_column,
                var_name="Tipo de voto",
                value_name="Tasa")
        )
        
        sns.barplot(
            data=df_grouped,
            x=group_column,
            y="Tasa",
            hue="Tipo de voto",
            palette=palette,
            edgecolor=edgecolor,
            linewidth=linewidth
        )
        
    prepare_plot(title, xlabel, ylabel)
    
    plt.xticks(rotation=35, ha="right")
        
    plt.legend(title = "Tipo de voto", loc=legend_loc, bbox_to_anchor=legend_bbox)
    
    render_or_save_plot(output_dir, filename, format, dpi)
    
    if log:
        log_message(
            (
                f"¡Barplot generado exitosamente! | \n"
                f"Título = {title} | \n"
                f"Agrupado por = {group_column} | \n"
                f"Columnas analizadas = {value_columns} | \n"
                f"Filas analizadas = {len(df)} | \n"
                f"Stacked = {stacked} | \n"
                f"Archivo generado = {filename} | \n"
            ),
            separator=True
        )
from eda.config.path.paths import PROCESSED_DATA_DIR
from eda.utils import generate_output_path
from eda.utils.logging import log_message
from eda.views.plots import plot_factory

from eda.views.console import(
    show_keys,
    show_head,
    show_columns,
    show_value_counts,
    show_summary,
    show_vote_rates,
    show_cohesion
)

from eda.process import(
    load_excel,
    copy_sheets,
    exclude_sheets,
    merge_sheets,
    save_dataframe
)

from eda.clean import(
    select_columns,
    rename_columns,
    exclude_categories,
    fill_nan,
    drop_dup,
    update_value
)

from eda.utils.validators import (
    validate_votes,
    validate_integrity
)

from eda.analysis import (
    median_group,
    iqr_group,
    standard_d,
    vote_rates,
    correlation_matrices
)

from eda.config import(
    approval_boxplot_config,
    rejection_boxplot_config,
    approval_heatmap_config,
    rejection_heatmap_config,
    grouped_barplot_config,
    stacked_barplot_config,
)

def main():
    ## Iniciar reporte del proyecto
    log_message(
        "Iniciando proyecto | \n Votaciones Primer Informe de Medioambiente - Nueva Constitución Chile 2022 \n", separator=True
    )
    
    ## Carga el archivo excel
    data = load_excel('data/raw/voto_medioambiente2022.xlsx')
    
    ## Preparación de datos
    # Crea una copia del archivo excel para manipular
    data_copy = copy_sheets(data)  
    
    # Excluye hojas innecesarias 
    show_keys(data_copy)
    valid_data = exclude_sheets(data_copy, excluded_sheets=[
        'General',
        'Constituyente',
        'Tabla base'
        ]
    )
    
    # Une hojas validas en un solo Dataframe, agregando columna identificadora 
    dataframe = merge_sheets(data_copy, valid_data, "articulos", 0)
    show_head(dataframe)
    
    # Selecciona solo las columnas necesarias
    show_columns(dataframe)
    dataframe = select_columns(dataframe, (0, 7))
    
    # Renombra las columnas
    dataframe = rename_columns(
        dataframe,
        ["Artículos",
        "Nombre",
        "Colectivo",
        "Aprueba",
        "Rechaza",
        "Se Abstiene",
        "No Vota"]
        )
    show_columns(dataframe)
    
    ## Limpieza de datos
    # Excluye las categorias innecesarias
    show_value_counts(dataframe, "Colectivo")
    dataframe = exclude_categories(dataframe, "Colectivo", ["Inhabilitado"])
    
    # Resumen del DataFrame creado
    show_summary(dataframe,unique_cols=['Artículos', 'Nombre', 'Colectivo'])
    
    # Elimina valores duplicados
    dataframe = drop_dup(dataframe)
    
    # Cuenta los valores nulos y los rellena con 0
    dataframe = fill_nan(dataframe)
    
    ## Validación de datos
    # Crea una variable que incluya las columnas a validar y analizar
    vote_cols = ["Aprueba", "Rechaza", "Se Abstiene", "No Vota"]
    
    # Valida que los votos solo contengan valores [0] o [1]
    validate_votes(dataframe, vote_cols)
    
    # Actualiza los valores incorrectos en las columnas de votacion
    dataframe = update_value(dataframe, 4002, 'Aprueba', 1)
    dataframe = update_value(dataframe, 4006, 'Rechaza', 1)
    
    # Revalida que votos solo contengan valores [0] o [1]
    validate_votes(dataframe, vote_cols)
    
    # Valida la integridad de los votos
    validate_integrity(dataframe, vote_cols)
    
    ## Procesamiento de datos
    # Calcula las tasas de ocurrencia de las votaciones por nombre y colectivo
    votes_ratio = vote_rates(dataframe, "Nombre", "Colectivo", vote_cols)
    show_vote_rates(votes_ratio, "Colectivo", vote_cols, "Aprueba")
    
    # Calcula matrices de correlacion para cada tipo de voto por colectivo
    collective_correlation = correlation_matrices(dataframe, 'Artículos', 'Colectivo', vote_cols)
    
    # Guarda el DataFrame procesado en la carpeta data/processed
    output_path = generate_output_path(PROCESSED_DATA_DIR, 'medioambiente2022_processed.xlsx')
    save_dataframe(dataframe, output_path)
    
    
    ## EDA
    log_message(
        "Iniciando Analisis Exploratorio de Datos | \n", separator=True
    )
    
    # Calcula medidas de cohesion por colectivo
    iqr_results = iqr_group(votes_ratio, "Colectivo", vote_cols)
    standard_d_results = standard_d(votes_ratio, "Colectivo", vote_cols)
    median_results = median_group(votes_ratio, "Colectivo", vote_cols)
    show_cohesion(iqr_results, standard_d_results, median_results, "Aprueba")
    show_cohesion(iqr_results, standard_d_results, median_results, "Rechaza")
    
    # Visualizaciones 
    log_message(
        "Iniciando la creacion de visualizaciones 🎥 | \n", separator=True
    )
    
    # Crea barplots para visualizar la distribucion de votos por colectivo
    plot_factory(dataframe, "barplot", ["Colectivo", vote_cols], grouped_barplot_config)
    plot_factory(dataframe, "barplot", ["Colectivo", vote_cols], stacked_barplot_config)
    
    # Crea boxplots para visualizar la cohesion de los votos de aprueba, rechaza y comparaciones de votos por colectivo
    plot_factory(votes_ratio, "boxplot", ["Colectivo", "Aprueba"], approval_boxplot_config)
    plot_factory(votes_ratio, "boxplot", ["Colectivo", "Rechaza"], rejection_boxplot_config)
    
    # Crea heatmaps para visualizar la correlacion de los votos aprueba y rechaza por colectivo
    plot_factory(collective_correlation["Aprueba"], "heatmap", None, approval_heatmap_config)
    plot_factory(collective_correlation["Rechaza"], "heatmap", votes_ratio, rejection_heatmap_config)
    
    log_message(
        "Análisis finalizado | \n Votaciones Primer Informe de Medioambiente - Nueva Constitución Chile 2022 \n", separator=True
    )
    
if __name__ == '__main__':
    main()
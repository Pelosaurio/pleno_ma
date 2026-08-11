from .show_title import show_title
from .show_separator import show_separator

def show_cohesion(iqr, standard_d, median, value_column):
    """
    Muestra medidas de cohesion interna para un tipo de voto.
    
    Args:
        median (DataFrame)
        iqr (DataFrame)
        standard_d (DataFrame)
        value_column (str)
    
    Returns:
        None
    """
    
    cohesion = (
        iqr[[value_column]]
        .rename(columns={value_column: "Rango intercuartil"})
        .join(
            standard_d[[value_column]].rename(
                columns={value_column: "Desv. estándar"}
            )
        )
        .join(
            median[[value_column]].rename(
                columns={value_column: "Mediana"}
            )
        )
        .sort_values("Rango intercuartil", ascending=True)
    )
    
    show_title(f"Cohesión interna por colectivo — {value_column}")
    
    print(cohesion.to_string(float_format="%.2f"))
    
    print()
    
    show_separator()
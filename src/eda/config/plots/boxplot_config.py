from ..path import BOXPLOT_DIR
from .colors import (
    approval_camara, 
    approval_modern, 
    rejection_camara, 
    rejection_modern,
    abstain_camara,
    abstain_modern,
    no_vote_camara,
    no_vote_modern)

default_boxplot_config = {
    "title": None,
    "xlabel": None,
    "ylabel": None,
    "figsize":(12, 6),
    "sort_by": "median",
    "show_grid": True,
    "linestyle": "--",
    "alpha": 0.5,
    "format": "png",
    "dpi": 300,
    "showfliers": True,
    "width": 0.6,
    "linewidth": 1,
    "boxprops": None,
    "medianprops": {"color": "black","linewidth": 2},
    "whiskerprops": {"color": "black"},
    "capprops": {"color": "black"},
    "flierprops": {"marker": "o", "markerfacecolor": "black", "markeredgecolor": "white", "markersize": 5},
    "output_dir": BOXPLOT_DIR,
}

approval_boxplot_config ={
    **default_boxplot_config,
    "title": "Cohesión de votaciones de Aprobación por Colectivo",
    "xlabel": "Tasa de aprobación (%)",
    "ylabel": "Colectivos",
    "column": "Aprueba",
    "boxprops": {"facecolor": approval_camara, "edgecolor": "black", "linewidth": 1},
    "filename": "approval_boxplot.png"
}

rejection_boxplot_config = {
    **default_boxplot_config,
    "title": "Cohesión de votaciones de Rechazo por colectivo",
    "xlabel": "Tasa de rechazo (%)",
    "ylabel": " Colectivos",
    "column":"Rechaza",
    "boxprops": {"facecolor": rejection_camara, "edgecolor": "black", "linewidth": 1},
    "filename": "rejection_boxplot.png"
}

abstains_boxplot_config = {
    **default_boxplot_config,
    "title": "Cohesión de votaciones de Abstencion por colectivo",
    "xlabel": "Tasa de abstención(%)",
    "ylabel": "Colectivos",
    "column": "Se Abstiene",
    "boxprops": {"facecolor": abstain_modern, "edgecolor": "black", "linewidth": 1},
    "filename": "abstains_boxplot.png"
}

no_vote_boxplot_config = {
    **default_boxplot_config,
    "title": "Cohesión de No Votar por colectivo",
    "xlabel": "Tasa de no voto (%)",
    "ylabel": "Colectivos",
    "column": "No Vota",
    "boxprops": {"facecolor": no_vote_modern, "edgecolor": "black", "linewidth": 1},    
    "filename": "no_vote_boxplot.png"
}
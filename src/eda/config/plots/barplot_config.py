from ..path import BARPLOT_DIR
from .colors import (vote_colors_camara, vote_colors_modern)

default_barplot_config = {
    "title": None,
    "xlabel": None,
    "ylabel": None,
    "figsize": (12, 6),
    "sort_column": None,
    "ascending": False,
    "palette": None,
    "legend_loc": "upper left",
    "legend_bbox": (1.02, 1),
    "show_grid": True,
    "linestyle": "--",
    "alpha": 0.5,
    "format": "png",
    "dpi": 300,
    "edgecolor": "black",
    "linewidth": 1,
    "output_dir": BARPLOT_DIR,
}

grouped_barplot_config = {
    **default_barplot_config,
    "title": "Distribución de votaciones por Colectivo",
    "ylabel": "Tasa de votación (%)",
    "xlabel": "Colectivos",
    "sort_column": "Aprueba",
    "ascending": False,
    "palette": vote_colors_camara,
    "filename": "grouped_votes_barplot.png",
    "stacked": False
}

stacked_barplot_config = {
    **default_barplot_config,
    "title": "Distribución de votaciones por Colectivo (apilado)",
    "ylabel": "Tasa de votación (%)",
    "xlabel": "Colectivos",
    "sort_column": "Rechaza",
    "ascending": False,
    "palette": vote_colors_modern,
    "filename": "stacked_votes_barplot.png",
    "stacked": True
}

from ..path import HEATMAP_DIR
from .colors import (cmap_general, cmap_accessible)

default_heatmap_config = {
    "title": None,
    "annot": True,
    "fmt": ".1f",
    "cmap": None,
    "cbar": True,
    "figsize": (12, 10),
    "format": "png",
    "dpi": 300,
    "output_dir": HEATMAP_DIR
}

approval_heatmap_config = {
    **default_heatmap_config,
    "title": "Correlación de votos de Aprueba entre colectivos",
    "cmap": cmap_general,
    "filename": "approval_heatmap.png",
}

rejection_heatmap_config = {
    **default_heatmap_config,
    "title": "Correlación de votos de Rechaza entre colectivos",
    "cmap": cmap_accessible,
    "filename": "rejection_heatmap.png",
}

abstains_heatmap_config = {
    **default_heatmap_config,
    "title": "Correlación de votos de Abstención entre colectivos",
    "filename": "abstains_heatmap.png",
}

no_vote_heatmap_config = {
    **default_heatmap_config,
    "title": "Correlación de NO participación entre colectivos",
    "filename": "no_vote_heatmap.png",
}
from .barplot_config import (
    default_barplot_config,
    grouped_barplot_config,
    stacked_barplot_config
)

from .boxplot_config import (
    default_boxplot_config,
    approval_boxplot_config,
    rejection_boxplot_config,
    abstains_boxplot_config,
    no_vote_boxplot_config,
)

from .heatmap_config import (
    default_heatmap_config,
    approval_heatmap_config,
    rejection_heatmap_config,
    abstains_heatmap_config,
    no_vote_heatmap_config,
)

from .colors import (
    vote_colors_camara,
    vote_colors_modern,
    approval_camara,
    approval_modern,
    rejection_camara,
    rejection_modern,
    abstain_camara,
    abstain_modern,
    no_vote_camara,
    no_vote_modern,
    cmap_general,
    cmap_accessible,
)

__all__ = [
    "default_boxplot_config",
    "approval_boxplot_config",
    "rejection_boxplot_config",
    "abstains_boxplot_config",
    "no_vote_boxplot_config",
    "default_heatmap_config",
    "approval_heatmap_config",
    "rejection_heatmap_config",
    "abstains_heatmap_config",
    "no_vote_heatmap_config",
    "default_barplot_config",
    "grouped_barplot_config",
    "stacked_barplot_config",
    "vote_colors_camara",
    "vote_colors_modern",
    "approval_camara",
    "approval_modern",
    "rejection_camara",
    "rejection_modern",
    "abstain_camara",
    "abstain_modern",
    "no_vote_camara",
    "no_vote_modern",
    "cmap_general",
    "cmap_accessible",
]
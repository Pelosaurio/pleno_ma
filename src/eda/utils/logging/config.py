from ...config.path.paths import LOGS_DIR
from .. import generate_output_path

LOG_PATH = generate_output_path(
    LOGS_DIR,
    "audit_log.txt"
)
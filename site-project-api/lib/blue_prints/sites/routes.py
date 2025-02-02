from flask import Blueprint
from .get_all_sites import process_get_all_sites

sites_bp = Blueprint(
    'sites_bp', __name__
    # Might be more useful for the site plans and certificates
    # template_folder='templates',
    # static_folder='static'
)

@sites_bp.route('/api/sites', methods=['GET'])
def get_all_sites():
    return process_get_all_sites()

from flask import Blueprint
from .create_tables_and_seed import process_create_tables_and_seed
from .delete_all_tables import process_delete_all_tables

create_tables_and_seed_bp = Blueprint(
    'create_tables_and_seed_bp', __name__
    # Might be more useful for the site plans and certificates
    # template_folder='templates',
    # static_folder='static'
)



@create_tables_and_seed_bp.route('/api/createAndSeed', methods=['GET'])
def create_and_seed():
    return process_create_tables_and_seed()

@create_tables_and_seed_bp.route('/api/createAndSeed', methods=['DELETE'])
def delete_tables():
    return process_delete_all_tables()
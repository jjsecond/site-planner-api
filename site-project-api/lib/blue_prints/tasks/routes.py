from flask import Blueprint
from .get_all_tasks_by_plot_id import process_get_all_tasks_by_plot_id


# Defining a blueprint
tasks_bp = Blueprint(
    'tasks_bp', __name__
    # Might be more useful for the site plans and certificates
    # template_folder='templates',
    # static_folder='static'
)

@tasks_bp.route('/api/tasks', methods=['GET'])
def get_all_task_by_plot_id():
    return process_get_all_tasks_by_plot_id()
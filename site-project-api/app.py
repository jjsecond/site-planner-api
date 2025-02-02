from flask import Flask
from flask_cors import CORS
from lib.blue_prints.tasks.routes import tasks_bp 
from lib.blue_prints.sites.routes import sites_bp
from lib.blue_prints.create_tables_and_seed.routes import create_tables_and_seed_bp


app = Flask(__name__)


# Not blocking postman
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

# task
app.register_blueprint(tasks_bp)

# sites
app.register_blueprint(sites_bp)

# create and seed
app.register_blueprint(create_tables_and_seed_bp)

if __name__ == '__main__':
    # debug mode will restart when we make changes
    app.run(debug=True)
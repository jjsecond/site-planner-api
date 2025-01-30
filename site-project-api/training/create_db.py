# TODO: Delete when new app is working

from index import app, db

with app.app_context():
    db.create_all()

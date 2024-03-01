from flask import current_app
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def drop_db(app):
    with app.app_context():
        db.drop_all()

@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db(current_app)
    click.echo("Initialized the database.")

@click.command("drop-db")
@with_appcontext
def drop_db_command():
    drop_db(current_app)
    click.echo("Dropped the database.")

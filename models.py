"""Demo file showing off a model for SQLAlchemy."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement = True)

    name = db.Column(db.String(20),
                     nullable = False)

    species = db.Column(db.Text, 
                    nullable = False)

    photo_url = db.Column(
                    db.String(200), 
                    default='https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif'
                    )

    age = db.Column(db.Float,
                    nullable = True)

    notes = db.Column(db.Text,
                    nullable = True)
                    
    available = db.Column(db.Boolean,
                    default = True)


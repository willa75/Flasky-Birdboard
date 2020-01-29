from lib.util_sqlalchemy import ResourceMixin
from birdboard.extensions import db, marshmallow


class Project(ResourceMixin, db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50))
    description = db.Column(db.String())

from application import db

class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    month = db.Column(db.String(3), nullable=False)
    build = db.Column(db.String(100), nullable=False)
from application import db

class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    month = db.Column(db.String(20))
    build = db.Column(db.String(100))
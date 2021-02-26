from application import db
from application.models import Travel

db.drop_all()
db.create_all()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#setting up flasql config(response params and route)
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

#route with password auth (worked once for importing tables)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/louis:admin@localhost/flasql' #tried/worked

#route with no password (authtype=trusted)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flasql' #tried

#'flask run' params, development doesn't seem to work as according to documentation (it should update page on file save, not page refresh)
app.config['FLASK_ENV'] = 'development'
app.config['FLASK_APP'] = 'api.py'

#how our file 'gets' the sql db
db = SQLAlchemy(app)

#table 'widgets'
class Widget(db.Model):
  __tablename__ = 'widgets'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, unique=True, nullable=False)
  wodgets = db.Column(db.Integer)
  quantity = db.Column(db.Integer)

  def as_dict(self):
    return {
      id: "self.id",
      name: "self.name",
      wodgets: "self.wodgets",
      quantity: "self.quantity"
    }

  def __repr__(self):
    return(f'Widget(id={self.id}, name="{self.name}", wodgets="{self.wodgets}", quantity={self.quantity}')

































# from sqlalchemy import Column, Integer, String, Sequence, create_engine
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# engine = create_engine('postgresql://localhost/sqlalchemy_test', echo=True)


# class Widget(Base):
#   __tablename__: 'widgets'

#   id = Column(Integer, Sequence('widget_id_seq'), primary_key=True)
#   name = Column(String, unique=True, nullable=False)
#   wodgets = Column(Integer)
#   quantity = Column(Integer)

#   def __repr__(self):
#     return(f'Widget(id={self.id}, name="{self.name}", wodgets="{self.wodgets}", quantity={self.quantity}')


# Base.metadata.create_all(engine)
from models import app, Widget
from flask import jsonify, request


#default route with simple json response
@app.route('/')
def home():
  return jsonify(message='what the?!')

#responds with first widget in db
@app.route('/firstWidget')
def get_first_widget():
  first_widget = Widget.query.first()
  print(f'PINGGGG {first_widget}')
  return jsonify(widget=first_widget.as_dict())

#copied from Sarah's notes
#responds with list of all widgets
@app.route('/widgets', methods=['GET', 'POST'])
def user_index_create():
  if request.method == 'GET':
    return get_all_widgets()
  else:
    return jsonify(message='route coming soon')


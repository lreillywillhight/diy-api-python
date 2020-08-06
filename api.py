from models import app, Widget
from flask import jsonify, request



@app.route('/')
def home():
  return jsonify(message='what the?!')


@app.route('/randomWidget')
def random_widget():
  first_widget = Widget.query.first()
  print(f'PINGGGG {first_widget}')
  return jsonify(widget=first_widget.as_dict())


@app.route('/widgets', methods=['GET', 'POST'])
def user_index_create():
  if request.method == 'GET':
    return get_all_users()
  else:
    return jsonify(message='route coming soon')


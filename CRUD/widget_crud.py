from flask import jsonify
from models import User, as_dict


#copied from sarah's class notes

#list of all widgets from postgres db
def get_all_widgets():
  all_widgets = Widget.query.all()
  results = []
  for widget in all_widgets:
    results.append(widget.as_dict())
    return jsonify(results)
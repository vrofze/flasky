from . import api
from flask import jsonify

@api.route('/posts/')
def get_posts():
    return jsonify({'posts': '123'})

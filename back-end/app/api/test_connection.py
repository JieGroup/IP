from __future__ import annotations

from app.api import api

from app.utils.api import handle_response


@api.route('/testing_get', methods=['GET'])
@handle_response
def testing_get():

    print('jinlaileshabi')
    return 'test successfully!'

@api.route('/testing_get_exception', methods=['GET'])
@handle_response
def testing_get_exception():
    a = {}
    a['5']
    return 'test successfully!'

@api.route('/testing_post', methods=['POST'])
@handle_response
def testing_post():
    return 'test successfully!'

@api.route('/testing_post_exception', methods=['POST'])
@handle_response
def testing_post_exception():
    a = {}
    a['5']
    return 'test successfully!'
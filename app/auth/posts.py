from . import auth

@auth.route('/test')
def test():
    return 'test'


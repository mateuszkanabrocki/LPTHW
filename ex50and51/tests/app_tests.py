from nose.tools import *
from app import app

# set TESTING=True - make it easier to debug
app.config['TESTING'] = True
# make requests to the app without running the server
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert_equal(rv.status_code, 404)

    rv = web.get('/hello', follow_redirects=True)
    assert_equal(rv.status_code, 200)
    # rv.data -> return for get request
    assert_in(b"Fill Out This Form", rv.data)

    data = {'name': 'Zed', 'greet': 'Hola'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert_in(b"Zed", rv.data)
    assert_in(b"Hola", rv.data)

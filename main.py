# examples/things.py

from wsgiref.simple_server import make_server
from routes import Router

import falcon

# falcon.App instances are callable WSGI apps
# in larger applications the app is created in a separate file
app = application = falcon.App()

# Routes definitions
router = Router(app)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()
from app.livros import LivrosResource
from app.criticas import CriticasResource

class Router():

    def __init__(self, app):
        # livros [GET][POST]
        app.add_route('/livros', LivrosResource())

        # criticas [GET][POST]
        app.add_route('/livros/{livro_id}/criticas', CriticasResource())
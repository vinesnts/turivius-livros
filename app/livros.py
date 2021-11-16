import falcon
import json
import traceback

from db.db import connect
from db import query

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class LivrosResource:
    def on_get(self, req, resp):
        try:
            with connect().cursor() as cursor:
                cursor.execute(query.select_livros())
                livros = cursor.fetchall()
                
                resp.status = falcon.HTTP_200
                resp.text = json.dumps({
                    "status": True,
                    "payload": livros,
                    "error": None, 
                })

        except Exception as e:
            traceback.print_exc()
            resp.status = falcon.HTTP_500
            resp.text = json.dumps({
                "status": False,
                "payload": None,
                "error": "Erro no servidor", 
            })

    def on_post(self, req, resp):
        try:
            body = req.media
            titulo = body["titulo"]
            autor = body["autor"]
            resumo = body["resumo"]

            with connect().cursor() as cursor:
                cursor.execute(
                    query.insert_livros(), [titulo, autor, resumo])
                livro_id = cursor.fetchone()
                cursor.execute("commit;")
                
                if not livro_id:
                    resp.status = falcon.HTTP_500
                    resp.text = json.dumps({
                        "status": False,
                        "payload": None,
                        "error": f"Erro no servidor", 
                    })
                    return

                resp.status = falcon.HTTP_200
                resp.text = json.dumps({
                    "status": True,
                    "payload": livro_id,
                    "error": None, 
                })

        except KeyError as e:
            traceback.print_exc()
            resp.status = falcon.HTTP_400
            resp.text = json.dumps({
                "status": False,
                "payload": None,
                "error": f"O atributo {e} é obrigatório", 
            })

        except Exception:
            traceback.print_exc()
            resp.status = falcon.HTTP_500
            resp.text = json.dumps({
                "status": False,
                "payload": None,
                "error": "Erro no servidor", 
            })
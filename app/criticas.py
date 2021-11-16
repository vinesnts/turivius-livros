import falcon
import json
import traceback
import psycopg2

from db.db import connect
from db import query

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class CriticasResource:
    def on_get(self, req, resp, livro_id):
        try:
            if not livro_id:
                raise KeyError('livro_id')

            with connect().cursor() as cursor:
                cursor.execute(query.select_criticas(), [livro_id])
                criticas = cursor.fetchall()
                
                resp.status = falcon.HTTP_200
                resp.text = json.dumps({
                    "status": True,
                    "payload": criticas,
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

        except Exception as e:
            traceback.print_exc()
            resp.status = falcon.HTTP_500
            resp.text = json.dumps({
                "status": False,
                "payload": None,
                "error": "Erro no servidor",
            })

    def on_post(self, req, resp, livro_id):
        try:
            body = req.media
            texto = body["texto"]
            autor = body["autor"]

            if not livro_id:
                raise KeyError('livro_id')

            with connect().cursor() as cursor:
                cursor.execute(
                    query.insert_criticas(), [texto, autor, livro_id])
                critica_id = cursor.fetchone()
                cursor.execute("commit;")
                
                if not critica_id:
                    resp.status = falcon.HTTP_500
                    resp.text = json.dumps({
                        "status": False,
                        "payload": None,
                        "error": "Erro no servidor", 
                    })
                    return

                resp.status = falcon.HTTP_200
                resp.text = json.dumps({
                    "status": True,
                    "payload": critica_id,
                    "error": None, 
                })

        except psycopg2.IntegrityError as e:
            traceback.print_exc()
            resp.status = falcon.HTTP_404
            resp.text = json.dumps({
                "status": False,
                "payload": None,
                "error": "O livro não existe", 
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
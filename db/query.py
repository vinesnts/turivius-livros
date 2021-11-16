
def insert_livros():
    query = """
        insert into public.livros (
            titulo, autor, resumo
        ) values (%s, %s, %s)
        returning id;
    """
    return query

def select_livros():
    query = """
        select
            id, titulo, autor, resumo
        from public.livros;
    """
    return query

def insert_criticas():
    query = """
        insert into public.critica (
            texto, autor, livro_id
        ) values (%s, %s, %s)
        returning id;
    """
    return query

def select_criticas():
    query = """
        select 
            id, texto, autor, livro_id
        from public.critica
        where livro_id = %s;
    """
    return query
CREATE DATABASE turivius
WITH 
OWNER = vinesnts
ENCODING = 'UTF8'
LC_COLLATE = 'pt_BR.UTF-8'
LC_CTYPE = 'pt_BR.UTF-8'
TABLESPACE = pg_default
CONNECTION LIMIT = -1;

CREATE TABLE IF NOT EXISTS public.livros
(
    titulo character varying NOT NULL,
    autor character varying NOT NULL,
    resumo text NOT NULL,
    id serial NOT NULL,
    PRIMARY KEY (id)
);

ALTER TABLE public.livros
    OWNER to vinesnts;

CREATE TABLE IF NOT EXISTS public.critica
(
    id serial NOT NULL,
    livro_id integer NOT NULL,
    texto text NOT NULL,
    autor character varying NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT livro_id_fk FOREIGN KEY (livro_id)
        REFERENCES public.livros (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

ALTER TABLE public.critica
    OWNER to vinesnts;
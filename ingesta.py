import feedparser
from bs4 import BeautifulSoup
from config import fuente_rss

def buscador_noticias():
    noticias_varias = []
    for fuente in fuente_rss:
        feed = feedparser.parse(fuente['url'])
        for item in feed.entries:
            title = item.title
            link = item.link
            if 'published' in item:
                publicacion =item.published
            else:
                publicacion = None
            descripcion = [p.get_text() for p in BeautifulSoup( item.description, 'html.parser').find_all('p')]
            if 'content' in item and len(item.content) > 0:
                contenido = [p.get_text() for p in BeautifulSoup(item.content[0].value, 'html.parser').find_all('p')]
            else:
                contenido = [p.get_text() for p in BeautifulSoup(item.get('summary', ''), 'html.parser').find_all('p')]
            noticia = {
                "medio":fuente['nombre'],
                "seccion": fuente['seccion'],
                "titulo": title,
                "link":link,
                "publicacion": publicacion,
                "descripcion":" ".join(descripcion),
                "contenido": " ".join(contenido)
            }
            noticias_varias.append(noticia)

    return noticias_varias

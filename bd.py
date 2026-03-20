import sqlite3
from functions import limpiar_texto

def inicializar_db():
    try:
        conn = sqlite3.connect('noticias.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS noticias (link  PRIMARY KEY, medio TEXT, seccion TEXT, titulo TEXT, publicacion TEXT, descripcion TEXT, contenido TEXT, temas TEXT , score TEXT,procesada INTEGER)')
        conn.commit()
    except sqlite3.Error as e:
        print(f"ocurrio un error {e}")
    finally:
        if conn:
            conn.close()

def guardar_noticias(noticias):
    try:
        conn = sqlite3.connect('noticias.db')
        cursor = conn.cursor()
        if noticias:
            for n in noticias:
                link =limpiar_texto(n['link'])
                medio = limpiar_texto(n['medio'])
                seccion = limpiar_texto(n['seccion'])
                titulo =limpiar_texto(n['titulo'])
                publi = limpiar_texto(n['publicacion'])
                des =limpiar_texto(n['descripcion'])
                cont =limpiar_texto(n['contenido'])
                tema =None
                score = None
                procesado = 0
                cursor.execute('INSERT OR IGNORE INTO noticias VALUES (?,?,?,?,?,?,?,?,?,?)', (link, medio, seccion, titulo, publi, des, cont, tema, score, procesado))
            conn.commit()
    except sqlite3.Error as e:
        print(f"ocurrio un error {e}")
    finally:
        if conn:
            conn.close()
    
def insertar_tema(item):
    try:
        conn = sqlite3.connect('noticias.db')
        cursor = conn.cursor()
        if item['id']:
            id = item['id']
            temas = item['temas']
            score = item['score']
            cursor.execute('UPDATE noticias SET temas = ?, score = ?,  procesada = 1 WHERE link ==?', (temas, score, id))
            conn.commit()
    except sqlite3.Error as e:
        print(f"ocurrio un error {e}")
    finally:
        if conn:
            conn.close()

def obtener_noticias(link):
    noticia = None
    try:
        conn = sqlite3.connect('noticias.db')
        cursor = conn.cursor()
        if link:
            cursor.execute('SELECT medio, seccion, titulo, publicacion, descripcion, contenido, temas, link FROM noticias WHERE link = ?;', (link,))
            noticia = cursor.fetchall()
    except sqlite3.Error as e:
        print(f"ocurrio un error en conexión de bd")
    finally:
        if conn:
            conn.close()
    return noticia
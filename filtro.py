from sentence_transformers import SentenceTransformer, util
from config import temas, umbral

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
lista_nombre_temas = [t for t in temas.keys()]
lista_temas = [t for t in temas.values()]
vector_store= model.encode(lista_temas)


def filtrar_noticia(noticia):
    coincidencia = []
    #1. Realizar embedding a la noticia
    vector_noticia = model.encode(noticia)
    for index, v in enumerate(vector_store):
        cosine_scores = util.cos_sim(v, vector_noticia)
        if cosine_scores > umbral:
            resultado = {
                "index": index,
                "similitud": cosine_scores
            }
            coincidencia.append(resultado)
    resultado = [{"tema": lista_nombre_temas[i['index']], "similitud": i['similitud']} for i in coincidencia]
    
    return resultado



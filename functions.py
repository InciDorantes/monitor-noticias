import unicodedata

def limpiar_texto(texto):
    if texto:
        texto_norm = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('utf-8') 
        texto_sin_espacios = " ".join(texto_norm.split())
    else:
        texto_sin_espacios = None
    return texto_sin_espacios
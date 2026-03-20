from ingesta import buscador_noticias
from bd import inicializar_db, guardar_noticias, insertar_tema, obtener_noticias
from filtro import filtrar_noticia
from resumen import generar_resumen
from documento import generar_doc
import time
import json

#1. Buscar noticias
noticias_extrac = buscador_noticias()

noticias = []
links_vistos = set()
for n in noticias_extrac:
    if n['link'] not in links_vistos:
        links_vistos.add(n['link'])
        noticias.append(n)

#2. Guardar noticias
inicializar_db()
guardar_noticias(noticias)

#3. Filtrarlas
resultados_noticia=[]
resultado_general = []
for n in noticias:
    noti = n['contenido']
    desc = n['descripcion']
    if noti:
        r = filtrar_noticia(noti)
        temas = " ,".join([t['tema'] for t in r])
        score = ", ".join([str(t['similitud'].item()) for t in r])
        cont = n['contenido']
    elif desc:
        r = filtrar_noticia(desc)
        temas = " ,".join([t['tema'] for t in r])
        score = ", ".join([str(t['similitud'].item()) for t in r])
        cont = n['descripcion']
    else: 
        temas = None
        score = None
        cont = n
    res = {
            "id": n['link'],
            "temas": temas,
            "score":score,
            "contenido": cont
        }
    resultados_noticia.append(res)


with open("resultados_noticia.json", "w") as write_file:
    json.dump(resultados_noticia, write_file, indent=4)

#4. Noticias con coincidencia
resultados_filtrados = []

for res in resultados_noticia:
    if res['temas']:
        resultados_filtrados.append(res)

for res in resultados_filtrados:
    insertar_tema(res)

#5. De esas noticias con coincidencia buscar el top 5 
for r in resultados_filtrados:
    r['max_score'] = max([float(s) for s in r['score'].split(", ")])

sorted_resultados_filtrados= sorted(resultados_filtrados, key=lambda d: d['max_score'],reverse=True)

info_noticias_top_5 =[]

for r in sorted_resultados_filtrados[:5]:
    link = r['id']
    info_noticia = obtener_noticias(link)
    info_noticias_top_5.append(info_noticia)

#6. Hacer el resumen, darle la info a la IA
resumenes = []
for i in info_noticias_top_5:
    for j in i:
        noticia = j[5]
        resumen = generar_resumen(noticia)
        res_dict = {
            "id": j[7],
            "resumen": resumen
        }
        resumenes.append(res_dict)
        time.sleep(3)

#7. relacionar resumen con info
for i in sorted_resultados_filtrados:
    link = i['id']
    for j in resumenes:
        if j['id'] == link:
            i['resumen'] = j['resumen']
            break
    else:
        i['resumen'] = None
#8. Hacer el documento
generar_doc(sorted_resultados_filtrados)
#9. Enviarlo
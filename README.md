# 📰 Monitor de Noticias — Gobierno de Yucatán

Sistema automatizado de monitoreo de noticias políticas. Extrae noticias de medios locales via RSS, las filtra semánticamente por temas de interés, genera resúmenes con IA y produce un documento Word diario listo para consulta ejecutiva.

---

## ¿Qué hace?

1. **Ingesta** — Lee los feeds RSS de medios locales de Yucatán
2. **Almacenamiento** — Guarda las noticias nuevas en una base de datos local SQLite (sin duplicados)
3. **Filtro semántico** — Convierte cada noticia y los temas de interés en vectores (embeddings) y filtra por similitud coseno
4. **Resumen con IA** — Pasa el contenido completo de las 5 noticias más relevantes a Gemini para generar resúmenes ejecutivos
5. **Documento Word** — Produce un `.docx` con los resúmenes del top 5 y una lista del resto de noticias relevantes

---

## Tecnologías

- Python 3.13+
- Cuenta de Google AI Studio con API key de Gemini

---
## Estructura del proyecto

```
monitor-noticias/
├── main.py              # Punto de entrada, orquesta todo el flujo <br>
├── config.py            # Fuentes RSS, temas y umbral <br>
├── ingesta.py           # Lectura de feeds RSS <br>
├── bd.py                # Base de datos SQLite <br>
├── filtro.py            # Filtro semántico con embeddings<br>
├── resumen.py           # Generación de resúmenes con Gemini <br>
├── documento.py         # Generación del archivo Word <br>
├── functions.py         # Utilidades (limpieza de texto) <br>
├── requierments.txt     # Dependencias <br>
├── .env                 # API keys (no incluido en el repo) <br>
└── noticias.db          # Base de datos local (generada al correr) <br>
```

----

## Instalación y uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/monitor-noticias.git
cd monitor-noticias

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Instalar dependencias
pip install -r requierments.txt
```

---

## Configuración

Crea un archivo `.env` en la raíz del proyecto:

```
GEMINI_API_KEY=tu_api_key_aqui
```

Puedes obtener tu API key en [Google AI Studio](https://aistudio.google.com/).

---

## Configuración de fuentes y temas

Edita `config.py` para personalizar:

- **`fuente_rss`** — Lista de medios y secciones a monitorear
- **`temas`** — Descripciones semánticas de los temas de interés
- **`umbral`** — Sensibilidad del filtro (valor entre 0 y 1, default: 0.51)

---

## Uso

```bash
python main.py
```

Al terminar se generará el archivo `noticias.docx` en la raíz del proyecto con:

- **Top 5 noticias** más relevantes con resumen ejecutivo
- **Lista de otras noticias relevantes** con título, medio, fecha y liga

## Autora

Inci Dorantes Malpica
[LinkedIn](https://www.linkedin.com/in/inci-dorantes-malpica-366b131b9/) 
| [GitHub](https://github.com/InciDorantes)

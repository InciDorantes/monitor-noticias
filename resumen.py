from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=GEMINI_API_KEY)

def generar_resumen(noticia):
    prompt= f'''
    Eres asistente del Secretario de Comunicación social, y tienes la tarea se resumir las noticias seleccionadas 
    de tal manera en que el secretario puede leerlas rapido y logre obtener información valiosa de ella.
    Realiza el resumen de manera formal con coherencia, de no mas de 2 parrafos de 5 lineas cada uno, 
    resalta información negativa respecto al gobierno y si hay mención de presupuesto y montos mencionalas,  
    hazlo si inventar información. No incluyas saludos ni frases introductorias, ve directo al resumen, y solo usa la noticia: {noticia}
    '''
    response = None
    try:
        response = client.models.generate_content(
                model='gemini-3-flash-preview',
                contents=types.Part.from_text(text=prompt),
                config=types.GenerateContentConfig(
                    temperature=0,
                    top_p=0.95,
                    top_k=20,
                ),
            )
    except Exception as e:
        print(f"Hubo un error {e}")
        
    return response.text if response else "Error al generar el resumen"
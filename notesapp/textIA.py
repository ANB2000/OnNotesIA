"""Analisis de lenguaje natural"""
import spacy
from googleapiclient.discovery import build

def obtener_links_recomendacion(actividad):
    # Carga el modelo de lenguaje en español de spaCy
    nlp = spacy.load('es_core_news_sm')
    
    # Procesa el texto de la actividad con el modelo de spaCy
    doc = nlp(actividad)
    
    # Extrae palabras clave del texto (puedes ajustar esto según tus necesidades)
    palabras_clave = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ']]
    
    # Crea un objeto de servicio de la API de YouTube
    youtube = build('youtube', 'v3', developerKey='AIzaSyBtXfyvrRbMqcdZBSSCTcb0WySRLEpbiKA')
    
    # Define los parámetros de búsqueda para obtener recomendaciones basadas en las palabras clave
    search_term = ' '.join(palabras_clave)  # Convierte la lista de palabras clave en un solo string

    # Realiza la solicitud a la API de YouTube para buscar videos relacionados
    response = youtube.search().list(
        part='snippet',
        q=search_term,
        type='video',
        maxResults=4  # Número de videos recomendados que deseas obtener
    ).execute()

    # Extrae los ID de los videos recomendados
    video_ids = [item['id']['videoId'] for item in response['items']]

    # Genera los enlaces a los videos recomendados
    video_links = [f'https://www.youtube.com/watch?v={video_id}' for video_id in video_ids]

    return video_links

# Ejemplo de uso:
#ACTIVIDAD = 'correr los martes por la manana'
#links_recomendados = obtener_links_recomendacion(ACTIVIDAD)
#for link in links_recomendados:
 #   print(link)
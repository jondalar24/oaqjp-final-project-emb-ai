import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    # procesar la respuesta en formato json
    response_json = json.loads(response.text)
    emotions = response_json['emotionPredictions'][0]['emotion']
    # encontrar la emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)
    #formatear la respuesta
    formatted_response = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
    if response.status_code == 200:
        return formatted_response
    elif response.status_code == 400:
        return {
            'anger':None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
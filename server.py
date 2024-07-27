''' Executing this function initiates the application of emorion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods = ['GET'])
def sent_detection():
    """
    Esta función maneja las solicitudes GET a la ruta /emotionDetector, toma el texto
    para analizar de los argumentos de la solicitud, y devuelve una respuesta formateada
    con las emociones detectadas y la emoción dominante.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400
    response = emotion_detector(text_to_analyze)
    formatted_response = (
    f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
    f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
)
    return formatted_response

@app.route("/")
def render_index_page():
    """Esta función devuelve la página de inicio."""
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)

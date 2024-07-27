''' Executing this function initiates the application of emorion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods = ['GET'])
def sent_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        response = emotion_detector(text_to_analyze)
        formatted_response = (
            f"For the given statement, the system response is 'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
            f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
        )
        return formatted_response
    else:
        return "No text provided", 400

@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)
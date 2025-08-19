
from flask import Flask, request, url_for, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    text_to_analyze = request.args.get("textToAnalyze")
    print(text_to_analyze)
    emotions_detected = emotion_detector(text_to_analyze)

    if emotions_detected.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 200

    return render_template(
        'system_response.html',
        anger_score=emotions_detected.get('anger'), 
        disgust_score=emotions_detected.get('disgust'),
        fear_score=emotions_detected.get('fear'),
        joy_score=emotions_detected.get('joy'),
        sadness_score=emotions_detected.get('sadness'),
        dominant_emotion=emotions_detected.get('dominant_emotion')
    )

@app.route("/")
def index():
    url_for('static', filename='mywebscript.js')
    return render_template('index.html')    
    
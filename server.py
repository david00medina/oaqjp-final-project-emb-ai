"""
Flask app for emotion detection.

Defines two routes:
- "/" renders the main index page with the UI.
- "/emotionDetector" analyzes text and returns emotion results.
"""

from flask import Flask, request, url_for, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """
    Flask route that receives text from the query string, analyzes its emotions,
    and returns either an error message for invalid input or a rendered template
    displaying the detected emotion scores and the dominant emotion.
    """
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
    """
    Flask route for the home page.
    Renders the main index.html template, which loads the static JavaScript
    file (mywebscript.js) and provides the user interface for emotion detection.
    """
    url_for('static', filename='mywebscript.js')
    return render_template('index.html')
    
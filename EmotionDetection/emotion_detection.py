import requests
import json
from typing import Dict

def emotion_detector(text_to_analyse) -> Dict:
    """
        Extracts the emotions from the Watson NLP application
    """
    # Performs the call to Watson NLP API
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": { "text": text_to_analyse }}
    res = requests.post(url,headers=headers,json=payload)

    if res.status_code == 400:
        return {
            "anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None,
            "dominant_emotion": None
        }

    res_json = json.loads(res.text)

    # Transform the response into the requested output format
    emotion_predictions = res_json.get('emotionPredictions')
    emotions = list(map(lambda x: x.get('emotion'), emotion_predictions))[0]
    max_value = max(emotions.values())
    dominant_emotion = [k for k,v in emotions.items() if v == max_value][0]
    emotions['dominant_emotion'] = dominant_emotion
    return emotions

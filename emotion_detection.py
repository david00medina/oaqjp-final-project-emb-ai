import requests

def emotion_detector(text_to_analyse) -> str:
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": { "text": text_to_analyse }}
    res = requests.post(url,headers=headers,json=payload)
    return res.text
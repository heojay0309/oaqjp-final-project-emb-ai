import requests # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze: str):
    # URL of the emotion detection
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

        max_key = max(emotion_dict, key=emotion_dict.get)

        result_dict = {**emotion_dict, 'dominant_emotion': max_key}
    elif response.status_code == 400:
        result_dict = {"anger": None, "disgust": None, "fear": None, "joy": None, "sadness": None, "dominant_emotion": None}
        
    return result_dict

    
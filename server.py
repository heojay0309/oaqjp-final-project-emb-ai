''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retreive the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is {}.".format(response['anger'],response['disgust'],response['fear'],response['joy'],response['sadness'], response['dominant_emotion'])
        
        
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)

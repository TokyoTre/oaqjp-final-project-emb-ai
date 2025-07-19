"""
Flask web server for EmotionDetection application.

Handles POST requests to /emotionDetector endpoint,
calls the emotion_detector function,
and returns JSON responses with emotion analysis results.
"""

from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector as detect_emotion

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """
    Flask route handler for emotion detection POST requests.

    Expects JSON payload with 'text' key.

    Returns JSON with emotion scores and dominant emotion
    or an error message if input is invalid.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    result = detect_emotion(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    response_str = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({
        "result": response_str,
        "details": result
    })

if __name__ == '__main__':
    # Entry point of the Flask application.
    # Runs the server on host 0.0.0.0 and port 5000.
    app.run(host='0.0.0.0', port=5000)

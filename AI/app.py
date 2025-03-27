from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace with your actual DeepSeek API key
API_KEY = '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'
API_URL = 'https://api.deepseek.com/v1/chat'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'reply': 'No message provided'}), 400

    try:
        response = requests.post(API_URL, headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }, json={'message': user_message})
        
        if response.status_code != 200:
            return jsonify({'reply': f'Error: {response.status_code} {response.text}'}), response.status_code
        
        data = response.json()
        return jsonify({'reply': data.get('reply', 'No reply from AI')})
    except Exception as e:
        return jsonify({'reply': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
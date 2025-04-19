from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key="")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )
    reply = response.choices[0].message.content
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
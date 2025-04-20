from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import PyPDF2

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'message': 'No PDF file uploaded'}), 400
    
    pdf_file = request.files['pdf']
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = "".join(page.extract_text() for page in reader.pages)
    except Exception as e:
        return jsonify({'message': 'Error reading PDF file', 'error': str(e)}), 500

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are analyzing uploaded PDF files."},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({'message': reply})
    except Exception as e:
        return jsonify({'message': 'Error processing PDF with AI', 'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message}
            ]
        )
        reply = response.choices[0].message["content"]
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': 'Error processing the chat message', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
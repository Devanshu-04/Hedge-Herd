from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF

load_dotenv()

app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data['messages']

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    reply = response.choices[0].message.content
    return jsonify({'reply': reply})


@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    try:
        # Save file temporarily
        filepath = os.path.join("temp.pdf")
        file.save(filepath)

        # Extract text from PDF
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        if not text.strip():
            return jsonify({'message': 'Could not extract any text from the PDF.'}), 400

        # Send to OpenAI
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an assistant that analyzes PDF documents."},
                {"role": "user", "content": f"Analyze this PDF content:\n\n{text[:4000]}"}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({'message': reply})

    except Exception as e:
        print("PDF processing error:", e)
        return jsonify({'message': 'Error processing PDF'}), 500

if __name__ == '__main__':
    app.run(debug=True)

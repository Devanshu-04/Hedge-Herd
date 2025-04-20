from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF

# Load environment variables
load_dotenv()

# Flask setup
app = Flask(__name__)
CORS(app)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ========== ROUTE: Chat interaction ==========
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({'reply': reply})
    except Exception as e:
        print("Chat error:", e)
        return jsonify({'reply': 'There was an error processing your message.'}), 500

# ========== ROUTE: PDF Upload and Preview Summary ==========
@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'pdf' not in request.files:
        return jsonify({'message': 'No file uploaded.'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'message': 'No file selected.'}), 400

    try:
        # Step 1: Save temporary file
        temp_path = "temp.pdf"
        file.save(temp_path)

        # Step 2: Extract text from PDF
        with fitz.open(temp_path) as doc:
            text = "".join(page.get_text() for page in doc)

        if not text.strip():
            return jsonify({'message': 'PDF has no extractable text.'}), 400

        # Step 3: Generate concise preview
        preview_prompt = (
            "Summarize the key highlights from this PDF in **200 to 250 characters**. "
            "This is just a quick preview for the user:\n\n" + text[:4000]
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You summarize PDFs into short previews."},
                {"role": "user", "content": preview_prompt}
            ]
        )

        summary = response.choices[0].message.content.strip()
        return jsonify({'message': summary})

    except Exception as e:
        print("PDF processing error:", e)
        return jsonify({'message': 'Error processing PDF.'}), 500

# ========== Run the server ==========
if __name__ == '__main__':
    app.run(debug=True)

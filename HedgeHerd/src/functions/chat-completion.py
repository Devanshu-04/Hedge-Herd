from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app)

pdf_chunks = []

@app.route('/upload', methods=['POST'])
def upload_pdf():
    global pdf_chunks

    if 'pdf' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    try:
        file.save("temp.pdf")
        pdf_chunks = []
        with fitz.open("temp.pdf") as doc:
            for i, page in enumerate(doc):
                text = page.get_text().strip()
                if text:
                    pdf_chunks.append(f"[Page {i+1}]\n{text}")

        if not pdf_chunks:
            return jsonify({'message': 'PDF has no extractable text'}), 400

        return jsonify({'message': 'PDF successfully uploaded and processed.'}), 200
    except Exception as e:
        print("Upload error:", e)
        return jsonify({'message': 'Error processing PDF.'}), 500

@app.route('/chat', methods=['POST'])
def chat():
    global pdf_chunks
    data = request.get_json()
    messages = data.get('messages', [])

    if pdf_chunks:
        combined_text = ""
        for chunk in pdf_chunks:
            if len(combined_text) + len(chunk) < 12000:
                combined_text += "\n\n" + chunk
            else:
                break

        messages.insert(1, {
            "role": "system",
            "content": (
                "Here is a PDF document content. If asked, extract and compare total assets or other financial numbers "
                "for 2023 and 2024. Also, extract asset category breakdowns with their ₹ values separately for each year. "
                "Format values with '₹' and commas, and label as 'Assets for 2023' and 'Assets for 2024'.\n\n" + combined_text)
        })

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

if __name__ == '__main__':
    app.run(debug=True)

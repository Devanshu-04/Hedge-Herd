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

# Temporary PDF content cache
pdf_chunks = []

# ========== ROUTE: Chat interaction ==========
@app.route('/chat', methods=['POST'])
def chat():
    global pdf_chunks
    data = request.get_json()
    messages = data.get('messages', [])

    # Insert as much chunked text as token limits allow (~12,000 chars for GPT-4o)
    if pdf_chunks:
        # Concatenate up to X characters (to avoid hitting token limit)
        combined_text = ""
        for chunk in pdf_chunks:
            if len(combined_text) + len(chunk) < 100000:
                combined_text += "\n\n" + chunk
            else:
                break

        messages.insert(1, {
            "role": "system",
            "content": (
                "Here is content from a PDF the user uploaded. Use this to answer any questions about the content. "
                "Refer to page numbers when possible. If the information contains tables or structured data like a balance sheet, "
                "format it as an HTML table:\n\n" + combined_text)
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


# ========== ROUTE: PDF Upload and Preview Summary ==========
@app.route('/upload', methods=['POST'])
def upload_pdf():
    global pdf_chunks

    if 'pdf' not in request.files:
        return jsonify({'message': 'No file uploaded.'}), 400

    file = request.files['pdf']
    if file.filename == '':
        return jsonify({'message': 'No file selected.'}), 400

    try:
        # Save PDF temporarily
        temp_path = "temp.pdf"
        file.save(temp_path)

        # Extract and chunk
        pdf_chunks = []  # Reset previous
        with fitz.open(temp_path) as doc:
            for i, page in enumerate(doc):
                page_text = page.get_text().strip()
                if page_text:
                    pdf_chunks.append(f"[Page {i+1}]\n{page_text}")

        if not pdf_chunks:
            return jsonify({'message': 'PDF has no extractable text.'}), 400

        return jsonify({
            'message': 'PDF successfully uploaded and processed.',
            'chunks': pdf_chunks  # Include chunks in the response
        }), 200

    except Exception as e:
        print("PDF processing error:", e)
        return jsonify({'message': 'Error processing PDF.'}), 500



# ========== Run the server ==========
if __name__ == '__main__':
    app.run(debug=True)

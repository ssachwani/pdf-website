from flask import Flask, request, jsonify
import PyPDF2
import os

app = Flask(__name__)

# Simple PDF merger
@app.route('/merge', methods=['POST'])
def merge_pdfs():
    files = request.files.getlist('files')
    merger = PyPDF2.PdfMerger()
    
    for file in files:
        merger.append(file)
    
    output_path = 'merged.pdf'
    merger.write(output_path)
    merger.close()
    
    return jsonify({"download_link": f"/download/{output_path}"})

if __name__ == '__main__':
    app.run(debug=True)
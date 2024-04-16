from flask import Flask, request, redirect, url_for, render_template, flash
import os
import logging
from werkzeug.utils import secure_filename
import PyPDF2
from docx import Document
import nltk
from keybert import KeyBERT

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'docx', 'txt'}

logging.basicConfig(level=logging.INFO)
kw_model = KeyBERT()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = [page.extract_text() for page in reader.pages]
    return ' '.join(text)

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    return ' '.join([para.text for para in doc.paragraphs])

def extract_text_from_txt(txt_path):
    with open(txt_path, 'r') as file:
        return file.read()

def process_text(text):
    # KeyBERT extract_keywords method returns a list of tuples (keyword, score)
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', highlight=False)
    # We only want the keyword part of each tuple, not the score
    keyword_phrases = [keyword[0] for keyword in keywords]  # Extract just the keywords
    return ' '.join(keyword_phrases)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        text = request.form.get('text')

        if file and file.filename != '':
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                logging.info(f'File saved to {file_path}')
                
                # Extract text based on file type
                extension = filename.rsplit('.', 1)[1].lower()
                if extension == 'pdf':
                    extracted_text = extract_text_from_pdf(file_path)
                elif extension == 'docx':
                    extracted_text = extract_text_from_docx(file_path)
                elif extension == 'txt':
                    extracted_text = extract_text_from_txt(file_path)
                
                processed_text = process_text(extracted_text)
            else:
                flash('File type is not allowed.')
                return redirect(request.url)
        elif text:
            processed_text = process_text(text)
            logging.info('Text data processed.')
        else:
            flash('No file or text provided!')
            return redirect(request.url)

        return render_template('result.html', processed_text=processed_text)
    
    return render_template('upload_form.html')

@app.route('/success')
def success():
    return 'Upload Successful'

if __name__ == '__main__':
    app.run(debug=True)
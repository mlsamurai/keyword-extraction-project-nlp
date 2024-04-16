from flask import Flask, request, redirect, url_for, render_template, flash
import os
import logging
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'doc', 'txt'}

logging.basicConfig(level=logging.INFO)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def process_text(text):
    # Example of processing: reverse the text
    return text[::-1]

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
                # Assume the file text needs to be extracted or processed
                processed_text = f"Processed file saved at {file_path}"
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
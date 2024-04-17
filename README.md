# Keyword Extraction Web App 

<div align="center">
    <img src="images/example.png" alt="Example Image">
</div>

## Project Description
This project features a Flask-based web application designed for extracting keywords from uploaded text documents (PDF, DOCX, TXT) or direct text inputs. Utilizing the KeyBERT model, the app offers an intuitive interface for users to interact with advanced NLP keyword extraction technologies easily.

The project structure includes:
- A `code` directory containing the Flask application.
- A `tutorial` directory with Jupyter notebooks that provide a detailed examination of keyword extraction algorithms and explanations of the application code.

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mlsamurai/keyword_extraction.git
   cd keyword_extraction

2. **Navigate to the Code Directory**
   ```bash
   cd code

3. **Install Requirements**
    Ensure you have Python 3.6+ installed, then run:
    ```bash
    conda env create -f environment.yml
    conda activate nlp

## How to Run

1. **Start the Flask App**
   From the code directory, execute:
   ```bash
   python app.py
   ``` 

This will start the server locally on http://127.0.0.1:5000/.

2. **Access the Web Interface**
   Open a web browser and go to http://127.0.0.1:5000/ to start using the application.

## Tutorials

Explore the `tutorial` directory for notebooks:

- `Part 1. Algorithms.ipynb`: Breaks down various keyword extraction algorithms using the NIPS Papers dataset.
- `Part 2. Application.ipynb`: Contains a detailed walkthrough of the application code.

## References

- **KeyBERT**: Maarten Grootendorst. KeyBERT: Minimal keyword extraction with BERT. Available at [KeyBERT GitHub](https://maartengr.github.io/KeyBERT/).

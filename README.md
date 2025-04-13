# Text Summarization Tool

A web-based text summarization tool built with Streamlit and NLTK.

## Features

- Paste text or upload documents (TXT, DOCX)
- Adjustable summarization ratio
- Edit generated summaries
- Download summaries
- Clean and modern UI

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

```bash
streamlit run app.py
```

## Docker Setup

Build the container:
```bash
docker build -t text-summarizer .
```

Run the container:
```bash
docker run -p 8501:8501 text-summarizer
```

Access the application at: http://localhost:8501

## How it Works

The application uses an extractive summarization approach:
1. Tokenizes text into sentences
2. Removes stopwords
3. Calculates word frequencies
4. Scores sentences based on word importance
5. Selects top-scoring sentences
6. Preserves original sentence order

## Technologies Used

- Python
- Streamlit
- NLTK
- Docker
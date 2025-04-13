# Text Summarization Tool

A web-based text summarization tool built with Streamlit and NLTK.

## Features

- Paste text or upload documents (TXT, DOCX)
- Adjustable summarization ratio
- Edit generated summaries
- Download summaries
- Clean and modern UI

## Running with Docker

You can run this application in two ways:

### Option 1: Pull from Docker Hub
```bash
docker pull YOUR_DOCKERHUB_USERNAME/text-summarizer:latest
docker run -p 8501:8501 YOUR_DOCKERHUB_USERNAME/text-summarizer:latest
```

### Option 2: Build Locally
```bash
docker build -t text-summarizer .
docker run -p 8501:8501 text-summarizer
```

Access the application at: http://localhost:8501

## Running Locally Without Docker

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:
```bash
streamlit run app.py
```

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

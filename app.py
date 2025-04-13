import streamlit as st
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from heapq import nlargest
import docx
import io

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def read_docx(file):
    doc = docx.Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def summarize_text(text, ratio=0.3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize words and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calculate word frequencies
    freq = FreqDist(words)
    
    # Calculate sentence scores based on word frequencies
    scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq:
                if sentence not in scores:
                    scores[sentence] = freq[word]
                else:
                    scores[sentence] += freq[word]
    
    # Select top sentences
    select_length = max(1, int(len(sentences) * ratio))
    summary = nlargest(select_length, scores, key=scores.get)
    
    # Return summary in original order
    ordered_summary = [sent for sent in sentences if sent in summary]
    return ' '.join(ordered_summary)

def main():
    st.set_page_config(page_title="Text Summarizer", layout="wide")
    
    st.title("📝 Text Summarization Tool")
    st.write("Upload a document or paste text to generate a summary")
    
    # Input method selection
    input_method = st.radio("Choose input method:", ["Paste Text", "Upload File"])
    
    text_to_summarize = ""
    
    if input_method == "Paste Text":
        text_to_summarize = st.text_area("Enter your text here:", height=200)
    else:
        uploaded_file = st.file_uploader("Upload a file", type=['txt', 'docx'])
        if uploaded_file is not None:
            if uploaded_file.type == "text/plain":
                text_to_summarize = uploaded_file.getvalue().decode()
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text_to_summarize = read_docx(uploaded_file)
    
    # Summarization options
    col1, col2 = st.columns(2)
    with col1:
        ratio = st.slider("Summarization Ratio", 0.1, 0.5, 0.3, 0.1)
    
    if text_to_summarize:
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                summary = summarize_text(text_to_summarize, ratio)
                
                # Display original text and summary in columns
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Original Text")
                    st.write(text_to_summarize)
                    st.info(f"Original Length: {len(word_tokenize(text_to_summarize))} words")
                
                with col2:
                    st.subheader("Summary")
                    summary_edit = st.text_area("Edit summary if needed:", summary, height=300)
                    st.info(f"Summary Length: {len(word_tokenize(summary_edit))} words")
                    
                # Download options
                if st.button("Download Summary"):
                    st.download_button(
                        label="Download Summary",
                        data=summary_edit,
                        file_name="summary.txt",
                        mime="text/plain"
                    )

if __name__ == "__main__":
    main()
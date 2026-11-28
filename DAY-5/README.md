# Day 5 – Memory and RAG
## Project Overview
This project demonstrates a Retrieval-Augmented Generation (RAG) system that answers questions based on information extracted from PDF documents.
It uses document processing, text chunking, embeddings, and vector similarity search to retrieve relevant information and generate answers using an AI model.
## Features
- Extracts text from PDF documents.
- Uses OCR when text extraction is unavailable.
- Splits extracted text into smaller chunks.
- Generates sentence embeddings using Sentence Transformers.
- Stores embeddings using FAISS.
- Retrieves the top 3 relevant text chunks for a question.
- Generates answers using the Groq LLM.
## Technologies Used
- Python
- Google Colab
- PyMuPDF
- Tesseract OCR
- Sentence Transformers
- FAISS
- Groq API
## Workflow
1. Upload a PDF document.
2. Extract text from the PDF.
3. Apply OCR when required.
4. Split the text into chunks.
5. Generate embeddings for each chunk.
6. Store embeddings in a FAISS vector index.
7. Retrieve relevant chunks based on the user's question.
8. Generate an answer using the retrieved context.
## How to Run
1. Open the notebook in Google Colab.
2. Install the required libraries.
3. Add your Groq API key securely using Colab Secrets.
4. Upload your PDF document.
5. Run all notebook cells.
6. Ask questions about the uploaded PDF.
## Learning Outcomes
- Understanding Retrieval-Augmented Generation (RAG).
- Learning text extraction and OCR.
- Understanding text chunking and embeddings.
- Learning vector similarity search using FAISS.
- Connecting an LLM with retrieved document information.
## Project File
`Agent_AI_task_day_5.ipynb`

## Note
The vector index is stored in memory and is not persistent across runtime restarts. Answers should be checked against the original PDF.

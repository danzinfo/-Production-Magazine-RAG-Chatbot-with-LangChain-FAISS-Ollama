Production Magazine RAG Chatbot:

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from Production Magazine PDF and text archives using LangChain, FAISS, Hugging Face Embeddings, Ollama (Llama 3.2), and Streamlit. The application supports both text and AI voice responses for an interactive document question-answering experience.
```
Features
•	Load magazine content from PDF and TXT files 
•	Automatic document chunking using Recursive Character Text Splitter 
•	Generate semantic embeddings with sentence-transformers/all-MiniLM-L6-v2 
•	Fast similarity search using FAISS Vector Database 
•	Retrieval-Augmented Generation (RAG) powered by Llama 3.2 (Ollama) 
•	AI voice responses using Microsoft Edge TTS 
•	Interactive Streamlit web interface 
•	Metadata tracking for magazine source files 
•	MMR retrieval for better context diversity 
```
```
Project Workflow

Document Ingestion (ingest.py)

PDF/TXT Files
       │
       ▼
Document Loader
       │
       ▼
Text Chunking
       │
       ▼
Sentence Embeddings
       │
       ▼
FAISS Vector Index

```
```
The ingestion pipeline:
•	Reads all PDF and TXT files from the read_documents directory 
•	Extracts text while preserving source metadata 
•	Splits documents into overlapping chunks 
•	Creates semantic embeddings using Hugging Face 
•	Stores embeddings in a local FAISS vector database 
```
```
Chatbot Pipeline (chatbot.py)

User Question
      │
      ▼
Question Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Prompt Construction
      │
      ▼
Llama 3.2 (Ollama)
      │
      ▼
Answer Generation
      │
      ▼
Text + Voice Response
```
```
The chatbot:
•	Converts user questions into embeddings 
•	Retrieves the most relevant magazine content using FAISS 
•	Uses LangChain Retrieval Chain for context-aware answering 
•	Generates responses with Llama 3.2 
•	Speaks the generated answer using Microsoft Edge Text-to-Speech 
```
```
Technologies Used
•	Python 3.12 
•	LangChain 
•	Hugging Face Transformers 
•	FAISS 
•	Ollama 
•	Llama 3.2 
•	Streamlit 
•	Edge TTS 
•	Pygame

```
```
Project Structure

Production-Magazine-RAG/
│
├── read_documents/
│   ├── *.pdf
│   └── *.txt
│
├── faiss_index/
├── images/
│   └── banner.jpg
│
├── ingest.py
├── chatbot.py
├── requirements.txt
└── README.md
```

```
Sample Questions:

•	What is the name of the magazine for Vol-4 Issue-8 May 2019 edition? 
•	List the companies and CEOs featured in Cyber Security. 
•	Is there any profile related to Artificial Intelligence? 
•	Summarize an article from any magazine in 200 words. 
•	Explain the EIT Health cover story in APAC Business Headlines magazine. 
```
```
How It Works:

Step 1 – Build the Vector Database
python ingest.py
This creates the faiss_index from all magazine documents.
Step 2 – Launch the Chatbot
streamlit run chatbot.py
Open the Streamlit application in your browser and start asking questions about the magazine collection.
```
```
Use Cases:

•	Digital magazine search 
•	Enterprise knowledge retrieval 
•	Editorial content exploration 
•	Corporate document assistant 
•	AI-powered archive search 
•	Voice-enabled document Q&A 

```
```
Author
Daniel Chakravarthy
AI | Machine Learning | Generative AI | RAG Applications | Computer Vision | NLP

```

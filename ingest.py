from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


documents=[]

doc_path=Path("read_documents")

for file in doc_path.iterdir():

    if file.suffix.lower()==".pdf":

        loader=PyPDFLoader(str(file))
        docs=loader.load()

        for doc in docs:

            doc.metadata["source"]=file.name
        documents.extend(docs)

    
    elif file.suffix.lower()==".txt":

       loader=TextLoader(str(file),encoding="utf-8")
       docs=loader.load()

       for doc in docs:
           doc.metadata["source"]=file.name
       documents.extend(docs)

    print(f" {len(documents)} documents loaded")



splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)

chunk=splitter.split_documents(documents)

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vectorstore=FAISS.from_documents(chunk,embeddings)

vectorstore.save_local("faiss_index")

print("Faiss index created successfully..")




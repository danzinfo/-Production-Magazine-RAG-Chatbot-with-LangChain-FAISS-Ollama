from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain   #langchain-core=0.3.75 only supports
from langchain.chains.retrieval import create_retrieval_chain

import winsound
import asyncio
import edge_tts
import pygame
import tempfile
import os
import streamlit as st

async def speak(text):

    #Create a temporary mp3 file

    with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as fp:
        filename=fp.name

    #Generate Speech
    communicate=edge_tts.Communicate(text=text,voice="en-GB-RyanNeural")

    await communicate.save(filename)


    #Play audio

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

    pygame.mixer.quit()

    os.remove(filename)
    



#embedding
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#load Faiss vecror database
vectorstore=FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)

#retriever
retriever=vectorstore.as_retriever(search_type="mmr",search_kwargs={"k":5,"fetch_k":20})


#llm
llm=ChatOllama(model="llama3.2",temperature=0)


#propmt template

prompt=ChatPromptTemplate.from_template(

"""
You are a helpful AI Assistant.

Use only the provided context.

Context:
{context}

Question:
{input}

If answer is not found in context, say unable to answer

""")


#Document Chain

document_chain=create_stuff_documents_chain(llm,prompt)


#Retrieval Chain

rag_chain=create_retrieval_chain(retriever,document_chain)


# Display a full-width banner image
st.image("images/banner.jpg",use_container_width=False)
st.markdown("--------------------------------------------------------------------------------------------------------")
st.subheader("Magazine RAG Chatbot (Text and Voice Based Response)")
st.text("The Technology Headlines,(Hancock Media Pvt Ltd,Bangalore)")
st.text("The magazine names are 'The Technology Headlines & APAC Business Headlines' which is created and published. ")
st.markdown("--------------------------------------------------------------------------------------------------------")

question=st.text_input("\n **Few Magazines are only loaded which are created during the year 2019 to 2023..Ask any questions related to magazines:**")

#Chat Loop
if st.button("Submit"):

      if question.strip():

          with st.spinner("Searching..."):

            response=rag_chain.invoke( { "input": question })

          answer=response["answer"]

          #Beep Sound
          winsound.Beep(1000,500)
        
          st.subheader("Answer")
          st.write(answer)

          asyncio.run(speak(answer))

st.markdown("--------------------------------------------------------------------------------------------------------")
st.text("These are the sample questions you can ask related to the context: \n 1.what is the name of the magazine for Vol-4 Issue-8 May 2019 edition? \n 2.List out the name of the companies and CEOs featured in cyber security? \n 3.Is there any profile available about Artificial Intelligence. If yes list out?  \n 4.write any article from any magazine in 200 words? \n 5.Explain EIT Health cover story in Apac Business Headlines magazine?")
st.markdown("--------------------------------------------------------------------------------------------------------")
st.markdown("<h5>Project done by: Daniel Chakravarthy</h5>",unsafe_allow_html=True)


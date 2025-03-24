import os
from config import GROQ_API_KEY
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain.schema import HumanMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader, TextLoader

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'base_de_conhecimento.txt')

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

chat_model = init_chat_model("llama3-8b-8192", model_provider="groq")

def load_knowledge_base(path):
  embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
  
  if path.endswith('.pdf'):
    loader = PyPDFLoader(path)
  elif path.endswith('.txt'):
    loader = TextLoader(path)
  else:
    raise ValueError('Formato de arquivo não suportado')
  
  documents = loader.load()
  text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
  texts = text_splitter.split_documents(documents)
  
  vector_store = Chroma.from_documents(texts, embeddings)
  return vector_store


def main():
  knowledge_base = load_knowledge_base(file_path)
  
  st.title('Chatbot Technova')
  st.write('Chatbot para responder perguntas sobre a TechNova Solutions.')

  if 'messages' not in st.session_state:
    st.session_state.messages = []
    
  def submit_question():
    question = st.session_state.question_input
    if question:
      st.session_state.messages.append({ 'sender': 'user', 'text': question })
      st.session_state.question_input = ''
      
      relevant_docs = knowledge_base.similarity_search(question, k=3)
      context = '\n'.join([doc.page_content for doc in relevant_docs])
      prompt = f"Base de conhecimento:\n{context}\n\nPergunta: {question}\nResposta:"

      response = chat_model.invoke([HumanMessage(content=prompt)])
      answer = response.content
      st.session_state.messages.append({ 'sender': 'bot', 'text': answer })
    
  container = st.container()
  
  with container:
    for message in st.session_state.messages:
      if message['sender'] == 'user':
        st.markdown(f'**Você:** {message["text"]}')
      else:
        st.markdown(f'**Chatbot:** {message["text"]}')

  st.text_input(
    'Sua pergunta:',
    key='question_input',
    placeholder='Digite sua pergunta',
    on_change=submit_question
  )

if __name__ == '__main__':
  main()

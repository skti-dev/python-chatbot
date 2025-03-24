# Chatbot Technova

Este é um chatbot simples desenvolvido para responder perguntas sobre a TechNova Solutions(empresa fictícia). O chatbot utiliza a biblioteca Langchain e a API Groq para fornecer respostas baseadas em uma base de conhecimento.

## Estrutura do Projeto

chatbot_technova ├── base_de_conhecimento.txt ├── config.py ├── main.py ├── requirements.txt

- `base_de_conhecimento.txt`: Arquivo de texto contendo a base de conhecimento.
- `config.py`: Arquivo de configuração para carregar variáveis de ambiente.
- `main.py`: Arquivo principal que contém a lógica do chatbot.
- `requirements.txt`: Arquivo com as dependências do projeto.

## Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot_technova.git
cd chatbot_technova
```

2. Crie um ambiente virtual (se necessário):

```python-repl
python-mvenvvenvsourcevenv/bin/activate  # No Windows, use venv\Scripts\activate
```

3. Instale as dependências:

```python
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API Groq:

```
GROQ_API_KEY=your_groq_api_key
```

## Uso

1. Execute o aplicativo Streamlit:

**streamlit** **run** **main.py**

2. Abra o navegador e acesse `http://localhost:8501` para interagir com o chatbot.

## Personalização

- Para alterar a base de conhecimento, edite o arquivo `base_de_conhecimento.txt` ou substitua-o por um arquivo PDF.

> Desenvolvido por _Augusto Seabra_

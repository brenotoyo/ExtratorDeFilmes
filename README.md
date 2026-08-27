# 🎬 Extrator de Filmes

> Uma ferramenta que busca em um site os dados dos filmes, exibe em uma interface web e permite baixar os resultados em um arquivo CSV.

## 🚀 Sobre o Projeto
O **Extrator de Filmes** foi criado como forma de aprendizado e ganho de experiência na linguagem Python.
O projeto utiliza as bibliotecas `requests` e `BeautifulSoup` para buscar e formatar os dados de um catálogo de filmes,
com extração paralela via `concurrent.futures` para maior performance. Os dados extraídos são exibidos em uma
interface web construída com **Streamlit**, com opção de download em formato CSV.

### 🛠 Tecnologias
As principais ferramentas usadas na construção do projeto:
- [Python](https://www.python.org)
- [Streamlit](https://streamlit.io)
- [Requests](https://requests.readthedocs.io)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Pandas](https://pandas.pydata.org)

## ✨ Funcionalidades
- [x] Busca e extração de dados de filmes.
- [x] Extração paralela com múltiplas threads para maior velocidade.
- [x] Interface web interativa.
- [x] Exportação e download dos dados em arquivo CSV.

## 📦 Como rodar localmente

### Pré-requisitos
- [Python 3.8+](https://www.python.org/downloads/)
- pip (gerenciador de pacotes do Python)

### Bibliotecas utilizadas
- `streamlit`
- `requests`
- `beautifulsoup4`
- `pandas`

## Passo a passo

### 1. Clone o repositório
git clone https://github.com/brenotoyo/ExtratorDeFilmes.git
cd ExtratorDeFilmes

### 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Instale as dependências
pip install -r requirements.txt

### 4. Rode o app
streamlit run app.py

# 🎬 Extrator de filmes

> Uma ferramenta que busca em um site os dados dos filmes e salva em um arquivo csv.

## 🚀 Sobre o Projeto
O **Extrator de filmes** foi criado como forma de aprendizado e ganho de experiência na linguagem Python,
foi utilizado de biblicoteca como requests e BeautifulSoup para buscar e formatar os dados, então com 
estes dados extraidos, são escritos e salvos em um arquivo csv que é gerado após a extração.

### 🛠 Tecnologias
As principais ferramentas usadas na construção do projeto:
- [Python](https://www.python.org)

## ✨ Funcionalidades
- [x] Busca e extração de dados.
- [x] Escrita em arquivo csv.

## 📦 Como rodar 

### Pré-requisitos
- [Python 3.8+](https://www.python.org/downloads/)
- pip (gerenciador de pacotes do Python)

### Bibliotecas utilizadas:
- `requests`
- `beautifulsoup4`

### Passo a passo
# 1. Clone o repositório
git clone https://github.com/brenotoyo/ExtratorDeFilmes

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install requests beautifulsoup4

# 4. Rode o script
python main.py

# Imagem do  Python
FROM python:3.9-slim

# Pasta principal dentro do container onde ficaram os arquivos para execução do desafio
WORKDIR /desafioPismo

# Arquivo requirements.txt que contém as libs necessárias para execução dos arquivos python
COPY requirements.txt .

# Instalação das bibliotecas python
RUN pip install --no-cache-dir -r requirements.txt

# Cópia do código do desafio para o contêiner
COPY . .

# Comando para executar o código principal do projeto
CMD ["python", "src/main.py"]
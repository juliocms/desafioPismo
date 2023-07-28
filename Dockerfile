# Use uma imagem base do Apache Spark que já inclua o Java, como "bde2020/spark-base"
# FROM bde2020/spark-base:3.1.1-hadoop3.2
ARG IMAGE_VARIANT=slim-buster
ARG OPENJDK_VERSION=8
ARG PYTHON_VERSION=3.9.8

FROM python:${PYTHON_VERSION}-${IMAGE_VARIANT} AS py3
FROM openjdk:${OPENJDK_VERSION}-${IMAGE_VARIANT}

COPY --from=py3 / /

# RUN pip --no-cache-dir install pyspark

# Define o diretório de trabalho dentro do container
WORKDIR /app/scripts

# Copia o código fonte e os arquivos necessários para o diretório de trabalho
COPY src/ /app/src/
COPY data/ /app/data/
COPY scripts/ /app/scripts/
COPY requirements.txt /app/

# Instala as dependências do Pythonc
RUN pip install -r /app/requirements.txt


# Define o comando padrão que será executado quando o container for iniciado
# CMD ["python3", "/app/src/event_dispatcher.py"]
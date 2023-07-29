# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, year, month, dayofmonth
from pyspark.sql.types import TimestampType

import os

class EventDispatcher:
    def __init__(self):
        # Inicialização do SparkSession
        self.spark = SparkSession.builder.appName("DesafioPismo").getOrCreate()
       
    def load_events(self, data_input_folder):
        try:
            # Carrega os eventos em um DataFrame do Spark
            self.df = self.spark.read.json(data_input_folder, multiLine=True)
        except Exception as e:
            raise Exception(f"Erro ao carregar os eventos: {str(e)}")

    def transform_events(self):
        try:
            # Converte a coluna 'timestamp' para o tipo TimestampType
            self.df = self.df.withColumn("timestamp", col("timestamp").cast(TimestampType()))

            # Criar colunas de ano, mês e dia a partir da coluna "timestamp"
            self.df = self.df.withColumn("year", year(col("timestamp")))
            self.df = self.df.withColumn("month", month(col("timestamp")))
            self.df = self.df.withColumn("day", dayofmonth(col("timestamp")))

            # Renomeia o campo "data" para "data_temp" antes de aplicar a função from_json
            self.df = self.df.withColumn("data_temp", col("data"))

            # Mantém o campo "data_temp" como está (sem aplicar a função from_json)
            self.df = self.df.withColumn("data", col("data_temp"))

            # Remove o campo "data_temp"
            self.df = self.df.drop("data_temp")

            # As linhas duplicatas estão sendo removidas e está sendo mantido apenas 
            # a última versão de cada evento
            self.df = self.df.dropDuplicates(["event_id"]).orderBy("timestamp", ascending=False)
        except Exception as e:
            raise Exception(f"Erro ao transformar os eventos: {str(e)}")

    def save_events(self, data_output_folder):
        try:
            # Salva os eventos processados e cria as pastas de acordo com 
            # o tipo (domain + event_type) e realizando o particionando por data (ano/mês/dia)
            self.df.write.partitionBy("domain", "event_type", "year", "month", "day") \
                .parquet(data_output_folder, mode="overwrite")
        except Exception as e:
            raise Exception(f"Erro ao salvar os eventos: {str(e)}")

    def stop_spark_session(self):
        try:
            # Interrompe o SparkSession
            self.spark.stop()
        except Exception as e:
            raise Exception(f"Erro ao parar a sessão Spark: {str(e)}")

if __name__ == "__main__":
    data_input_folder = "../data/input/"
    data_output_folder = "../data/output/"
    
    event_dispatcher = EventDispatcher()
    event_dispatcher.load_events(data_input_folder)
    event_dispatcher.transform_events()
    event_dispatcher.save_events(data_output_folder)
    event_dispatcher.stop_spark_session()
  
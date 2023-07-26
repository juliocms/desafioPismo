import os
from pyspark.sql import SparkSession
# from event_dispatcher import event_dispatcher

def event_tests():
    
    # Inicia o SparkSession
    spark = SparkSession\
                .builder\
                .appName("DesafioPismoTest")\
                .getOrCreate()
                
    # Pasta com os arquivos de entrada para o teste
    data_input_events = "../data/input"
    
    # Carrega os arquivos json de entrada do teste para um Dataframe
    df = spark.read.json(data_input_events)
    
    # Pasta com os arquivos de saida dos eventso processados para o teste
    data_input_events = "../data/output"
    
    # Executa o dispatcher de eventos. É onde acontece a execução do desafio
    # event_dispatcher(blablabla)
    
    # Checa se os diretorios de saida foram criados
    # assert blablabla
    
    # Checa se os arquivos dos eventos foram particionados corretamente
    # assert blablabla
    
    # Interrompe o SparkSession
    spark.stop()
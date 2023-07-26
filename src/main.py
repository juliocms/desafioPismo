from pyspark.sql import SparkSession
from event_dispatcher import event_dispatcher

if __name__ == "__main__":
    
    # Inicialização do SparkSession
    spark = SparkSession.builder.appName("DesafioPismo").getOrCreate()
    
    # Pasta contendo os arquivos json de eventos
    data_input_folder = "../data/input/"

    # Carrega os eventos em um DataFrame do Spark
    df = spark.read.json(data_input_folder, multiLine=True)
    
    # Pasta contendo os arquivos dos eventos processados
    data_output_folder = "../data/output/"
    
    # Realiza a execução dos eventos
    # event_dispatcher(Blablabla)
    
    # Interrompe o SparkSession
    spark.stop()
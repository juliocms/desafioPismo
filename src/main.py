from pyspark.sql import SparkSession
from event_processor import process_events

if __name__ == "__main__":
    # Arquivo que vai iniciar e procesar os eventos
import pytest
from pyspark.sql import SparkSession
import sys

sys.path.insert(0, '../src')
from event_dispatcher import EventDispatcher

def test_load_events():
    # Cria uma instância da classe EventDispatcher
    event_dispatcher = EventDispatcher()

    # Folder com dados de entrada para os testes
    data_input_folder = "../data/input/"

    # Testa o método load_events se carrega os eventos corretamente
    try:
        event_dispatcher.load_events(data_input_folder)
    except Exception as e:
        pytest.fail(f"Erro ao carregar os eventos: {str(e)}")

def test_transform_events():
    # Cria uma instância da classe EventDispatcher
    event_dispatcher = EventDispatcher()

    # Folder com dados de entrada para os testes
    data_input_folder = "../data/input/"

    # Carrega os eventos para o teste
    event_dispatcher.load_events(data_input_folder)

    # Verifica se o método transform_events transforma os eventos corretamente
    try:
        event_dispatcher.transform_events()
    except Exception as e:
        pytest.fail(f"Erro ao transformar os eventos: {str(e)}")

def test_save_events():
    # Cria uma instância da classe EventDispatcher
    event_dispatcher = EventDispatcher()

    # Folder com dados de entrada e saída para os testes
    data_input_folder = "../data/input/"
    data_output_folder = "output/"

    # Carrega e transforma os eventos para o teste
    event_dispatcher.load_events(data_input_folder)
    event_dispatcher.transform_events()

    # Verifica se o método save_events salva os eventos corretamente
    try:
        event_dispatcher.save_events(data_output_folder)
    except Exception as e:
        pytest.fail(f"Erro ao salvar os eventos: {str(e)}")

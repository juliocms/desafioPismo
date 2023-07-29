from faker import Faker
import os
import json
import random

# Lib gerador de mocks
fake = Faker()

# Total de eventos a ser gerado
num_events = 50

# Total de eventos que devem se repetir
events_repeated = 5

# Total de eventos salvos na mesma data
events_same_date = 3

# Lista de domínios e tipos de eventos
domains = ["account", "transaction"]
event_types = ["status-change", "transfer"]

# Pasta para o mock de eventos gerados
data_input_folder = "../../data/input"

# Pasta onde ficarão os eventos gerados após execução do desafio
os.makedirs(data_input_folder, exist_ok=True)

# Função para criar um mock de evento
def event_skeleton():
    event_id = fake.uuid4()
    timestamp = fake.date_time_between(start_date='-1y', end_date='now')
    domain = random.choice(domains)
    event_type = random.choice(event_types)
    event_data = {
        "id": fake.random_int(min=1, max=1000),
        "old_status": fake.random_element(elements=("ACTIVE", "SUSPENDED", "PENDING")),
        "new_status": fake.random_element(elements=("ACTIVE", "SUSPENDED", "PENDING")),
        "reason": fake.sentence()
    }
    event = {
        "event_id": str(event_id),
        "timestamp": str(timestamp),
        "domain": domain,
        "event_type": event_type,
        "data": event_data
    }
    return event

from faker import Faker
import os
import random
import json

# Lib gerador de mocks
fake = Faker()

# Total de eventos a ser gerado
num_events = 50

# Total de eventos que devem se repetir
events_repeteated = 5

# Total de eventos salvos na mesma data
events_same_date = 3

# Lista de domínios e tipos de eventos
domains = ["account", "transaction"]
event_types = ["status-change", "transfer"]

# Pasta para o mock de eventos gerados
data_input_folder = "../../data/input"

# Pasta onde ficarão os eventos gerados após execução do desafio
os.makedirs(data_input_folder, exist_ok=True)

# Função para criar um mock de evento
def event_skeleton():
    event_id = fake.uuid4()
    timestamp = fake.date_time_between(start_date='-1y', end_date='now')
    domain = random.choice(domains)
    event_type = random.choice(event_types)
    event_data = {
        "id": fake.random_int(min=1, max=1000),
        "old_status": fake.random_element(elements=("ACTIVE", "SUSPENDED", "PENDING")),
        "new_status": fake.random_element(elements=("ACTIVE", "SUSPENDED", "PENDING")),
        "reason": fake.sentence()
    }
    event = {
        "event_id": str(event_id),
        "timestamp": str(timestamp),
        "domain": domain,
        "event_type": event_type,
        "data": event_data
    }
    return event

# Salva em arquivos de eventos no formato JSON na pasta de saída
for i in range(num_events):
    event = event_skeleton()
    output_file = os.path.join(data_input_folder, f"event_{i}.json")
    with open(output_file, "w") as f:
        json.dump(event, f, indent=2)
        
# Gera os eventos repetidos
event_repeteated = event_skeleton()
for i in range(num_events, num_events + events_repeated):
    output_file = os.path.join(data_input_folder, f"event_{i}.json")
    with open(output_file, "w") as f:
        json.dump(event_repeteated, f, indent=2)

# Eventos com a mesma data
same_date = fake.date_time_between(start_date='-1y', end_date='now')
for i in range(num_events + events_repeated, num_events + events_repeated + events_same_date):
    event = event_skeleton()
    event["timestamp"] = str(same_date)
    output_file = os.path.join(data_input_folder, f"event_{i}.json")
    with open(output_file, "w") as f:
        json.dump(event, f, indent=2)
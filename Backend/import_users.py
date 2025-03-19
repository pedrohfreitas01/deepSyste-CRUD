import json
from pymongo import MongoClient
from datetime import datetime

# Função para converter a data do formato string para timestamp
def convert_to_timestamp(date_str):
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ").timestamp()

# Conectando ao MongoDB
client = MongoClient("mongodb://localhost:27017")  # Conexão com o MongoDB
db = client["user_database"]  # Nome do banco de dados
users_collection = db["users"]  # Nome da coleção

# Lendo o arquivo JSON
with open('users_data.json', 'r') as file:
    data = json.load(file)

# Preparando os dados para inserir
users_data = []

for user in data['users']:
    user_obj = {
        "username": user['user'],
        "password": user['password'],
        "roles": [],
        "preferences": {
            "timezone": user['user_timezone']
        },
        "active": user['is_user_active'],
        "created_ts": convert_to_timestamp(user['created_at'])
    }

    # Atribuindo os roles baseado no JSON
    if user['is_user_admin']:
        user_obj['roles'].append('admin')
    if user['is_user_manager']:
        user_obj['roles'].append('manager')
    if user['is_user_tester']:
        user_obj['roles'].append('tester')

    users_data.append(user_obj)

# Inserindo os dados na coleção MongoDB
users_collection.insert_many(users_data)

print("Usuários importados com sucesso!")

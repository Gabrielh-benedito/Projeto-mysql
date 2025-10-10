import mysql.connector
from dotenv import load_dotenv
import os
# python -m pip install mysql-connector-python
#python -m pip install dotenv

#Carregar as variaveis de ambiente (.env)
load_dotenv()

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("DB_PASSWORD"),
            database="faculdade"
        )
        cursor = conexao.cursor()
        print("conexão estabelecida")
        return conexao, cursor
    except Exception as erro:
        print("Erro de conexão: {erro}")
        return None, None
    

    
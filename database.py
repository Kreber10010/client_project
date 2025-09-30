# database.py
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            database = os.getenv("DB_DATABASE")
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado ao servidor MYSQL: , versão: {db_info}")
            return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

#conn = connect_to_database("localhost", "root", "sua_senha", "nome_do_seu_banco")
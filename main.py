import os
import mysql.connector
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

def create_client(connection, nome, email, telefone, endereco):
    try:
        cursor = connection.cursor()
        sql_insert = "INSERT INTO clientes (nome, emai, telefone, endereco) VALUES (%s, %s, %s, %s)"
        client_data = (nome, email, telefone, endereco)

        cursor.execute(sql_insert, client_data)
        connection.commit()
        print(f"Cliente '{nome}' inserido com sucesso! ID: {cursor.lastrowid}")
        return True
    except mysql.connector.Error as e:
        print(f"Erro ao inserir cliente: {e}")
        connection.rollback()
        return False
        

def main():
    connection = connect_to_database()
    if connection:
        print("Conexão bem sucedida com o banco de dados!")

        # O código para inserir, ler, atualizar e deletar dados virá aqui.
        # Por exemplo: create_client(), get_all_clients(), etc.

        connection.close()
        print("Conexão com o MYSQL fechada!")
    else:
        print("Não foi possível conectar ao banco de dados. Verificar as credencias em .env.")

if __name__ == "__main__":
    main()
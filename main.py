import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import database

load_dotenv()

"""
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
"""

def create_customers_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS customers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            telefone VARCHAR(20),
            endereco VARCHAR(255),
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        print("Tabela 'clientes' verificada/criada com sucesso.")
        #cursor.execute("SHOW TABLES")
        return True
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("A tabela 'clientes' já existe.")
        else:
            print(f"Erro ao criar a tabela: {err}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
    """
    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela: {e}")
        connection.rollback()
        return False
    """



def create_customers(connection, nome, email, telefone, endereco):
    try:
        cursor = connection.cursor()
        sql_insert = "INSERT INTO customers (nome, email, telefone, endereco) VALUES (%s, %s, %s, %s)"
        customers_data = (nome, email, telefone, endereco)

        cursor.execute(sql_insert, customers_data)
        connection.commit()
        print(f"Cliente '{nome}' inserido com sucesso! ID: {cursor.lastrowid}")
        return True
    except mysql.connector.Error as e:
        print(f"Erro ao inserir cliente: {e}")
        connection.rollback()
        return False
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        

def main():
    connection = database.connect_to_database()
    if connection:
        print("Conexão bem sucedida com o banco de dados!")

        create_customers_table(connection)

        customers_name =  "Fulano da Silva"
        customers_email = "fulano.silva@gmail.com"
        customers_phone = "91986207879"
        customers_adress = "Rua A, 1895"

        create_customers(connection, customers_name, customers_email, customers_phone, customers_adress)

        connection.close()
        print("Conexão com o MYSQL fechada!")
    else:
        print("Não foi possível conectar ao banco de dados. Verificar as credencias.")

if __name__ == "__main__":
    main()
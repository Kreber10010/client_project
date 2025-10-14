import os
import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import database
import metodos_crud

load_dotenv()

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

def menu_principal():
    print("\n-------- Opções --------")
    print("1: Criar")
    print("2: Procurar")
    print("3: Atualizar")
    print("4: Deletar")
    print("5: Sair")
    print("---------------------------")

def sub_menu():
    print("\n-------- Opções --------")
    print("1: Nome")
    print("2: Email")
    print("3: Contato")
    print("4: Endereço")

def main():
    opcoes = {
        '1' : metodos_crud.criar_novo_cliente,
        '2' : metodos_crud.read__all_customers,
        '3' : sub_menu,    
        '4' : metodos_crud.delete_customers
    }

    connection = database.connect_to_database()
    if connection:
        print("Conexão bem sucedida com o banco de dados!")

        create_customers_table(connection)

        while True:
            menu_principal()
            escolha = input("Escolha uma opção: ")

            if escolha == '5':
                print("Saindo...")
                break

        #metodos_crud.read__all_customers(connection)

    else:
        print("Não foi possível conectar ao banco de dados. Verificar as credencias.")

if __name__ == "__main__":
    main()
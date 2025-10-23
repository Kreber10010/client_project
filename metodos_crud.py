import os
from sqlite3 import Cursor 
import mysql.connector
from mysql.connector import errorcode

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

def criar_novo_cliente(connection):
        print("\n----- Cadastro novo cliente -----\n")
        customers_name =  input("Nome: ")
        customers_email = input("Email: ")
        customers_phone = input("Contato: ")
        customers_adress = input("Endereço:")
        print("-------------------------------------")

        create_customers(connection, customers_name, customers_email, customers_phone, customers_adress)

        connection.close()


def read__all_customers(connection):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT id, nome, email, telefone FROM customers"
        #customers_data = (id, nome, email, telefone)
        cursor.execute(sql_query)

        results = cursor.fetchall()

        if results:
            print("\n----- Lista de clientes cadastrados -----\n")
            for customers in results:
                print(f"ID: {customers[0]}, Nome: {customers[1]}, Email: {customers[2]}, Telefone: {customers[3]}")
            print("---------------------------------------------")
        else:
            print("Nenhum cliente encontrado no banco de dados!")
    except mysql.connector.Error as e:
        print(f"Erro ao verificar clientes: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def read_one(connection, nome):
    try:
        cursor = connection.cursor()
        sql_query = "SELECT nome, email, telefone FROM customers WHERE nome = %s"
        cursor.execute(sql_query, (nome, ))

        linha = cursor.fetchone()

        if linha:
            print(f"Dados de {nome}: ")
            print(f"Nome: {linha[0]}")
            print(f"Email: {linha[1]}")
            #print(f"Telefone: {linha[2]}")
            #print(f"Endereço: {linha[3]}")
            print("---------------------------------------------")

            return True
            
        else:
            print("Nenhum cliente encontrado no banco de dados!")

    except mysql.connector.Error as e:
        print(f"Erro ao verificar cliente: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def update_customers(connection):
    try:
        cursor = connection.cursor()

        print("Digite o nome do cliente a ser procurado: ")
        nome_para_buscar = input("Nome: ")

        item_encontrado = read_one(connection, nome_para_buscar)

        #item_encontrado = busca_customers(connection, nome_para_buscar)
        
        if item_encontrado:
            novo_nome = input("Digite novo nome: ")
            valores = (novo_nome, nome_para_buscar)

            query_update = "UPDATE customers SET nome = %s WHERE nome = %s"
            cursor.execute(query_update, valores)
            connection.commit()

            read_one(connection, novo_nome)
        else:
            print("Nome buscado não foi encontrado!")
        

    except mysql.connector.Error as e:
        print(f"Erro ao atualizar dado: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def delete_customers():
    print("delete")

#No momento esse método não tem muita utilidade, pq já temos um método read_one que retorna os valores de cada linha do DB.
def busca_customers(connection, nome_para_buscar):
    try:
        cursor = connection.cursor()
        query_select = f"SELECT * FROM customers WHERE nome = %s"
        nome_busca = (nome_para_buscar)

        cursor.execute(query_select, (nome_busca), )
        item = cursor.fetchone()

        return item

    except mysql.connector.Error as e:
        print(f"Erro ao atualizar dado: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
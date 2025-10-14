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
        print("Erro ao verificar clientes: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def update_customers(connection):
    try:
        cursor = connection.cursor()
        print("update")
    except mysql.connector.Error as e:
        print("Erro ao atualizar dado: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()

def delete_customers():
    print("delete")
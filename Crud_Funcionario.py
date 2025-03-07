import mysql.connector
from config import MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE

def get_connection():
    return mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD,
        database = MYSQL_DATABASE 
    )
           
def create_user(nome,email,data_de_nascimento,data_de_contrato,telefone,cidade,estado,bairro):
    conn =get_connection()
    cursor = conn.cursor()
    query = "insert user (nome,email,data_de_nascimento,data_de_contrato,telefone,cidade,estado,bairro) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(nome,email,data_de_nascimento,data_de_contrato,telefone,cidade,estado,bairro))
    conn.commit()
    cursor.close()
    conn.close()


def read_users():
    conn =get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM user"
    cursor.execute(query,)
    result = cursor.fetchall()
    cursor.close()
    conn.close() 
    return result


def update_user(user_id,nome,email,data_de_nascimento,data_de_contrato,telefone,cidade,estado,bairro):
    conn =get_connection()
    cursor = conn.cursor()
    query = "UPDATE user SET nome=%s,email=%s,data_de_nascimento=%s,data_de_contrato=%s,telefone%s,cidade%s,estado%s,bairro%s WHERE idusuario ==%s"
    cursor.execute(query,(user_id,nome,email,data_de_nascimento,data_de_contrato,telefone,cidade,estado,bairro))
    conn.commit()
    cursor.close()
    conn.close()


def delete_user(user_id):
    conn =get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM user WHERE = %s"
    cursor.execute(query,(user_id
                          ))
    conn.commit()
    cursor.close()
    conn.close()

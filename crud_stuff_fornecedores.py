import mysql.connector

# Configurações do banco de dados
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''  # Substitua pelo seu password, se necessário
MYSQL_DATABASE = 'farmacia_sa'

def get_connection():
    """Estabelece conexão com o banco de dados"""
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

# Adicionar fornecedor
def add_supplier(nome, email, produto, transporte, cidade, estado):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """INSERT INTO fornecedor (nome, email, produto, transporte, cidade, estado)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (nome, email, produto, transporte, cidade, estado))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# Ler todos os fornecedores
def read_suppliers():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM fornecedor"
        cursor.execute(query)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

# Atualizar fornecedor
def update_supplier(id_fornecedor, nome, email, produto, transporte, cidade, estado):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = """UPDATE fornecedor
                   SET nome = %s, email = %s, produto = %s,
                       transporte = %s, cidade = %s, estado = %s
                   WHERE idfornecedor = %s"""
        cursor.execute(query, (nome, email, produto, transporte, cidade, estado, id_fornecedor))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

# Deletar fornecedor
def delete_supplier(id_fornecedor):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM fornecedor WHERE idfornecedor = %s"
        cursor.execute(query, (id_fornecedor,))
        conn.commit()
    finally:
        cursor.close()
        conn.close()

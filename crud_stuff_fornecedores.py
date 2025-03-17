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
        print("Fornecedor adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar fornecedor: {e}")
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
        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Erro ao listar fornecedores: {e}")
    finally:
        cursor.close()
        conn.close()

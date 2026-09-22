
from database.conexao import conectar_bd


def criar_banco_dados():
    #Criando a tabela de tarefas no banco de dados SQLITE3
        conexao, cursor = conectar_bd()
        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tarefas (
                        cod_tarefas INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarefa TEXT,
                        status TEXT);            
                        """)
        conexao.commit()
        conexao.close()



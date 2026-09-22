
from database.conexao import conectar_bd



def inserir_tarefa(tarefa):
    #Incluindo na tabela tarefas
            conexao, cursor = conectar_bd()
            cursor.execute("""
                            INSERT INTO tarefas (tarefa, status)
                            VALUES (?, ?)
                            """,
                            [tarefa, "PENDENTE" ])
            conexao.commit()
            cod_tarefa = cursor.lastrowid
            conexao.close()
            return cod_tarefa

def recuperar_tarefas():
        conexao, cursor = conectar_bd()
        cursor.execute("""
                     SELECT * FROM tarefas;""")
        tarefas = cursor.fetchall()
        conexao.close()
        
        return tarefas

def deletar_tarefa(codigo_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""
                    DELETE FROM tarefas
                    WHERE cod_tarefas = ?;
                    """,
                    [codigo_tarefa])
    conexao.commit()
    conexao.close()

    def atualizar_status(codigo_tarefa, novo_Status):
        conexao, cursor = conectar_bd()
        cursor.execute("""
                        UPDATE FROM tarefas
                        SET status = ?
                        WHERE cod_tarefas = ?;
                        """,
                        [novo_Status, codigo_tarefa])
        conexao.commit()
        conexao.close()
        
        
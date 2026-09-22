import sqlite3

def conectar_bd():
    connect = sqlite3.connect("bd_tarefas.sqlite")
    cursor = connect.cursor()
    return connect, cursor

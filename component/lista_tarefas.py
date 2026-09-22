import flet as ft
from component.classe_campo_lista import Campo_tarefa
import sqlite3
from database.conexao import conectar_bd
from database.create_database import criar_banco_dados
from model import model_tarefa

def main(page: ft.Page):
    page.title = "TAREFAS"
    page.bgcolor = "#b352d1"
    page.window.height = 700
    page.window.width = 800
    page.horizontal_alignment = "center"

    criar_banco_dados()

    titulo = ft.Text(value = "GodoRefas",
                     size=40,
                     font_family="Times New Roman",
                     color="#31ec31")

    



    lista_campo_tarefas = []

    tarefa = ft.TextField(value="",
                          label="Adicione sua tarefa")


        
    
    def adicionar_tarefa(e):
        cod = model_tarefa.inserir_tarefa(tarefa.value)
        lista_campo_tarefas.append(Campo_tarefa(texto_tarefa=tarefa.value, 
                                                funcao_excluir=excluir_tarefa,
                                                cod_tarefa=cod))
        tarefa.value = ""

    def excluir_tarefa(campo_tarefa):
        model_tarefa.deletar_tarefa(campo_tarefa.cod_tarefa)
        lista_campo_tarefas.remove(campo_tarefa)
        
        #Recuperando as tarefas do banco de dados e montando os componentes
    tarefas_do_bd = model_tarefa.recuperar_tarefas()
    for tarefas in tarefas_do_bd:
        novo_campo = Campo_tarefa(texto_tarefa=tarefas[1],
                                funcao_excluir=excluir_tarefa,
                                cod_tarefa=tarefas[0])
        lista_campo_tarefas.append(novo_campo)

    

  
    botao_adicionar_tarefa = ft.Button(content="Incluir",
                                       on_click=adicionar_tarefa)

    coluna_tarefas = ft.Column(controls=lista_campo_tarefas,
                               )


    linha_tarefa_add = ft.Row(controls=[tarefa,botao_adicionar_tarefa],
                              alignment="center")


    page.controls = [
                    titulo,
                    coluna_tarefas,
                    linha_tarefa_add
                    ]
    page.update()
ft.run(main)
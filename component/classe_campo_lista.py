import flet as ft
from model import model_tarefa


class Campo_tarefa(ft.Row):
    def __init__(self, texto_tarefa, funcao_excluir, cod_tarefa):
        super().__init__()

        self.cod_tarefa = cod_tarefa

        self.funcao_excluir = funcao_excluir

        self.caixa_tarefa_fazer = ft.TextField(value=texto_tarefa)
    
        self.caixa_estado = ft.Text(value="Pendente")
        
        def mudar_texto():
            if self.caixa_estado.value == "Pendente":
                self.caixa_estado.value = "Concluído"
                self.container_tudo.bgcolor = "#31ec31"
            elif self.caixa_estado.value == "Concluído":
                self.caixa_estado.value = "Pendente"
                self.container_tudo.bgcolor = "#ffffff"


        def alterar_cor():
            if self.caixa_estado.value == True
                
        
        self.caixa_verificacao = ft.Checkbox(value=0,
                                             on_change=mudar_texto)

        self.caixa_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE,
                                                     mini=True,
                                                     on_click=lambda: self.funcao_excluir(self),
                                                     bgcolor="#b352d1",
                                                     
                                                     )

        self.caixa_editar = ft.FloatingActionButton(icon=ft.Icons.EDIT,
                                                    mini=True,
                                                    bgcolor="#b352d1" 
                                                    )

        self.coluna_botoes = ft.Column(controls=[self.caixa_excluir,self.caixa_editar])

        self.coluna_tarefas = ft.Column(controls=[self.caixa_estado,self.caixa_tarefa_fazer])

        self.linha_tudo = ft.Row(controls=[self.caixa_verificacao,self.coluna_tarefas,self.coluna_botoes])

        self.container_tudo = ft.Container(content=self.linha_tudo,
                                           border_radius=10,
                                           bgcolor="#FFFFFF")

        self.controls = [self.container_tudo]
import flet as ft

cadastros = []

def main(page: ft.Page):
    nome_input = ft.TextField(label="Nome", width=300)
    horario_input = ft.TextField(label="Horário", width=300)
    produto_input = ft.TextField(label="Produto", width=300)

    def cadastrar(e):   
        cadastros.append({
            "nome": nome_input.value,
            "horario": horario_input.value,
            "produto": produto_input.value  })
        
        def segunda_pagina(page: ft.Page):
            page.title = "Dados Cadastrados"            
            tabela = ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Nome")),
                    ft.DataColumn(ft.Text("Horário")),
                    ft.DataColumn(ft.Text("Produto")),],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(cadastro["nome"])),
                            ft.DataCell(ft.Text(cadastro["horario"])),
                            ft.DataCell(ft.Text(cadastro["produto"])),]) 
                    for cadastro in cadastros])
                        
            page.add(
                ft.Text("Dados Cadastrados", style="headlineMedium"),
                 tabela,
                ft.ElevatedButton(text="Voltar", on_click=lambda e: main(page)))

        page.clean()
        segunda_pagina(page)

    cadastrar_button = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar)   
    page.add(
        ft.Text("Cadastro de Pessoas", style="headlineMedium"),
        nome_input,
        horario_input,
        produto_input,
        cadastrar_button)


ft.app(target=main)

print(cadastros)
import flet as ft

def main(page):
    # Entradas de dados
    superintendência = ft.TextField(label='Superintendência')
    agencia = ft.TextField(label='Agência')
    gerente = ft.TextField(label='Gerente')
    cpf_cooperado = ft.TextField(label='CPF do cooperado')
    nome_cooperado = ft.TextField(label='Nome do cooperado')

    cooperativa = ft.Row([
        superintendência,
        agencia,
        gerente
    ])






    #Entrada de dados de crédito
    emprestimo = ft.TextField(label='Empréstimo')
    carta_credito = ft.TextField(label='Carta de crédito')
    financiamento = ft.TextField(label='Financiamento')

    # Entradas de DAP
    rdc = ft.TextField(label='RDC')
    lca = ft.TextField(label='LCA')

    # Entradas de produtos
    produto = ft.TextField(label='Digite o Produto: ')
    volume_produto = ft.TextField(label='Volume em negociação')
    quantidade_produto = ft.TextField(label='Quantidade')
    data_previsao_produto = ft.TextField(label='Data de previsão',)

    page.add(
        cooperativa,
        ft.Divider(color='transparent', height=9),
    )


ft.app(target=main)
# vendas = ('guilherme', '20/05/2022', '14/11/1996', 2000, 'estagiario')
#
# nome = vendas[0]
# contratacao = vendas[1]
# data_nasc = vendas[2]
# salario = vendas[3]
# cargo = vendas[4]
#
# nome, contratacao, data_nasc, salario, cargo = vendas # ou pode realizar dessa forma
# print(salario)


# ---------------------------------------
# vendas = [1000, 2000, 3000, 4000]
# funcionarios = ['Joao', 'Guilherme', 'Wilma', 'Victor']
#
#
# for i, venda in enumerate(vendas):
#     print(f'O funcionario {funcionarios[i]} vendeu {venda}')

# -----------------------
# meta = 1000
# vendas = [
#     ['caio', 983],
#     ['jorge', 987],
#     ['matheus', 1126],
#     ['marcelo', 816],
#     ['miguel', 1765],
#     ['lara', 998],
#     ['guilherme', 1099],
#     ['wilma', 1199],
# ]
#
# for vendedor, qtde in vendas:
#     if qtde >= meta:
#         print(f'{vendedor} nao bateu a meta vendendo {qtde}.')

# -----------------------
# vendas_produtos = [('Iphone', 203948,374865), ('galaxy', 56763, 87674), ('ipad', 12455,9874)]
#
# for produto, venda2019,venda2020 in vendas_produtos:
#     if venda2020 > venda2019:
#         porcent = (venda2020 / venda2019 -1)
#         print(f'O produto {produto} vendeu em 2019 {venda2019} e em 2020 {venda2020} e teve um crescimento de {porcent:.1%}')

# ---------------------------
# vendas = [
#     ('20/05/2020', 'iphone', 'preto', '128gb', 350, 7800),
#     ('20/05/2020', 'galaxy', 'azul', '128gb', 430, 2800),
#     ('21/05/2020', 'xiaomi', 'preto', '240gb', 700, 3800),
#     ('21/05/2020', 'lg', 'roxo', '64gb', 350, 1800),
# ]
#
# produto_mais_vendido20 = ''
# qtde_produto_vendido20 = 0
#
# for item in vendas:
#     data, produto, cor, memoria, unidade, valor_unid = item
#     if data == '20/05/2020':
#         if unidade > qtde_produto_vendido20:
#             produto_mais_vendido20 = produto
#             qtde_produto_vendido20 = unidade
#
# print(f'O produto mais vendido do dia 20/05/2020 foi {produto_mais_vendido20}. Quantidade vendida: {qtde_produto_vendido20}')
#
#
# produto_mais_vendido21 = ''
# qtde_produto_vendido21 = 0
#
# for item in vendas:
#     data, produto, cor, memoria, unidade, valor_unid = item
#     if data == '21/05/2020':
#         if unidade > qtde_produto_vendido21:
#             produto_mais_vendido21 = produto
#             qtde_produto_vendido21 = unidade
#
# print(f'O produto mais vendido do dia 21/05/2020 foi {produto_mais_vendido21}. Quantidade vendida: {qtde_produto_vendido21}')

# -------------------------------------------------
vendas = [
    ('20/05/2020', 'iphone', 'preto', '128gb', 350, 7800),
    ('20/05/2020', 'galaxy', 'azul', '128gb', 430, 2800),
    ('21/05/2020', 'xiaomi', 'preto', '240gb', 700, 3800),
    ('21/05/2020', 'lg', 'roxo', '64gb', 350, 1800),
]

produto_mais_vendido21 = ''
qtde_produto_vendido21 = 0
faturamento = 0

for item in vendas:
    data, produto, cor, memoria, unidade, valor_unid = item
    if produto == 'xiaomi' and data == '21/05/2020':
        print(produto)
        faturamento += unidade * valor_unid
        print(f' O modelo {produto} foi vendido {unidade} unidades. O valor de faturamento foi de: R${faturamento}')
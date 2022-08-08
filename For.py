# produtos = ['leite', 'soja', 'macarrao', 'aveia', 'manteiga']
# producao = [100, 150, 300, 450, 525, 799]
#
# tamanho_lista = len(produtos)
# for i in range(tamanho_lista):
#     print(f'O produto {produtos[i]} foi produzida {producao[i]} unidades.')

# -----------
# produtos = ['leite', 'soja', 'macarrao', 'aveia', 'manteiga']
# producao = [100, 150, 300, 450, 525, 799]
#
# for produto in produtos:
#     print(produto)

# -------------------
# vendas = [100,1200,232,456,1345,1567,789,567,34,55,687,918,990,1110,658]
# meta = 1000
# bateu_meta = 0
# qtd_func = len(vendas)
#
# for venda in vendas:
#     if venda >= meta:
#         bateu_meta += 1
#
# percentual_metas = bateu_meta / qtd_func
# print('A quantidade de metas batidas foi de {:.2%}'.format(percentual_metas))

# ---------------------
# funcionarios = ['Marcos', 'Antonio', 'Joao', 'Kleber', 'Mauricio', 'Marcio', 'Guilherme']
#
# for i, funcionario in enumerate(funcionarios):
#     print(f'O nummero {i} é o {funcionario}')

# ---------------------------
# estoque = [100,234,46,456,234,567,68,315,234,657,44,49,867]
# produtos = ['Soda', 'Soja', 'Cerveja', 'Amendoim', 'Maça', 'Cebola', 'Abacate', 'Chocolate', 'Bis', 'Nescau', 'Agua', 'Refrigerante', 'Salgado']
#
# nivel_minimo = 50
#
# for i, qtd in enumerate(estoque):
#     if qtd < nivel_minimo:
#         print(f'O produto {produtos[i]} esta abaixo do nivel minimo. Temos apenas {qtd}')

# -------------------------------
# estoque = [[100,234,46,456,234,567,68,315,234,657,44,49,867,345,234,456,76,78,234,456,678,45,27,468,123],[923,874,89,327,437,298,478,327,493,289,748,327,498,738,33,12,41],[71,85,973,659,659,14,83,65,983,465,938,465,831,476,594,386,57,33,45]]
#
# fabricas = ['Fabricsul', 'Notorierd', 'JoaoImports']
# minimo = 50
#
# for i, item in enumerate(estoque):
#     for qtd in item:
#         if qtd < minimo:
#             print(fabricas[i], qtd)

# ----------------------------
# produtos = ['celular', 'notebook', 'ipad', 'tablet', 'all-in-one']
# vendas2020 = [293847,18476,128746,67465,7221]
# vendas2021 = [409865,13454,138473,90854,2348]
#
# for i, produto in enumerate(produtos):
#     if vendas2021[i] > vendas2020[i]:
#         crescimento = vendas2021[i] / vendas2020[i] - 1
#         print(f'O produto {produto} vendeu R${vendas2020[i]} reais em 2020 e em 2021 R${vendas2021[i]}. Teve seu crescimento em {crescimento:.2%}')
#     else:
#         print(f'O produto {produto} não teve um crescimento significativo de 2020 para 2021.')

# ----------------------------------

# qtde_pessoas = int(input('Quantas pessoas irá ficar nesse quarto? '))
# quarto = []
#
# for i in range(qtde_pessoas):
#     nome = input('Digite o nome da pessoa: ')
#     cpf = input('Digite o cpf da pessoa: ')
#     hospede = [f'{nome}, cpf: {cpf}']
#     quarto.append(hospede)
#
# print(quarto)

# ---------------------------
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
# for item in vendas:
#     if item[1] >= meta:
#         print(f'O vendedor {item[0]} teve {item[1]} vendas e conseguiu bater a meta.')

# ---------------------
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
#     ['Jose', 567],
# ]
#
# bateu_meta = []
#
# for i in vendas:
#     if i[1] >= meta:
#         bateu_meta.append(i)
#
#
# vendas = len(vendas)
# bateu_meta = len(bateu_meta)
# percentual_metas = bateu_meta / vendas
#
# print(f'O percentual de metas batidas foi de {percentual_metas:.1%}')

# --- OU FAZER DE OUTRO JEITO

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
#     ['Jose', 567],
# ]
#
# acima_meta = 0
#
#
# for i in vendas:
#     if i[1] >= meta:
#         acima_meta += 1
#
# vendas = len(vendas)
# resultado = acima_meta / vendas
#
# print(f'{resultado:.1%}')

# ------- MELHOR VENDEDOR ---------

# meta = 1000
# vendas = [
#     ['caio', 983],
#     ['jorge', 987],
#     ['matheus', 1126],
#     ['marcelo', 816],
#     ['miguel', 1765],
#     ['lara', 998],
#     ['guilherme', 1099],
#     ['wilma', 11199],
#     ['Jose', 567],
# ]
#
# melhor_vendedor = ''
# bateu_meta = 0
#
# for venda in vendas:
#     if venda[1] > bateu_meta:
#         bateu_meta = venda[1]
#         melhor_vendedor = venda[0]
#
# print(f'Meu melhor vendedor(a) é o(a) {melhor_vendedor} que vendeu {bateu_meta}')

# ----------------------------------------
vendas = [100,150,200,230,400]
vendedor = ['maria', 'carlos', 'jose', 'fernando', 'sorocaba']
meta = 101

for venda in vendas:
    if venda < meta:
        continue
    print(venda)
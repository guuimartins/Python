# venda = input('Digite aqui o nome do produto que queira cadastrar. Para finalizar, aperte enter.  ')
# vendas = []
#
# while venda != '':
#     vendas.append(venda)
#     venda = input('Digite aqui o nome do produto que queira cadastrar. Para finalizar, aperte enter.  ')
#
# print(f'Registro finalizado. Os produtos cadastrados são: {vendas}')

# -------------------------------------

# estoque = [100,234,46,456,234,567,68,315,234,657,44,49,867]
# produtos = ['Soda', 'Soja', 'Cerveja', 'Amendoim', 'Maça', 'Cebola', 'Abacate', 'Chocolate', 'Bis', 'Nescau', 'Agua', 'Refrigerante', 'Salgado']
#
# meta = 50
# i = 0
#
# while estoque[i] > meta:
#     print(f'O produto {produtos[i]} bateu a meta com {estoque[i]} vendas.')

vendas = []

while True:
    produto = input('Digite um produto: ')
    if not produto:
        break
    qtde = int(input('Digite uma quantidade de produto: '))
    vendas.append([produto,qtde])

print(vendas)
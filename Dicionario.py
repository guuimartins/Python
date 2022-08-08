mais_vendidos = {'tecnologia': 'iphone', 'cozinha': 'panelas', 'sala': 'sofa', 'quarto': 'guarda-roupa'}
qtde_vendas = {'iphone': 1212, 'panelas': 846, 'sofa': 1810, 'guarda-roupa': 1299}

# vendas_iphone = qtde_vendas['iphone']
# quarto = mais_vendidos['quarto']
# v_quarto = qtde_vendas['guarda-roupa']
#
# print(f'O {quarto} foi vendido {v_quarto} unidades')

# if 'panelas' in qtde_vendas:
#     print('Nós temos esse item no estoque')
# else:
#     print('Nós NÃO temos esse item em estoque}')

if qtde_vendas.get('iphone') == None:
    print('Nós não temos esse item em estoque')
else:
    print(f'Vendemos {qtde_vendas.get("iphone")} iphones')

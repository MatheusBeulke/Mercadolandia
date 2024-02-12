# Versão 2.1

habilidades = {'Habilidade de vendas': 0, 'Habilidade de reduzir preco': 0, 'Habilidade de lucro': 0,
               'Habilidade de ganhar mais exp': 0}
precohabilidade = {'precohavendas': 5, 'precohapreco': 5, 'precohalucro': 5, 'precohaexp': 5}
levelmaximohabi = {'lvhv': 10, 'lvhp': 5, 'lvhl': 10, 'lvhe': 10}
maisexp = 0

dinheiro = 20000
diamante = 0
nivel = {'level': 1, 'qtdeexp': 0, 'uplevel': 3000}

nmapa = ['0']
mapa = ['Santa Catarina']
ntipo_de_mercado = ['0', '1', '2', '3']
tipo_de_mercado = ['Acougue', 'Padaria', 'Loja de Eletronica', 'SuperMercado']
preco_mercado = [4000, 2000, 5000, 3000]
SCSPTipos_Deposito_Informacoes = []
SCSPTipos_Mercado_Informacoes = []
lvevolucaoimovel = {'scacougued': 1, 'scacougue': 1, 'scpadariad': 1, 'scpadaria': 1, 'sclojaeled': 1, 'sclojaele': 1,
                    'scsmd': 1, 'scsm': 1}
precoevolucaoimovel = {'scacougued': 500, 'scacougue': 1000, 'scpadariad': 500, 'scpadaria': 1000, 'sclojaeled': 500,
                       'sclojaele': 1000, 'scsmd': 500, 'scsm': 1000}
limiteevolucaoimovel = {'scacougued': 100, 'scacougue': 100, 'scpadariad': 100, 'scpadaria': 100, 'sclojaeled': 100,
                        'sclojaele': 100, 'scsmd': 100, 'scsm': 100}
tamanhoocupado = {'scacougue': 0, 'scpadaria': 0, 'sclojaele': 0, 'scsm': 0}
lucro = {'scacougue': 0, 'scpadaria': 0, 'sclojaele': 0, 'scsm': 0}

nfuncionario = ['0', '1']
funcionario = ['Daniel', 'Jhennyfer']
precofuncionario = [1300, 1200]

# Santa Catarina
SC = int(-1)
SCnumeracao_estado = []
SCEstado_Mercado = []
SCTipo_Mercado = []
SCNome_Mercado = []
scimoveis = {'Acougue': 0, 'Padaria': 0, 'Loja de Eletronica': 0, 'SuperMercado': 0}
sctipo_deposito_info = ['scacougued', 'scpadariad', 'sclojaeled', 'scsmd']
sctipo_mercado_info = ['scacougue', 'scpadaria', 'sclojaele', 'scsm']

# SCAcougue
scqtdemoveisacougue = {'Caixa': 0, 'FreezerP': 0, 'FreezerM': 0, 'FreezerG': 0}
sclimiteitensmoveisacougue = [0, 30, 60, 90]
scespacomoveisacougue = [20, 10, 20, 30]
scnmoveisa = ['0', '1', '2', '3']
scmoveisacougue = ['Caixa', 'FreezerP', 'FreezerM', 'FreezerG']
scprecomoveisacougue = [800, 600, 950, 1300]

scnpa = ['0', '1', '2', '3', '4', '5', '6', '7']
scprodutosacougue = ['Atum', 'Bacon', 'Carne de boi', 'Carne de frango', 'Carne de porco', 'Caviar', 'Lula', 'Picanha']
scprecoacouguec = [9.99, 17.99, 19.99, 12.99, 19.99, 93, 29.49, 45.99]
scqtdeprodutoacougue = {'Atum': 0, 'Bacon': 0, 'Carne de boi': 0, 'Carne de frango': 0, 'Carne de porco': 0,
                        'Caviar': 0, 'Lula': 0, 'Picanha': 0}

scqtdeprodepositoacougue = {'Atum': 0, 'Bacon': 0, 'Carne de boi': 0, 'Carne de frango': 0,
                            'Carne de porco': 0, 'Caviar': 0, 'Lula': 0, 'Picanha': 0}

scprecoacouguev = [17.99, 24.49, 24.99, 20.69, 27.49, 129.99, 59.99, 79.99]
scqtdeprovendasacougue = {'Atum': 0, 'Bacon': 0, 'Carne de boi': 0, 'Carne de frango': 0, 'Carne de porco': 0,
                          'Caviar': 0, 'Lula': 0, 'Picanha': 0}

scqtdefuncionariosacougue = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoesacougue = {'Caixa': 0, 'Acougueiro': 0}
scfuncoesacougue = ['Caixa', 'Acougueiro']
scacouguepgmtfuntotal = 0

# SCPadaria
scqtdemoveispadaria = {'Caixa': 0, 'Boleira': 0, 'MesaP': 0, 'MesaM': 0, 'MesaG': 0, 'GeladeiraP': 0, 'GeladeiraM': 0,
                       'GeladeiraG': 0, 'PasteleiraP': 0, 'PasteleiraM': 0, 'PasteleiraG': 0, 'PrateleiraP': 0,
                       'PrateleiraM': 0, 'PrateleiraG': 0}
sclimiteitensmoveispadaria = [0, 20, 20, 40, 60, 50, 100, 150, 50, 100, 150, 100, 200, 300]
scespacomoveispadaria = [20, 20, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30]
scnmoveisp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
scmoveispadaria = ['Caixa', 'Boleira', 'MesaP', 'MesaM', 'MesaG', 'GeladeiraP', 'GeladeiraM', 'GeladeiraG',
                   'PasteleiraP', 'PasteleiraM', 'PasteleiraG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
scprecomoveispadaria = [800, 300, 25, 50, 75, 500, 750, 900, 200, 400, 600, 150, 350, 550]

scnpp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
scprodutospadaria = ['Bolacha', 'Bolinho', 'Bolo', 'Cafe', 'Coxinha', 'Cuca', 'Leite', 'Margarina', 'Nata', 'Pao',
                     'Pao_de_queijo', 'Pastel', 'Presunto', 'Queijo', 'Rosquinha', 'Sorvete', 'Yogurt']
scprecopadariac = [3.99, 3.99, 19.99, 7.99, 5.49, 6.49, 5.99, 5.99, 4.99, 5.99, 4.49, 6.99, 5.99, 6.49, 6.99, 18.99,
                   6.49]
scqtdeprodutopadaria = {'Bolacha': 0, 'Bolinho': 0, 'Bolo': 0, 'Cafe': 0, 'Coxinha': 0, 'Cuca': 0, 'Leite': 0,
                        'Margarina': 0, 'Nata': 0, 'Pao': 0, 'Pao_de_queijo': 0, 'Pastel': 0, 'Presunto': 0,
                        'Queijo': 0, 'Rosquinha': 0, 'Sorvete': 0, 'Yogurt': 0}

scqtdeprodepositopadaria = {'Bolacha': 0, 'Bolinho': 0, 'Bolo': 0, 'Cafe': 0, 'Coxinha': 0, 'Cuca': 0,
                            'Leite': 0, 'Margarina': 0, 'Nata': 0, 'Pao': 0, 'Pao_de_queijo': 0,
                            'Pastel': 0, 'Presunto': 0, 'Queijo': 0, 'Rosquinha': 0, 'Sorvete': 0, 'Yogurt': 0}

scprecopadariav = [8.99, 8.49, 49.49, 16.99, 12.99, 13.69, 10.49, 9.49, 8.49, 10.99, 8.99, 9.99, 9.49, 13.49, 12.49,
                   22.99, 11.49]
scqtdeprovendaspadaria = {'Bolacha': 0, 'Bolinho': 0, 'Bolo': 0, 'Cafe': 0, 'Coxinha': 0, 'Cuca': 0, 'Leite': 0,
                          'Margarina': 0, 'Nata': 0, 'Pao': 0, 'Pao_de_queijo': 0, 'Pastel': 0, 'Presunto': 0,
                          'Queijo': 0, 'Rosquinha': 0, 'Sorvete': 0, 'Yogurt': 0}

scqtdefuncionariospadaria = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoespadaria = {'Caixa': 0, 'Padeiro': 0}
scfuncoespadaria = ['Caixa', 'Padeiro']
scpadariapgmtfuntotal = 0

# SCEletronica
scqtdemoveiseletronica = {'Caixa': 0, 'MesaP': 0, 'MesaM': 0, 'MesaG': 0, 'PrateleiraP': 0, 'PrateleiraM': 0,
                          'PrateleiraG': 0}
sclimiteitensmoveiseletronica = [0, 10, 20, 30, 30, 40, 50]
scespacomoveiseletronico = [20, 10, 20, 30, 10, 20, 30]
scnmoveise = ['0', '1', '2', '3', '4', '5', '6']
scmoveiseletronica = ['Caixa', 'MesaP', 'MesaM', 'MesaG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
scprecomoveiseletronica = [800, 25, 50, 75, 150, 350, 550]

scnpe = ['0', '1', '2', '3', '4', '5', '6', '7']
scprodutoseletronica = ['Celular', 'Computador', 'Ipad', 'Mouse', 'Notebook', 'Tablet', 'Teclado', 'Televisao']
scprecoeletronicac = [550, 800, 400, 50, 600, 300, 100, 1000]
scqtdeprodutoeletronica = {'Celular': 0, 'Computador': 0, 'Ipad': 0, 'Mouse': 0, 'Notebook': 0, 'Tablet': 0,
                           'Teclado': 0, 'Televisao': 0}

scqtdeprodepositoeletronica = {'Celular': 0, 'Computador': 0, 'Ipad': 0, 'Mouse': 0, 'Notebook': 0,
                               'Tablet': 0, 'Teclado': 0, 'Televisao': 0}

scprecoeletronicav = [700, 1000, 550, 90, 800, 450, 150, 1300]
scqtdeprovendaseletronica = {'Celular': 0, 'Computador': 0, 'Ipad': 0, 'Mouse': 0, 'Notebook': 0, 'Tablet': 0,
                             'Teclado': 0, 'Televisao': 0}

scqtdefuncionarioseletronica = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoeseletronica = {'Caixa': 0, 'Atendente': 0}
scfuncoeseletronica = ['Caixa', 'Atendente']
scelepgmtfuntotal = 0

# SCSuperMercado
scqtdemoveissupermercado = {'Caixa': 0, 'FruteiraP': 0, 'FruteiraM': 0, 'FruteiraG': 0, 'PrateleiraP': 0,
                            'PrateleiraM': 0, 'PrateleiraG': 0}
sclimiteitensmoveissm = [0, 50, 100, 150, 100, 200, 300]
scespacomoveissm = [20, 10, 20, 30, 10, 20, 30]
scnmoveiss = ['0', '1', '2', '3', '4', '5', '6']
scmoveissupermercado = ['Caixa', 'FruteiraP', 'FruteiraM', 'FruteiraG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
scprecomoveissupermercado = [800, 100, 150, 200, 150, 350, 550]

# SCSuperMercado Frutas_Verduras
scnpsfv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
scprodutossupermercadofv = ['Abacaxi', 'Alface', 'Banana', 'Batata', 'Caqui', 'Cebola', 'Goiaba',
                            'Jabuticaba', 'Limao', 'Maca', 'Noz', 'Tangerina', 'Tomate', 'Uva']

scprecosupermercadocfv = [4.99, 3.49, 3.99, 4.99, 4.49, 4.99, 4.69, 4.49, 4.99, 4.99, 4.69, 4.49, 4.99, 4.99]
scprecosupermercadovfv = [9.49, 6.49, 7.99, 8.99, 8.99, 8.49, 8.99, 8.99, 8.49, 8.99, 9.49, 8.99, 8.49, 8.99]

# SCSuperMercado Limpeza_Higiene
scnpslh = ['14', '15', '16', '17', '18', '19']
scprodutossupermercadolh = ['Amaciante', 'Papel_higienico', 'Detergente', 'Sabao_em_po', 'Sabonete', 'Shampoo']

scprecosupermercadoclh = [9.99, 5.99, 4.99, 7.99, 5.99, 6.99]
scprecosupermercadovlh = [16.99, 10.49, 10.49, 16.99, 10.99, 12.99]

# SCSuperMercado Gerais
scnpsg = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
scprodutossupermercadog = ['Arroz', 'Azeite', 'Acucar', 'Cha', 'Chocolate', 'Feijao', 'Nescau', 'Ovo', 'Pimenta',
                           'Polenta', 'Sal', 'Salgadinho', 'Vinho', 'Vodka']

scprecosupermercadocg = [6.99, 8.49, 9.99, 4.99, 5.99, 7.49, 6.49, 7.99, 6.99, 6.49, 6.49, 6.99, 12.99, 16.99]
scprecosupermercadovg = [11.99, 13.49, 15.99, 9.99, 10.99, 12.99, 12.49, 11.99, 13.99, 12.99, 12.99, 13.99, 19.99, 24.99
                         ]

scqtdeprodutosm = {'Abacaxi': 0, 'Alface': 0, 'Banana': 0, 'Batata': 0, 'Caqui': 0, 'Cebola': 0, 'Goiaba': 0,
                   'Jabuticaba': 0, 'Limao': 0, 'Maca': 0, 'Noz': 0, 'Tangerina': 0, 'Tomate': 0, 'Uva': 0,
                   'Amaciante': 0, 'Papel_higienico': 0, 'Detergente': 0, 'Sabao_em_po': 0, 'Sabonete': 0, 'Shampoo': 0,
                   'Arroz': 0, 'Azeite': 0, 'Acucar': 0, 'Cha': 0, 'Chocolate': 0, 'Feijao': 0, 'Nescau': 0, 'Ovo': 0,
                   'Pimenta': 0, 'Polenta': 0, 'Sal': 0, 'Salgadinho': 0, 'Vinho': 0, 'Vodka': 0}

scqtdeprodepositosm = {'Abacaxi': 0, 'Alface': 0, 'Banana': 0, 'Batata': 0, 'Caqui': 0, 'Cebola': 0,
                       'Goiaba': 0, 'Jabuticaba': 0, 'Limao': 0, 'Maca': 0, 'Noz': 0, 'Tangerina': 0,
                       'Tomate': 0, 'Uva': 0, 'Amaciante': 0, 'Papel_higienico': 0, 'Detergente': 0,
                       'Sabao_em_po': 0, 'Sabonete': 0, 'Shampoo': 0, 'Arroz': 0, 'Azeite': 0, 'Acucar': 0,
                       'Cha': 0, 'Chocolate': 0, 'Feijao': 0, 'Nescau': 0, 'Ovo': 0, 'Pimenta': 0, 'Polenta': 0,
                       'Sal': 0, 'Salgadinho': 0, 'Vinho': 0, 'Vodka': 0}

scqtdeprovendasupermercado = {'Abacaxi': 0, 'Alface': 0, 'Banana': 0, 'Batata': 0, 'Caqui': 0, 'Cebola': 0,
                              'Goiaba': 0, 'Jabuticaba': 0, 'Limao': 0, 'Maca': 0, 'Noz': 0, 'vangerina': 0,
                              'Tomate': 0, 'Uva': 0, 'Amaciante': 0, 'Papel_higienico': 0, 'Detergente': 0,
                              'Sabao_em_po': 0, 'Sabonete': 0, 'Shampoo': 0, 'Arroz': 0, 'Azeite': 0, 'Acucar': 0,
                              'Cha': 0, 'Chocolate': 0, 'Feijao': 0, 'Nescau': 0, 'Ovo': 0, 'Pimenta': 0,
                              'Polenta': 0, 'Sal': 0, 'Salgadinho': 0, 'Vinho': 0, 'Vodka': 0}

scprecocomprasm = scprecosupermercadocfv + scprecosupermercadoclh + scprecosupermercadocg
scprecovendasm = scprecosupermercadovfv + scprecosupermercadovlh + scprecosupermercadovg
scprodutossm = scprodutossupermercadofv + scprodutossupermercadolh + scprodutossupermercadog
scnprodutossm = scnpsfv + scnpslh + scnpsg

scqtdefuncionariossupermercado = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoessupermercado = {'Caixa': 0, 'Repositor': 0}
scfuncoessupermercado = ['Caixa', 'Repositor']
scsmpgmtfuntotal = 0

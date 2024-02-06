habilidades = {'Habilidade de vendas': 1, 'Habilidade de reduzir preco': 0, 'Habilidade de lucro': 0,
               'Habilidade de ganhar mais exp': 0}
precohavendas = int(5)
precohapreco = int(5)
precohalucro = int(5)
precohaexp = int(5)
levelhabi = {'lvhv': 1, 'lvhp': 0, 'lvhl': 0, 'lvhe': 0}
levelmaximohabi = {'lvhv': 10, 'lvhp': 5, 'lvhl': 10, 'lvhe': 10}
maisexp = 0

dinheiro = int(8000)
diamante = int(0)
nivel = {'level': 1, 'qtdeexp': 0, 'uplevel': 3000}

nmapa = ['0', '1']
mapa = ['Santa Catarina', 'São Paulo']
cmapa = ['SC', 'SP']

ntipo_de_mercado = ['0', '1', '2', '3']
tipo_de_mercado = ['Acougue', 'Padaria', 'Loja de Eletronica', 'SuperMercado']
preco_mercado = [4000, 2000, 5000, 3000]

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

# SCAcougue
scqtdemoveisacougue = {'Caixa': 0, 'FreezerP': 0, 'FreezerM': 0, 'FreezerG': 0}
sclimiteitensmoveisacougue = [0, 30, 60, 90]
scqtdeitensmoveisacougue = {'FreezerP': 0, 'FreezerM': 0, 'FreezerG': 0}
scnmoveisa = ['0', '1', '2', '3']
scmoveisacougue = ['Caixa', 'FreezerP', 'FreezerM', 'FreezerG']
scprecomoveisacougue = [800, 600, 950, 1300]

scnpa = ['0', '1', '2', '3', '4', '5', '6', '7']
scprodutosacougue = ['Atum', 'Bacon', 'Carne de boi', 'Carne de frango', 'Carne de porco', 'Caviar', 'Lula', 'Picanha']
scprecoacouguec = [9.99, 17.99, 19.99, 12.99, 19.99, 93, 29.49, 45.99]
scqtdeprodutoacougue = {'Atum': 0, 'Bacon': 0, 'Carne de boi': 0, 'Carne de frango': 0, 'Carne de porco': 0,
                        'Caviar': 0, 'Lula': 0, 'Picanha': 0}

scprodutosdepositoacougue = ['dAtum', 'dBacon', 'dCarne de boi', 'dCarne de frango', 'dCarne de porco', 'dCaviar',
                             'dLula', 'dPicanha']
scqtdeprodepositoacougue = {'dAtum': 0, 'dBacon': 0, 'dCarne de boi': 0, 'dCarne de frango': 0,
                            'dCarne de porco': 0, 'dCaviar': 0, 'dLula': 0, 'dPicanha': 0}

scprodutovendasacougue = ['vAtum', 'vBacon', 'vCarne de boi', 'vCarne de frango', 'vCarne de porco', 'vCaviar', 'vLula',
                          'vPicanha']
scprecoacouguev = [17.99, 24.49, 24.99, 20.69, 27.49, 139.99, 69.99, 89.99]
scqtdeprovendasacougue = {'vAtum': 0, 'vBacon': 0, 'vCarne de boi': 0, 'vCarne de frango': 0, 'vCarne de porco': 0,
                          'vCaviar': 0, 'vLula': 0, 'vPicanha': 0}

scqtdefuncionariosacougue = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoesacougue = {'Fcaixa': 0, 'Facougueiro': 0}
scfuncoesacougue = ['Caixa', 'Acougueiro']

# SCPadaria
scqtdemoveispadaria = {'Caixa': 0, 'Boleira': 0, 'MesaP': 0, 'MesaM': 0, 'MesaG': 0, 'GeladeiraP': 0, 'GeladeiraM': 0,
                       'GeladeiraG': 0, 'PasteleiraP': 0, 'PasteleiraM': 0, 'PasteleiraG': 0, 'PrateleiraP': 0,
                       'PrateleiraM': 0, 'PrateleiraG': 0}
sclimiteitensmoveispadaria = [0, 20, 20, 40, 60, 50, 100, 150, 50, 100, 150, 100, 200, 300]
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

scprodutosdepositopadaria = ['dBolacha', 'dBolinho', 'dBolo', 'dCafe', 'dCoxinha', 'dCuca', 'dLeite', 'dMargarina',
                             'dNata', 'dPao', 'dPao_de_queijo', 'dPastel', 'dPresunto', 'dQueijo', 'dRosquinha',
                             'dSorvete', 'dYogurt']
scqtdeprodepositopadaria = {'dBolacha': 0, 'dBolinho': 0, 'dBolo': 0, 'dCafe': 0, 'dCoxinha': 0, 'dCuca': 0,
                            'dLeite': 0, 'dMargarina': 0, 'dNata': 0, 'dPao': 0, 'dPao_de_queijo': 0,
                            'dPastel': 0, 'dPresunto': 0, 'dQueijo': 0, 'dRosquinha': 0, 'dSorvete': 0, 'dYogurt': 0}

scprodutovendaspadaria = ['vBolacha', 'vBolinho', 'vBolo', 'vCafe', 'vCoxinha', 'vCuca', 'vLeite', 'vMargarina',
                          'vNata', 'vPao', 'vPao_de_queijo', 'vPastel', 'vPresunto', 'vQueijo', 'vRosquinha',
                          'vSorvete', 'vYogurt']
scprecopadariav = [8.99, 8.49, 49.49, 16.99, 12.99, 13.69, 10.49, 9.49, 8.49, 10.99, 8.99, 9.99, 9.49, 13.49, 12.49,
                   22.99, 11.49]
scqtdeprovendaspadaria = {'vBolacha': 0, 'vBolinho': 0, 'vBolo': 0, 'vCafe': 0, 'vCoxinha': 0, 'vCuca': 0, 'vLeite': 0,
                          'vMargarina': 0, 'vNata': 0, 'vPao': 0, 'vPao_de_queijo': 0, 'vPastel': 0, 'vPresunto': 0,
                          'vQueijo': 0, 'vRosquinha': 0, 'vSorvete': 0, 'vYogurt': 0}

scqtdefuncionariospadaria = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoespadaria = {'Fcaixa': 0, 'Fpadeiro': 0}
scfuncoespadaria = ['Caixa', 'Padeiro']

# SCEletronica
scqtdemoveiseletronica = {'Caixa': 0, 'MesaP': 0, 'MesaM': 0, 'MesaG': 0, 'PrateleiraP': 0, 'PrateleiraM': 0,
                          'PrateleiraG': 0}
sclimiteitensmoveiseletronica = [0, 20, 40, 60, 100, 200, 300]
scnmoveise = ['0', '1', '2', '3', '4', '5', '6', '7']
scmoveiseletronica = ['Caixa', 'MesaP', 'MesaM', 'MesaG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
scprecomoveiseletronica = [800, 25, 50, 75, 150, 350, 550]

scnpe = ['0', '1', '2', '3', '4', '5', '6', '7']
scprodutoseletronica = ['Celular', 'Computador', 'Ipad', 'Mouse', 'Notebook', 'Tablet', 'Teclado', 'Televisao']
scprecoeletronicac = [550, 800, 400, 50, 600, 300, 100, 1000]
scqtdeprodutoeletronica = {'Celular': 0, 'Computador': 0, 'Ipad': 0, 'Mouse': 0, 'Notebook': 0, 'Tablet': 0,
                           'Teclado': 0, 'Televisao': 0}

scprodutosdepositoeletronica = ['dCelular', 'dComputador', 'dIpad', 'dMouse', 'dNotebook', 'dTablet', 'dTeclado',
                                'dTelevisao']
scqtdeprodepositoeletronica = {'dCelular': 0, 'dComputador': 0, 'dIpad': 0, 'dMouse': 0, 'dNotebook': 0,
                               'dTablet': 0, 'dTeclado': 0, 'dTelevisao': 0}

scprodutovendaseletronica = ['vCelular', 'vComputador', 'vIpad', 'vMouse', 'vNotebook', 'vTablet', 'vTeclado',
                             'vTelevisao']
scprecoeletronicav = [1000, 1300, 550, 120, 1200, 500, 170, 1600]
scqtdeprovendaseletronica = {'vCelular': 0, 'vComputador': 0, 'vIpad': 0, 'vMouse': 0, 'vNotebook': 0, 'vTablet': 0,
                             'vTeclado': 0, 'vTelevisao': 0}

scqtdefuncionarioseletronica = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoeseletronica = {'Fcaixa': 0, 'Fatendente': 0}
scfuncoeseletronica = ['Caixa', 'Atendente']

# SCSuperMercado
scqtdemoveissupermercado = {'Caixa': 0, 'FruteiraP': 0, 'FruteiraM': 0, 'FruteiraG': 0, 'PrateleiraP': 0,
                            'PrateleiraM': 0, 'PrateleiraG': 0}
sclimiteitensmoveissm = [0, 50, 100, 150, 100, 200, 300]
scnmoveiss = ['0', '1', '2', '3', '4', '5', '6']
scmoveissupermercado = ['Caixa', 'FruteiraP', 'FruteiraM', 'FruteiraG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
scprecomoveissupermercado = [800, 100, 150, 200, 150, 350, 550]

# SCSuperMercado Frutas_Verduras
scnpsfv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
scprodutossupermercadofv = ['Abacaxi', 'Alface', 'Banana', 'Batata', 'Caqui', 'Cebola', 'Goiaba',
                            'Jabuticaba', 'Limao', 'Maca', 'Noz', 'Tangerina', 'Tomate', 'Uva']
scprodutosdepositosmfv = ['dAbacaxi', 'dAlface', 'dBanana', 'dBatata', 'dCaqui', 'dCebola', 'dGoiaba',
                          'dJabuticaba', 'dLimao', 'dMaca', 'dNoz', 'dTangerina', 'dTomate', 'dUva']
scprodutovendasmfv = ['vAbacaxi', 'vAlface', 'vBanana', 'vBatata', 'vCaqui', 'vCebola', 'vGoiaba',
                      'vJabuticaba', 'vLimao', 'vMaca', 'vNoz', 'vTangerina', 'vTomate', 'vUva']
scprecosupermercadocfv = [4.99, 3.49, 3.99, 4.99, 4.49, 4.99, 4.69, 4.49, 4.99, 4.99, 4.69, 4.49, 4.99, 4.99]
scprecosupermercadovfv = [9.49, 6.49, 7.99, 8.99, 8.99, 8.49, 8.99, 8.99, 8.49, 8.99, 9.49, 8.99, 8.49, 8.99]

# SCSuperMercado Limpeza_Higiene
scnpslh = ['14', '15', '16', '17', '18', '19']
scprodutossupermercadolh = ['Amaciante', 'Papel_higienico', 'Detergente', 'Sabao_em_po', 'Sabonete', 'Shampoo']
scprodutosdepositosmlh = ['dAmaciante', 'dPapel_higienico', 'dDetergente', 'dSabao_em_po', 'dSabonete', 'dShampoo']
scprodutovendasmlh = ['vAmaciante', 'vPapel_higienico', 'vDetergente', 'vSabao_em_po', 'vSabonete', 'vShampoo']
scprecosupermercadoclh = [9.99, 5.99, 4.99, 7.99, 5.99, 6.99]
scprecosupermercadovlh = [16.99, 10.49, 10.49, 16.99, 10.99, 12.99]

# SCSuperMercado Gerais
scnpsg = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
scprodutossupermercadog = ['Arroz', 'Azeite', 'Acucar', 'Cha', 'Chocolate', 'Feijao', 'Nescau', 'Ovo', 'Pimenta',
                           'Polenta', 'Sal', 'Salgadinho', 'Vinho', 'Vodka']
scprodutosdepositosmg = ['dArroz', 'dAzeite', 'dAcucar', 'dCha', 'dChocolate', 'dFeijao', 'dNescau', 'dOvo', 'dPimenta',
                         'dPolenta', 'dSal', 'dSalgadinho', 'dVinho', 'dVodka']
scprodutovendasmg = ['vArroz', 'vAzeite', 'vAcucar', 'vCha', 'vChocolate', 'vFeijao', 'vNescau', 'vOvo', 'vPimenta',
                     'vPolenta', 'vSal', 'vSalgadinho', 'vVinho', 'vVodka']
scprecosupermercadocg = [6.99, 8.49, 9.99, 4.99, 5.99, 7.49, 6.49, 7.99, 6.99, 6.49, 6.49, 6.99, 12.99, 16.99]
scprecosupermercadovg = [11.99, 13.49, 15.99, 9.99, 10.99, 12.99, 12.49, 11.99, 13.99, 12.99, 12.99, 13.99, 19.99, 24.99
                         ]

scqtdeprodutosm = {'Abacaxi': 0, 'Alface': 0, 'Banana': 0, 'Batata': 0, 'Caqui': 0, 'Cebola': 0, 'Goiaba': 0,
                   'Jabuticaba': 0, 'Limao': 0, 'Maca': 0, 'Noz': 0, 'Tangerina': 0, 'Tomate': 0, 'Uva': 0,
                   'Amaciante': 0, 'Papel_higienico': 0, 'Detergente': 0, 'Sabao_em_po': 0, 'Sabonete': 0, 'Shampoo': 0,
                   'Arroz': 0, 'Azeite': 0, 'Acucar': 0, 'Cha': 0, 'Chocolate': 0, 'Feijao': 0, 'Nescau': 0, 'Ovo': 0,
                   'Pimenta': 0, 'Polenta': 0, 'Sal': 0, 'Salgadinho': 0, 'Vinho': 0, 'Vodka': 0}

scqtdeprodepositosm = {'dAbacaxi': 0, 'dAlface': 0, 'dBanana': 0, 'dBatata': 0, 'dCaqui': 0, 'dCebola': 0,
                       'dGoiaba': 0, 'dJabuticaba': 0, 'dLimao': 0, 'dMaca': 0, 'dNoz': 0, 'dTangerina': 0,
                       'dTomate': 0, 'dUva': 0, 'dAmaciante': 0, 'dPapel_higienico': 0, 'dDetergente': 0,
                       'dSabao_em_po': 0, 'dSabonete': 0, 'dShampoo': 0, 'dArroz': 0, 'dAzeite': 0, 'dAcucar': 0,
                       'dCha': 0, 'dChocolate': 0, 'dFeijao': 0, 'dNescau': 0, 'dOvo': 0, 'dPimenta': 0, 'dPolenta': 0,
                       'dSal': 0, 'dSalgadinho': 0, 'dVinho': 0, 'dVodka': 0}

scqtdeprovendasupermercado = {'vAbacaxi': 0, 'vAlface': 0, 'vBanana': 0, 'vBatata': 0, 'vCaqui': 0, 'vCebola': 0,
                              'vGoiaba': 0, 'vJabuticaba': 0, 'vLimao': 0, 'vMaca': 0, 'vNoz': 0, 'vTangerina': 0,
                              'vTomate': 0, 'vUva': 0, 'vAmaciante': 0, 'vPapel_higienico': 0, 'vDetergente': 0,
                              'vSabao_em_po': 0, 'vSabonete': 0, 'vShampoo': 0, 'vArroz': 0, 'vAzeite': 0, 'vAcucar': 0,
                              'vCha': 0, 'vChocolate': 0, 'vFeijao': 0, 'vNescau': 0, 'vOvo': 0, 'vPimenta': 0,
                              'vPolenta': 0, 'vSal': 0, 'vSalgadinho': 0, 'vVinho': 0, 'vVodka': 0}

scprecocomprasm = scprecosupermercadocfv + scprecosupermercadoclh + scprecosupermercadocg
scprecovendasm = scprecosupermercadovfv + scprecosupermercadovlh + scprecosupermercadovg
scprodutossm = scprodutossupermercadofv + scprodutossupermercadolh + scprodutossupermercadog
scprodutosdepositosm = scprodutosdepositosmfv + scprodutosdepositosmlh + scprodutosdepositosmg
scprodutovendasm = scprodutovendasmfv + scprodutovendasmlh + scprodutovendasmg
scnprodutossm = scnpsfv + scnpslh + scnpsg
scqtdefuncionariossupermercado = {'Daniel': 0, 'Jhennyfer': 0}
scqtdefuncoessupermercado = {'Fcaixa': 0, 'Frepositor': 0}
scfuncoessupermercado = ['Caixa', 'Repositor']

# São Paulo # São Paulo
SP = int(-1)
SPnumeracao_estado = []
SPEstado_Mercado = []
SPTipo_Mercado = []
SPNome_Mercado = []

spimoveis = {'Acougue': 0, 'Padaria': 0, 'Loja de Eletronica': 0, 'SuperMercado': 0}

# SPAcougue
spqtdemoveisacougue = {'Caixa': 0, 'FreezerP': 0, 'FreezerM': 0, 'FreezerG': 0}
spnmoveisa = ['0', '1', '2', '3']
splimiteitensmoveisacougue = [0, 30, 60, 90]
spmoveisacougue = ['Caixa', 'FreezerP', 'FreezerM', 'FreezerG']
spprecomoveisacougue = [800, 600, 950, 1300]
spnpa = ['0', '1', '2', '3', '4', '5', '6', '7']

spprodutosacougue = ['Atum', 'Bacon', 'Carne de boi', 'Carne de frango', 'Carne de porco', 'Caviar', 'Lula', 'Picanha']
spprecoacouguec = [9.99, 17.99, 19.99, 12.99, 19.99, 93, 29.49, 45.99]
spqtdeprodutoacougue = {'Atum': 0, 'Bacon': 0, 'Carne de boi': 0, 'Carne de frango': 0, 'Carne de porco': 0,
                        'Caviar': 0, 'Lula': 0, 'Picanha': 0}

spprodutosdepositoacougue = ['dAtum', 'dBacon', 'dCarne de boi', 'dCarne de frango', 'dCarne de porco', 'dCaviar',
                             'dLula', 'dPicanha']
spqtdeprodepositoacougue = {'dAtum': 0, 'dBacon': 0, 'dCarne de boi': 0, 'dCarne de frango': 0,
                            'dCarne de porco': 0, 'dCaviar': 0, 'dLula': 0, 'dPicanha': 0}

spprodutovendasacougue = ['vAtum', 'vBacon', 'vCarne de boi', 'vCarne de frango', 'vCarne de porco', 'vCaviar', 'vLula',
                          'vPicanha']
spprecoacouguev = [17.99, 24.49, 24.99, 20.69, 27.49, 139.99, 69.99, 89.99]
spqtdeprovendasacougue = {'vAtum': 0, 'vBacon': 0, 'vCarne de boi': 0, 'vCarne de frango': 0, 'vCarne de porco': 0,
                          'vCaviar': 0, 'vLula': 0, 'vPicanha': 0}

spqtdefuncionariosacougue = {'Daniel': 0, 'Jhennyfer': 0}
spqtdefuncoesacougue = {'Fcaixa': 0, 'Facougueiro': 0}
spfuncoesacougue = ['Caixa', 'Acougueiro']

# SPPadaria
spqtdemoveispadaria = {'Caixa': 0, 'Boleira': 0, 'MesaP': 0, 'MesaM': 0, 'MesaG': 0, 'GeladeiraP': 0, 'GeladeiraM': 0,
                       'GeladeiraG': 0, 'PasteleiraP': 0, 'PasteleiraM': 0, 'PasteleiraG': 0, 'PrateleiraP': 0,
                       'PrateleiraM': 0, 'PrateleiraG': 0}
splimiteitensmoveispadaria = [0, 20, 20, 40, 60, 50, 100, 150, 50, 100, 150, 100, 200, 300]
spnmoveisp = ['0', '1', '2', '3', '4', '5', '6', '7', '8' '9', '10', '11', '12', '13']
spmoveispadaria = ['Caixa', 'Boleira', 'MesaP', 'MesaM', 'MesaG', 'GeladeiraP', 'GeladeiraM', 'GeladeiraG',
                   'PasteleiraP', 'PasteleiraM', 'PasteleiraG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
spprecomoveispadaria = [800, 300, 25, 50, 75, 500, 750, 900, 200, 400, 600, 150, 350, 550]

spnpp = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
spprodutospadaria = ['Bolacha', 'Bolinho', 'Bolo', 'Cafe', 'Coxinha', 'Cuca', 'Leite', 'Margarina', 'Nata', 'Pao',
                     'Pao_de_queijo', 'Pastel', 'Presunto', 'Queijo', 'Rosquinha', 'Sorvete', 'Yogurt']
spprecopadariac = [3.99, 3.99, 19.99, 7.99, 5.49, 6.49, 5.99, 5.99, 4.99, 5.99, 4.49, 6.99, 5.99, 6.49, 6.99, 19.99,
                   6.49]
spqtdeprodutopadaria = {'Bolacha': 0, 'Bolinho': 0, 'Bolo': 0, 'Cafe': 0, 'Coxinha': 0, 'Cuca': 0, 'Leite': 0,
                        'Margarina': 0, 'Nata': 0, 'Pao': 0, 'Pao_de_queijo': 0, 'Pastel': 0, 'Presunto': 0,
                        'Queijo': 0, 'Rosquinha': 0, 'Sorvete': 0, 'Yogurt': 0}

spprodutosdepositopadaria = ['dBolacha', 'dBolinho', 'dBolo', 'dCafe', 'dCoxinha', 'dCuca', 'dLeite', 'dMargarina',
                             'dNata', 'dPao', 'dPao_de_queijo', 'dPastel', 'dPresunto', 'dQueijo', 'dRosquinha',
                             'dSorvete', 'dYogurt']
spqtdeprodepositopadaria = {'dBolacha': 0, 'dBolinho': 0, 'dBolo': 0, 'dCafe': 0, 'dCoxinha': 0, 'dCuca': 0,
                            'dLeite': 0, 'dMargarina': 0, 'dNata': 0, 'dPao': 0, 'dPao_de_queijo': 0,
                            'dPastel': 0, 'dPresunto': 0, 'dQueijo': 0, 'dRosquinha': 0, 'dSorvete': 0, 'dYogurt': 0}

spprodutovendaspadaria = ['vBolacha', 'vBolinho', 'vBolo', 'vCafe', 'vCoxinha', 'vCuca', 'vLeite', 'vMargarina',
                          'vNata', 'vPao', 'vPao_de_queijo', 'vPastel', 'vPresunto', 'vQueijo', 'vRosquinha',
                          'vSorvete', 'vYogurt']
spprecopadariav = [8.99, 8.49, 49.49, 16.99, 12.99, 13.69, 10.49, 9.49, 8.49, 10.99, 9.99, 9.49, 13.49, 12.49, 22.99,
                   11.49]
spqtdeprovendaspadaria = {'vBolacha': 0, 'vBolinho': 0, 'vBolo': 0, 'vCafe': 0, 'vCoxinha': 0, 'vCuca': 0, 'vLeite': 0,
                          'vMargarina': 0, 'vNata': 0, 'vPao': 0, 'vPao_de_queijo': 0, 'vPastel': 0, 'vPresunto': 0,
                          'vQueijo': 0, 'vRosquinha': 0, 'vSorvete': 0, 'vYogurt': 0}

spqtdefuncionariospadaria = {'Daniel': 0, 'Jhennyfer': 0}
spqtdefuncoespadaria = {'Fcaixa': 0, 'Fpadeiro': 0}
spfuncoespadaria = ['Caixa', 'Padeiro']

# SPEletronica
spqtdemoveiseletronica = {'Caixa': 0, 'MesaP': 0, 'MesaM': 0, 'MesaG': 0, 'PrateleiraP': 0, 'PrateleiraM': 0,
                          'PrateleiraG': 0}
splimiteitensmoveiseletronica = [0, 20, 40, 60, 100, 200, 300]
spnmoveise = ['0', '1', '2', '3', '4', '5', '6', '7']
spmoveiseletronica = ['Caixa', 'MesaP', 'MesaM', 'MesaG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
spprecomoveiseletronica = [800, 25, 50, 75, 150, 350, 550]

spnpe = ['0', '1', '2', '3', '4', '5', '6', '7']
spprodutoseletronica = ['Celular', 'Computador', 'Ipad', 'Mouse', 'Notebook', 'Tablet', 'Teclado', 'Televisao']
spprecoeletronicac = [550, 800, 400, 50, 600, 300, 100, 1000]
spqtdeprodutoeletronica = {'Celular': 0, 'Computador': 0, 'Ipad': 0, 'Mouse': 0, 'Notebook': 0, 'Tablet': 0,
                           'Teclado': 0, 'Televisao': 0}

spprodutosdepositoeletronica = ['dCelular', 'dComputador', 'dIpad', 'dMouse', 'dNotebook', 'dTablet', 'dTeclado',
                                'dTelevisao']
spqtdeprodepositoeletronica = {'dCelular': 0, 'dComputador': 0, 'dIpad': 0, 'dMouse': 0, 'dNotebook': 0,
                               'dTablet': 0, 'dTeclado': 0, 'dTelevisao': 0}

spprodutovendaseletronica = ['vCelular', 'vComputador', 'vIpad', 'vMouse', 'vNotebook', 'vTablet', 'vTeclado',
                             'vTelevisao']
spprecoeletronicav = [1000, 1300, 550, 120, 1200, 500, 170, 1600]
spqtdeprovendaseletronica = {'vCelular': 0, 'vComputador': 0, 'vIpad': 0, 'vMouse': 0, 'vNotebook': 0, 'vTablet': 0,
                             'vTeclado': 0, 'vTelevisao': 0}

spqtdefuncionarioseletronica = {'Daniel': 0, 'Jhennyfer': 0}
spqtdefuncoeseletronica = {'Fcaixa': 0, 'Fatendente': 0}
spfuncoeseletronica = ['Caixa', 'Atendente']

# SPSuperMercado
spqtdemoveissupermercado = {'Caixa': 0, 'FruteiraP': 0, 'FruteiraM': 0, 'FruteiraG': 0, 'PrateleiraP': 0,
                            'PrateleiraM': 0, 'PrateleiraG': 0}
splimiteitensmoveissm = [0, 50, 100, 150, 100, 200, 300]
spnmoveiss = ['0', '1', '2', '3', '4', '5', '6']
spmoveissupermercado = ['Caixa', 'FruteiraP', 'FruteiraM', 'FruteiraG', 'PrateleiraP', 'PrateleiraM', 'PrateleiraG']
spprecomoveissupermercado = [800, 100, 150, 200, 150, 350, 550]

# SPSuperMercado Frutas_Verduras
spnpsfv = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
spprodutossupermercadofv = ['Abacaxi', 'Alface', 'Banana', 'Batata', 'Caqui', 'Cebola', 'Goiaba',
                            'Jabuticaba', 'Limao', 'Maca', 'Noz', 'Tangerina', 'Tomate', 'Uva']
spprodutosdepositosmfv = ['dAbacaxi', 'dAlface', 'dBanana', 'dBatata', 'dCaqui', 'dCebola', 'dGoiaba',
                          'dJabuticaba', 'dLimao', 'dMaca', 'dNoz', 'dTangerina', 'dTomate', 'dUva']
spprodutovendasmfv = ['vAbacaxi', 'vAlface', 'vBanana', 'vBatata', 'vCaqui', 'vCebola', 'vGoiaba',
                      'vJabuticaba', 'vLimao', 'vMaca', 'vNoz', 'vTangerina', 'vTomate', 'vUva']
spprecosupermercadocfv = [4.99, 3.49, 3.99, 4.99, 4.49, 4.99, 4.69, 4.49, 4.99, 4.99, 4.69, 4.49, 4.99, 4.99]
spprecosupermercadovfv = [9.49, 6.49, 7.99, 8.99, 8.99, 8.49, 8.99, 8.99, 8.49, 8.99, 9.49, 8.99, 8.49, 8.99]

# SPSuperMercado Limpeza_Higiene
spnpslh = ['14', '15', '16', '17', '18', '19']
spprodutossupermercadolh = ['Amaciante', 'Papel_higienico', 'Detergente', 'Sabao_em_po', 'Sabonete', 'Shampoo']
spprodutosdepositosmlh = ['dAmaciante', 'dPapel_higienico', 'dDetergente', 'dSabao_em_po', 'dSabonete', 'dShampoo']
spprodutovendasmlh = ['vAmaciante', 'vPapel_higienico', 'vDetergente', 'vSabao_em_po', 'vSabonete', 'vShampoo']
spprecosupermercadoclh = [9.99, 5.99, 4.99, 7.99, 5.99, 6.99]
spprecosupermercadovlh = [16.99, 10.49, 10.49, 16.99, 10.99, 12.99]

# SPSuperMercado Gerais
spnpsg = ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
spprodutossupermercadog = ['Arroz', 'Azeite', 'Acucar', 'Cha', 'Chocolate', 'Feijao', 'Nescau', 'Ovo', 'Pimenta',
                           'Polenta', 'Sal', 'Salgadinho', 'Vinho', 'Vodka']
spprodutosdepositosmg = ['dArroz', 'dAzeite', 'dAçucar', 'dCha', 'dChocolate', 'dFeijao', 'dNescau', 'dOvo', 'dPimenta',
                         'dPolenta', 'dSal', 'dSalgadinho', 'dVinho', 'dVodka']
spprodutovendasmg = ['vArroz', 'vAzeite', 'vAçucar', 'vCha', 'vChocolate', 'vFeijao', 'vNescau', 'vOvo', 'vPimenta',
                     'vPolenta', 'vSal', 'vSalgadinho', 'vVinho', 'vVodka']
spprecosupermercadocg = [6.99, 8.49, 9.99, 4.99, 5.99, 7.49, 6.49, 7.99, 6.99, 6.49, 6.49, 6.99, 12.99, 16.99]
spprecosupermercadovg = [11.99, 13.49, 15.99, 9.99, 10.99, 12.99, 12.49, 11.99, 13.99, 12.99, 12.99, 13.99, 19.99, 24.99
                         ]
spqtdeprodutosm = {'Abacaxi': 0, 'Alface': 0, 'Banana': 0, 'Batata': 0, 'Caqui': 0, 'Cebola': 0, 'Goiaba': 0,
                   'Jabuticaba': 0, 'Limao': 0, 'Maca': 0, 'Noz': 0, 'Tangerina': 0, 'Tomate': 0, 'Uva': 0,
                   'Amaciante': 0, 'Papel_higienico': 0, 'Detergente': 0, 'Sabao_em_po': 0, 'Sabonete': 0, 'Shampoo': 0,
                   'Arroz': 0, 'Azeite': 0, 'Acucar': 0, 'Cha': 0, 'Chocolate': 0, 'Feijao': 0, 'Nescau': 0, 'Ovo': 0,
                   'Pimenta': 0, 'Polenta': 0, 'Sal': 0, 'Salgadinho': 0, 'Vinho': 0, 'Vodka': 0}

spqtdeprodepositosm = {'dAbacaxi': 0, 'dAlface': 0, 'dBanana': 0, 'dBatata': 0, 'dCaqui': 0, 'dCebola': 0,
                       'dGoiaba': 0, 'dJabuticaba': 0, 'dLimao': 0, 'dMaca': 0, 'dNoz': 0, 'dTangerina': 0,
                       'dTomate': 0, 'dUva': 0, 'dAmaciante': 0, 'dPapel_higienico': 0, 'dDetergente': 0,
                       'dSabao_em_po': 0, 'dSabonete': 0, 'dShampoo': 0, 'dArroz': 0, 'dAzeite': 0, 'dAçucar': 0,
                       'dCha': 0, 'dChocolate': 0, 'dFeijao': 0, 'dNescau': 0, 'dOvo': 0, 'dPimenta': 0, 'dPolenta': 0,
                       'dSal': 0, 'dSalgadinho': 0, 'dVinho': 0, 'dVodka': 0}

spqtdeprovendasupermercado = {'vAbacaxi': 0, 'vAlface': 0, 'vBanana': 0, 'vBatata': 0, 'vCaqui': 0, 'vCebola': 0,
                              'vGoiaba': 0, 'vJabuticaba': 0, 'vLimao': 0, 'vMaca': 0, 'vNoz': 0, 'vTangerina': 0,
                              'vTomate': 0, 'vUva': 0, 'vAmaciante': 0, 'vPapel_higienico': 0, 'vDetergente': 0,
                              'vSabao_em_po': 0, 'vSabonete': 0, 'vShampoo': 0, 'vArroz': 0, 'vAzeite': 0, 'vAcucar': 0,
                              'vCha': 0, 'vChocolate': 0, 'vFeijao': 0, 'vNescau': 0, 'vOvo': 0, 'vPimenta': 0,
                              'vPolenta': 0, 'vSal': 0, 'vSalgadinho': 0, 'vVinho': 0, 'vVodka': 0}

spprecocomprasm = spprecosupermercadocfv + spprecosupermercadoclh + spprecosupermercadocg
spprecovendasm = spprecosupermercadovfv + spprecosupermercadovlh + spprecosupermercadovg
spprodutossm = spprodutossupermercadofv + spprodutossupermercadolh + spprodutossupermercadog
spprodutosdepositosm = spprodutosdepositosmfv + spprodutosdepositosmlh + spprodutosdepositosmg
spprodutovendasm = spprodutovendasmfv + spprodutovendasmlh + spprodutovendasmg
spnprodutossm = spnpsfv + spnpslh + spnpsg
spqtdefuncionariossupermercado = {'Daniel': 0, 'Jhennyfer': 0}
spqtdefuncoessupermercado = {'Fcaixa': 0, 'Frepositor': 0}
spfuncoessupermercado = ['Caixa', 'Repositor']

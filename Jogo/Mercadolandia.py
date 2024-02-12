# Versão 2.1

from time import sleep
from math import trunc
from random import randint, choice
import BDP


def boasvinda():
    print('Bem-Vindo ao Mercadolândia')
    JogoInicio()


def JogoInicio():
    while True:
        print('Funções de controle:')
        print('[A] Visualizar mapa')
        print('[B] Abrir Mercado')
        print('[C] Comprar Moedas')
        print('[D] Informações')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'ABCD':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
        if tecla in 'A':
            print('Mapa do Jogo: ')
            for i in range(len(BDP.mapa)):
                print(BDP.mapa[i])
            sleep(2)

        elif tecla in 'B':
            Abrir_Mercados()

        elif tecla in 'C':
            comprarmoeda()

        elif tecla in 'D':
            informacoes()


def comprarmoeda():
    print('[0] Comprar diamante.')
    print('[1] Comprar dinheiro.')
    print('[C] Voltar.')
    while True:
        tecla1 = input('Tecla: ').strip().title()
        if tecla1 in '01C':
            break
        else:
            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

    if tecla1 in '0':
        print('1 diamante = R$500')
        qtdemaxima = BDP.dinheiro / 500
        print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
        while True:
            qtde = str(input('Quantidade: '))
            inteiro = qtde.isnumeric()
            strinteiro = str(inteiro)
            ebool = strinteiro.find('False')
            if ebool == 0:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
            else:
                break
        qtde = int(qtde)
        total = 500 * qtde
        if BDP.dinheiro >= total:
            BDP.dinheiro -= total
            BDP.diamante += qtde
            print('Você comprou {} diamante por R${}'.format(qtde, total))
            sleep(1)
        else:
            print('\033[33mErro: \033[mDiamante insuficiente.')

    elif tecla1 in '1':
        while True:
            print('[0] R$500 = 1 diamante')
            print('[1] R$2500 = 5 diamante')
            print('[2] R$5000 = 10 diamante')
            print('[C] Voltar')
            qtdemaxima = BDP.diamante * 500
            print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
            while True:
                tecla2 = input('Tecla: ').strip().title()
                if tecla2 in '012C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla2 in 'C':
                break

            elif tecla2 in '0':
                if BDP.diamante >= 1:
                    BDP.diamante -= 1
                    BDP.dinheiro += 500
                    print('Você comprou R$500 por 1 diamante')
                    sleep(1)
                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')
            elif tecla2 in '1':
                if BDP.diamante >= 5:
                    BDP.diamante -= 5
                    BDP.dinheiro += 2500
                    print('Você comprou R$2500 por 5 diamante')
                    sleep(1)
                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')
            elif tecla2 in '2':
                if BDP.diamante >= 10:
                    BDP.diamante -= 10
                    BDP.dinheiro += 5000
                    print('Você comprou R$5000 por 10 diamante')
                    sleep(1)
                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')


def informacoes():
    while True:
        print('[0] Mostrar saldo.')
        print('[1] Mostrar imóveis.')
        print('[2] Mostrar Level.')
        print('[3] Mostrar habilidades.')
        print('[4] Mostrar conquistar.')
        print('[C] Voltar.')
        while True:
            tecla2 = input('Tecla: ').strip().upper()
            if tecla2 in '01234C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla2 in 'C':
            break

        elif tecla2 in '0':
            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
            print('Dima = {}'.format(BDP.diamante))
            sleep(2)

        elif tecla2 in '1':
            if not BDP.SCTipo_Mercado:
                print('\033[33mErro: \033[mSem comércio.')
                sleep(1)

            else:
                print('Ver informações sobre o imóvel:')
                for m in range(len(BDP.SCTipo_Mercado)):
                    print('[{}] \033[36m{} \033[m= {}'.format(m, BDP.SCNome_Mercado[m], BDP.SCTipo_Mercado[m]))
                while True:
                    tecla3 = str(input('Tecla: '))
                    if tecla3 in '':
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        inteiro = tecla3.isnumeric()
                        strinteiro = str(inteiro)
                        ebool = strinteiro.find('True')
                        if ebool == 0:
                            tecla3 = int(tecla3)
                        if tecla3 in BDP.SCnumeracao_estado:
                            tecla3 = str(tecla3)
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                busca = BDP.scnpe.index(tecla3)
                busca1 = BDP.SCNome_Mercado[busca]
                buscad = BDP.SCSPTipos_Deposito_Informacoes[busca]
                buscam = BDP.SCSPTipos_Mercado_Informacoes[busca]
                print('\033[36m{}: \033[m'.format(busca1))
                while True:
                    print('[0] Mostrar {}'.format(busca1))
                    print('[1] Melhorar {}'.format(busca1))
                    print('[C] Voltar')
                    tecla4 = input('Tecla: ').strip().upper()
                    if tecla4 in 'C':
                        break

                    elif tecla4 in '0':
                        print(f'Depósito: Lv.{BDP.lvevolucaoimovel[buscad]}')
                        print(f'Espaço: Lv.{BDP.lvevolucaoimovel[buscam]}')
                        print(f'Espaço ocupado: {BDP.tamanhoocupado[buscam]}/{BDP.limiteevolucaoimovel[buscam]}')
                        print('Lucro: R${:.2f}'.format(BDP.lucro[buscam]))
                        sleep(3)

                    elif tecla4 in '1':
                        valor_evolucaod = (BDP.precoevolucaoimovel[buscad] * BDP.lvevolucaoimovel[buscad])
                        valor_evolucao = (BDP.precoevolucaoimovel[buscam] * BDP.lvevolucaoimovel[buscam])
                        while True:
                            print('[0] Melhorar Depósito Lv.{} R${}'.format(BDP.lvevolucaoimovel[buscad],
                                                                            valor_evolucaod))
                            print('[1] Melhorar {} Lv.{} R${}'.format(busca1, BDP.lvevolucaoimovel[buscam],
                                                                      valor_evolucao))
                            print('[C] Voltar')
                            while True:
                                tecla5 = input('Tecla: ').strip().upper()
                                if tecla5 in '':
                                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                                else:
                                    if tecla5 in '01C':
                                        break
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                            if tecla5 in 'C':
                                break

                            elif tecla5 in '0':
                                if BDP.dinheiro >= valor_evolucaod:
                                    BDP.dinheiro -= valor_evolucaod
                                    BDP.lvevolucaoimovel[buscad] += 1
                                    BDP.limiteevolucaoimovel[buscad] += 100
                                    print('Você teve um gasto de R${:.2f} com o aumento do depósito'.format(
                                        valor_evolucaod))
                                    sleep(2)
                                    break

                                else:
                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                    sleep(1)

                            elif tecla5 in '1':
                                if BDP.dinheiro >= valor_evolucao:
                                    BDP.dinheiro -= valor_evolucao
                                    BDP.lvevolucaoimovel[buscam] += 1
                                    BDP.limiteevolucaoimovel[buscam] += 100
                                    print('Você teve um gasto de R${:.2f} com o aumento do imóvel({})'.format(
                                        valor_evolucao, busca1))
                                    sleep(2)
                                    break

                                else:
                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                    sleep(1)
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        elif tecla2 in '2':
            expproximolv = BDP.nivel['uplevel'] - BDP.nivel['qtdeexp']
            print('Lv.{}'.format(BDP.nivel['level']))
            print('Quantidade de exp: {}'.format(BDP.nivel['qtdeexp']))
            print('Exp até o préximo level: {}'.format(expproximolv))
            sleep(2.5)

        elif tecla2 in '3':
            habilidades()

        elif tecla2 in '4':
            print('PRÓXIMA ATUALIZAÇÃO! 2.2')


def habilidades():
    while True:
        print('[0] Mostrar habilidades.')
        print('[1] Melhorar habilidade.')
        print('[C] Voltar.')
        while True:
            tecla1 = input('Tecla: ').title()
            if tecla1 in '01C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla1 in 'C':
            break

        if tecla1 in '0':
            print('Habilidade de vendas Lv. {}'.format(BDP.habilidades['Habilidade de vendas']))
            print(f'Habilidade de reduzir preco Lv.{BDP.habilidades["Habilidade de reduzir preco"]}')
            print('Habilidade de lucro Lv.{}'.format(BDP.habilidades['Habilidade de lucro']))
            print('Habilidade de ganhar mais exp Lv.{}'.format(BDP.habilidades['Habilidade de ganhar mais exp']))
            sleep(2)

        elif tecla1 in '1':
            print('Melhorar:')
            valor_habilidadev = BDP.precohabilidade['precohavendas'] * BDP.habilidades['Habilidade de vendas']
            valor_habilidadep = BDP.precohabilidade['precohapreco'] * BDP.habilidades['Habilidade de reduzir preco']
            valor_habilidadel = BDP.precohabilidade['precohalucro'] * BDP.habilidades['Habilidade de lucro']
            valor_habilidadee = BDP.precohabilidade['precohaexp'] * BDP.habilidades['Habilidade de ganhar mais exp']
            print('[0] Habilidade de vendas = {} Diamantes (+1 Venda)'.format(valor_habilidadev))
            print('[1] Habilidade de reduzir preco = {} diamantes (-0.50 Centavos)'.format(valor_habilidadep))
            print('[2] Habilidade de lucro = {} diamantes (+2 Reais)'.format(valor_habilidadel))
            print('[3] Habilidade de ganhar mais exp = {} diamantes (+5 Expêriencia)'.format(valor_habilidadee))
            print('[C] Voltar.')
            while True:
                tecla2 = input('Tecla: ').title()
                if tecla2 in '0123C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla2 in '0':
                if BDP.diamante >= valor_habilidadev:
                    if BDP.habilidades['Habilidade de vendas'] == 10:
                        print('\033[33mErro: \033[mHabilidade no level máximo')
                        sleep(1)

                    else:
                        BDP.habilidades['Habilidade de vendas'] += 1
                        BDP.diamante -= valor_habilidadev
                        print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format
                              (valor_habilidadev))
                        print('Você aumentou o Lv. de habilidade de vendas.')
                        sleep(2)

                else:
                    print('\033[33mErro:  \033[mDiamante insuficiente.')

            elif tecla2 in '1':
                if BDP.diamante >= valor_habilidadep:
                    if BDP.habilidades['Habilidade de reduzir preco'] == 5:
                        print('\033[33mErro: \033[mHabilidade no level máximo')
                        sleep(1)

                    else:
                        BDP.habilidades['Habilidade de reduzir preco'] += 1
                        BDP.diamante -= valor_habilidadep
                        print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format
                              (valor_habilidadep))
                        print('Você aumentou o Lv. de habilidade de reduzir preco.')
                        sleep(2)

                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')

            elif tecla2 in '2':
                if BDP.diamante >= valor_habilidadel:
                    if BDP.habilidades['Habilidade de lucro'] == 10:
                        print('\033[33mErro: \033[mHabilidade no level máximo')
                        sleep(1)

                    else:
                        BDP.habilidades['Habilidade de lucro'] += 1

                        BDP.diamante -= valor_habilidadel
                        print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format(
                            valor_habilidadel))
                        print('Você aumentou o Lv. de habilidade de lucro.')
                        sleep(2)

                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')

            elif tecla2 in '3':
                if BDP.diamante >= valor_habilidadee:
                    if BDP.habilidades['Habilidade de ganhar mais exp'] == 10:
                        print('\033[33mErro: \033[mHabilidade no level máximo')
                        sleep(1)

                    else:
                        BDP.habilidades['Habilidade de ganhar mais exp'] += 1
                        BDP.diamante -= valor_habilidadee
                        BDP.maisexp += 5
                        print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format
                              (valor_habilidadee))
                        print('Você aumentou o Lv. de habilidade de ganhar mais exp.')
                        sleep(2)

                else:
                    print('\033[33mErro: \033[mDiamante insuficiente.')


def sistemalevel():
    while True:
        if BDP.nivel['qtdeexp'] >= BDP.nivel['uplevel']:
            BDP.nivel['uplevel'] *= 2.5
            BDP.nivel['level'] += 1
            print('Up level {}'.format(BDP.nivel['level']))
            sleep(1.5)

        else:
            break


def Abrir_Mercados():
    while True:
        print('[0] Abrir um novo mercado.')
        print('[1] Acessar um mercado existente.')
        print('[C] voltar.')
        while True:
            tecla1 = input('Tecla: ').strip().title()
            if tecla1 in '01C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
        if tecla1 in 'C':
            break
        if tecla1 in '0':
            print('Estado em que seu mercado ficará: ')
            for i in range(len(BDP.mapa)):
                print('[{}] {}'.format(i, BDP.mapa[i]))
            print('[C] Voltar')

            while True:
                tecla2 = input('Tecla: ').title().strip()
                if tecla2 in '0C':
                    break
                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla2 in '0':
                print('Qual será seu imóvel?')
                print('Tipos de Imóveis:')
                for i in range(len(BDP.tipo_de_mercado)):
                    print('[{}] {} = R${}.'.format(i, BDP.tipo_de_mercado[i], BDP.preco_mercado[i]))
                print('[C] Voltar.')
                busca = 10
                busca1 = 10
                while True:
                    tecla3 = input('Tecla: ').title().strip()
                    if tecla3 in '':
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    else:
                        if tecla3 in '0123':
                            busca = BDP.ntipo_de_mercado.index(tecla3)
                            busca1 = BDP.tipo_de_mercado[busca]
                            if BDP.scimoveis[busca1] == 1:
                                print('\033[33mErro: \033[mVoce já tem um(a) {} em Santa Catarina.'.format(busca1))

                            else:
                                break

                        elif tecla3 in 'C':
                            break

                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                if tecla3 in '0123':
                    if BDP.dinheiro >= BDP.preco_mercado[busca]:
                        NomeMercado = input('Nome do imóvel: ').strip()
                        buscam = BDP.sctipo_mercado_info[busca]
                        buscad = BDP.sctipo_deposito_info[busca]
                        BDP.SCTipo_Mercado.append(busca1)
                        BDP.SCNome_Mercado.append(NomeMercado)
                        BDP.SC += 1
                        BDP.scimoveis[busca1] += 1
                        BDP.SCnumeracao_estado.append(BDP.SC)
                        BDP.SCSPTipos_Mercado_Informacoes.append(buscam)
                        BDP.SCSPTipos_Deposito_Informacoes.append(buscad)
                        preco = BDP.preco_mercado[busca]
                        BDP.dinheiro -= preco
                        print('Você teve um gasto de R${} com o imóvel.'.format(preco))
                        sleep(1.5)
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')

        elif tecla1 in '1':
            for i in range(len(BDP.mapa)):
                print('[{}] {}'.format(i, BDP.mapa[i]))
            print('[C] Voltar')
            while True:
                tecla2 = input('Tecla: ').strip().title()
                if tecla2 in '':
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                else:
                    if tecla2 in '0C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            if tecla2 in '0':
                busca = BDP.nmapa.index(tecla2)
                busca1 = BDP.mapa[busca]
                print('{}:'.format(busca1))
                for i in range(len(BDP.SCTipo_Mercado)):
                    print('[{}] {}: \033[36m{}\033[m'.format(i, BDP.SCTipo_Mercado[i], BDP.SCNome_Mercado[i]))
                print('[C] Voltar')
                if not BDP.SCTipo_Mercado:
                    print('\033[33mErro: \033[mSem comércio nesse Estado')
                    sleep(1.5)

                else:
                    while True:
                        tecla3 = str(input('Tecla: ')).upper()
                        if tecla3 in '':
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                        else:
                            if tecla3 in 'C':
                                break
                            else:
                                inteiro = tecla3.isnumeric()
                                strinteiro = str(inteiro)
                                ebool = strinteiro.find('True')
                                if ebool == 0:
                                    tecla3 = int(tecla3)
                            if tecla3 in BDP.SCnumeracao_estado:
                                break
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                    if tecla3 in BDP.SCnumeracao_estado:
                        buscatm = BDP.SCnumeracao_estado.index(tecla3)
                        buscatm1 = BDP.SCTipo_Mercado[buscatm]
                        buscanome = BDP.SCnumeracao_estado.index(tecla3)
                        buscanome1 = BDP.SCNome_Mercado[buscanome]
                        print('Entrando no Imóvel: \033[36m{} \033[m'.format(buscanome1))
                        sleep(2)
                        SCDentro_Mercado(buscatm1, buscanome1)


def SCDentro_Mercado(buscatm1, buscanome1):
    Tipo_Mercado = buscatm1
    Nome_Mercado = buscanome1
    while True:
        if Tipo_Mercado in 'Acougue':
            scvendaacougue()
            scdepositoacougue()
        elif Tipo_Mercado in 'Padaria':
            scvendapadaria()
            scdepositopadaria()
        elif Tipo_Mercado in 'Loja de Eletronica':
            scvendaeletronica()
            scdepositoeletronico()
        elif Tipo_Mercado in 'SuperMercado':
            scvendasupermercado()
            scdepositosupermercado()

        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras')
        print('[1] Contratar Funcionários')
        print('[2] Comprar moedas')
        print('[3] Tentar Vender')
        print('[4] Mostrar {}'.format(Tipo_Mercado))
        print('[C] Sair do Imóvel.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in '01234C':
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if tecla in 'C':
            print('Saindo do Imóvel: \033[36m{} \033[m'.format(Nome_Mercado))
            sleep(2)
            break

        if tecla in '0':
            while True:
                print('[0] Comprar móveis.')
                print('[1] Comprar produtos.')
                print('[C] Voltar.')
                tecla1 = input('Tecla: ').upper().strip()
                if tecla1 in 'C':
                    break

                elif tecla1 in '0':
                    if Tipo_Mercado in 'Acougue':
                        sclojamoveis(buscatm1, buscanome1)
                    elif Tipo_Mercado in 'Padaria':
                        sclojamoveis(buscatm1, buscanome1)
                    elif Tipo_Mercado in 'Loja de Eletronica':
                        sclojamoveis(buscatm1, buscanome1)
                    elif Tipo_Mercado in 'SuperMercado':
                        sclojamoveis(buscatm1, buscanome1)

                elif tecla1 in '1':
                    if Tipo_Mercado in 'Acougue':
                        scmercado(buscatm1, buscanome1)
                    elif Tipo_Mercado in 'Padaria':
                        scmercado(buscatm1, buscanome1)
                    elif Tipo_Mercado in 'Loja de Eletronica':
                        scmercado(buscatm1, buscanome1)
                    elif Tipo_Mercado in 'SuperMercado':
                        scmercado(buscatm1, buscanome1)

                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
        elif tecla in '1':
            if Tipo_Mercado in 'Acougue':
                scfuncionarios(buscatm1)
            elif Tipo_Mercado in 'Padaria':
                scfuncionarios(buscatm1)
            elif Tipo_Mercado in 'Loja de Eletronica':
                scfuncionarios(buscatm1)
            elif Tipo_Mercado in 'SuperMercado':
                scfuncionarios(buscatm1)

        elif tecla in '2':
            comprarmoeda()

        elif tecla in '3':
            if Tipo_Mercado in 'Acougue':
                scvendaacougue()
            elif Tipo_Mercado in 'Padaria':
                scvendapadaria()
            elif Tipo_Mercado in 'Loja de Eletronica':
                scvendaeletronica()
            elif Tipo_Mercado in 'SuperMercado':
                scvendasupermercado()

        elif tecla in '4':
            while True:
                print('[0] Ver saldo.')
                print('[1] Quantidade de móveis.')
                print('[2] Quantidade de produtos na venda.')
                print('[3] Quantidade de produtos no depósito')
                print('[4] Quantidade de vendas.')
                print('[5] Funcionários.')
                print('[C] Voltar')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '012345C':
                        break
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                if tecla2 in 'C':
                    break
                if tecla2 in '0':
                    print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                    print('Dima = {}'.format(BDP.diamante))
                    sleep(1)

                if tecla2 in '1':
                    print('Quantidade de móveis:')
                    sleep(1)
                    if Tipo_Mercado in 'Acougue':
                        for p, moveisacougue in enumerate(BDP.scmoveisacougue):
                            print(f'{moveisacougue} = {BDP.scqtdemoveisacougue[moveisacougue]} '
                                  f'({BDP.sclimiteitensmoveisacougue[p]} produtos) ({BDP.scespacomoveisacougue[p]}'
                                  f' espaço)')

                    elif Tipo_Mercado in 'Padaria':
                        for p, moveispadaria in enumerate(BDP.scmoveispadaria):
                            print(f'{moveispadaria} = {BDP.scqtdemoveispadaria[moveispadaria]} '
                                  f'({BDP.sclimiteitensmoveispadaria[p]} produtos) ({BDP.scespacomoveispadaria[p]}'
                                  f' espaço)')

                    elif Tipo_Mercado in 'Loja de Eletronica':
                        for p, moveiseletronica in enumerate(BDP.scmoveiseletronica):
                            print(f'{moveiseletronica} = {BDP.scqtdemoveiseletronica[moveiseletronica]} '
                                  f'({BDP.sclimiteitensmoveiseletronica[p]} produtos)'
                                  f'({BDP.scespacomoveiseletronico[p]} espaço)')

                    elif Tipo_Mercado in 'SuperMercado':
                        for p, moveissm in enumerate(BDP.scmoveissupermercado):
                            print(f'{moveissm} = {BDP.scqtdemoveissupermercado[moveissm]} '
                                  f'({BDP.sclimiteitensmoveissm[p]} produtos) ({BDP.scespacomoveissm[p]} espaço')
                    sleep(2)

                elif tecla2 in '2':
                    print('Quantidade de produtos na venda:')
                    sleep(2)
                    if Tipo_Mercado in 'Acougue':
                        for produtoacougue in BDP.scqtdeprodutoacougue:
                            print('{} = {}'.format(produtoacougue, BDP.scqtdeprodutoacougue[produtoacougue]))

                    elif Tipo_Mercado in 'Padaria':
                        for produtopadaria in BDP.scqtdeprodutopadaria:
                            print('{} = {}'.format(produtopadaria, BDP.scqtdeprodutopadaria[produtopadaria]))

                    elif Tipo_Mercado in 'Loja de Eletronica':
                        for produtoeletronica in BDP.scqtdeprodutoeletronica:
                            print('{} = {}'.format(produtoeletronica,
                                                   BDP.scqtdeprodutoeletronica[produtoeletronica]))

                    elif Tipo_Mercado in 'SuperMercado':
                        for produtosm in BDP.scqtdeprodutosm:
                            print('{} = {}'.format(produtosm, BDP.scqtdeprodutosm[produtosm]))
                    sleep(2)

                elif tecla2 in '3':
                    print('Quantidade de produtos no depósito:')
                    sleep(2)
                    if Tipo_Mercado in 'Acougue':
                        for depositoacougue in BDP.scqtdeprodepositoacougue:
                            print('{} = {}'.format(depositoacougue, BDP.scqtdeprodepositoacougue[depositoacougue]))

                    elif Tipo_Mercado in 'Padaria':
                        for depositopadaria in BDP.scqtdeprodepositopadaria:
                            print('{} = {}'.format(depositopadaria, BDP.scqtdeprodepositopadaria[depositopadaria]))

                    elif Tipo_Mercado in 'Loja de Eletronica':
                        for depositoeletronico in BDP.scqtdeprodepositoeletronica:
                            print('{} = {}'.format(depositoeletronico,
                                                   BDP.scqtdeprodepositoeletronica[depositoeletronico]))

                    elif Tipo_Mercado in 'SuperMercado':
                        for depositosm in BDP.scqtdeprodepositosm:
                            print('{} = {}'.format(depositosm, BDP.scqtdeprodepositosm[depositosm]))

                    sleep(2)

                elif tecla2 in '4':
                    print('Quantidade de vendas:')
                    sleep(2)
                    if Tipo_Mercado in 'Acougue':
                        for vendaacougue in BDP.scqtdeprovendasacougue:
                            print('{} = {}'.format(vendaacougue, BDP.scqtdeprovendasacougue[vendaacougue]))

                    elif Tipo_Mercado in 'Padaria':
                        for vendapadaria in BDP.scqtdeprovendaspadaria:
                            print('{} = {}'.format(vendapadaria, BDP.scqtdeprovendaspadaria[vendapadaria]))

                    elif Tipo_Mercado in 'Loja de Eletronica':
                        for vendaeletronica in BDP.scqtdeprovendaseletronica:
                            print('{} = {}'.format(vendaeletronica, BDP.scqtdeprovendaseletronica[vendaeletronica]))
                    elif Tipo_Mercado in 'SuperMercado':
                        for vendasm in BDP.scqtdeprovendasupermercado:
                            print('{} = {}'.format(vendasm, BDP.scqtdeprovendasupermercado[vendasm]))
                    sleep(2)

                elif tecla2 in '5':
                    print('Funcionários:')
                    if Tipo_Mercado in 'Acougue':
                        for funciacougue in BDP.scqtdefuncionariosacougue:
                            print('{} = {}'.format(funciacougue, BDP.scqtdefuncionariosacougue[funciacougue]))
                    elif Tipo_Mercado in 'Padaria':
                        for funcipadaria in BDP.scqtdefuncionariospadaria:
                            print('{} = {}'.format(funcipadaria, BDP.scqtdefuncionariospadaria[funcipadaria]))
                    elif Tipo_Mercado in 'Loja de Eletronica':
                        for funcieletronica in BDP.scqtdefuncionarioseletronica:
                            print('{} = {}'.format(funcieletronica, BDP.scqtdefuncionarioseletronica[funcieletronica]))
                    elif Tipo_Mercado in 'SuperMercado':
                        for funcism in BDP.scqtdefuncionariossupermercado:
                            print('{} = {}'.format(funcism, BDP.scqtdefuncionariossupermercado[funcism]))
                    sleep(2)


def scvendaacougue():
    while True:
        sorteio = randint(0, 2)
        qtdevendaslevel = BDP.habilidades['Habilidade de vendas'] * 1
        precoreduzido = BDP.habilidades['Habilidade de reduzir preco'] * 0.50
        lucromaior = BDP.habilidades['Habilidade de lucro'] * 2
        scvendas = BDP.scqtdemoveisacougue['Caixa'] * 2
        scqtdevendas = qtdevendaslevel + scvendas
        if BDP.scqtdemoveisacougue['Caixa'] >= 1:
            if BDP.scqtdefuncoesacougue['Caixa'] >= 1:
                if BDP.scqtdefuncoesacougue['Acougueiro'] >= 1:
                    if sorteio == 0:
                        escolha = choice(BDP.scprodutosacougue)
                        if BDP.scqtdeprodutoacougue[escolha] >= 1:
                            busca = BDP.scprodutosacougue.index(escolha)
                            busca1 = BDP.scprodutosacougue[busca]
                            if BDP.scqtdeprodutoacougue[busca1] >= scqtdevendas:
                                BDP.scqtdeprodutoacougue[busca1] -= scqtdevendas
                                BDP.scqtdeprovendasacougue[busca1] += scqtdevendas
                                precov = (BDP.scprecoacouguev[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecoacouguev[busca] + lucromaior
                                npc = BDP.scprecoacouguec[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['scacougue'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                sleep(4)
                            else:
                                scqtdevendas = BDP.scqtdeprodutoacougue[busca1]
                                BDP.scqtdeprodutoacougue[busca1] -= scqtdevendas
                                BDP.scqtdeprovendasacougue[busca1] += scqtdevendas
                                precov = (BDP.scprecoacouguev[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecoacouguev[busca] + lucromaior
                                npc = BDP.scprecoacouguec[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['scacougue'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                sleep(4)
                        break
                else:
                    print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função açougueiro.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
                    break
            else:
                print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
                break
        else:
            print('\033[33mErro: \033[mVocê não tem um Caixa.')
            print('Vá para a loja de móveis.')
            sleep(2)
            break


def scvendapadaria():
    while True:
        sorteio = randint(0, 2)
        qtdevendaslevel = BDP.habilidades['Habilidade de vendas'] * 1
        precoreduzido = BDP.habilidades['Habilidade de reduzir preco'] * 0.50
        lucromaior = BDP.habilidades['Habilidade de lucro'] * 2
        scvendas = BDP.scqtdemoveispadaria['Caixa'] * 2
        scqtdevendas = qtdevendaslevel + scvendas
        if BDP.scqtdemoveispadaria['Caixa'] >= 1:
            if BDP.scqtdefuncoespadaria['Caixa'] >= 1:
                if BDP.scqtdefuncoespadaria['Padeiro'] >= 1:
                    if sorteio == 0:
                        escolha = choice(BDP.scprodutospadaria)
                        if BDP.scqtdeprodutopadaria[escolha] >= 1:
                            busca = BDP.scprodutospadaria.index(escolha)
                            busca1 = BDP.scprodutospadaria[busca]
                            if BDP.scqtdeprodutopadaria[busca1] >= scqtdevendas:
                                BDP.scqtdeprodutopadaria[busca1] -= scqtdevendas
                                BDP.scqtdeprovendaspadaria[busca1] += scqtdevendas
                                precov = (BDP.scprecopadariav[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecopadariav[busca] + lucromaior
                                npc = BDP.scprecopadariac[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['scpadaria'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                sleep(4)
                            else:
                                scqtdevendas = BDP.scqtdeprodutopadaria[busca1]
                                BDP.scqtdeprodutopadaria[busca1] -= scqtdevendas
                                BDP.scqtdeprovendaspadaria[busca1] += scqtdevendas
                                precov = (BDP.scprecopadariav[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecopadariav[busca] + lucromaior
                                npc = BDP.scprecopadariac[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['scpadaria'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Voce vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('voce teve um lucro de R${:.2f}'.format(lucro))
                                print('Voce ganhou {} exp'.format(somaexp))
                                sleep(4)
                        break
                else:
                    print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função padeiro.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
                    break
            else:
                print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
                break
        else:
            print('\033[33mErro: \033[mVocê não tem um Caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
            break


def scvendaeletronica():
    while True:
        sorteio = randint(0, 2)
        qtdevendaslevel = BDP.habilidades['Habilidade de vendas'] * 1
        precoreduzido = BDP.habilidades['Habilidade de reduzir preco'] * 0.50
        lucromaior = BDP.habilidades['Habilidade de lucro'] * 2
        scvenda = BDP.scqtdemoveiseletronica['Caixa'] * 2
        scqtdevendas = qtdevendaslevel + scvenda
        if BDP.scqtdemoveiseletronica['Caixa'] >= 1:
            if BDP.scqtdefuncoeseletronica['Caixa'] >= 1:
                if BDP.scqtdefuncoeseletronica['Atendente'] >= 1:
                    if sorteio == 0:
                        escolha = choice(BDP.scprodutoseletronica)
                        if BDP.scqtdeprodutoeletronica[escolha] >= 1:
                            busca = BDP.scprodutoseletronica.index(escolha)
                            busca1 = BDP.scprodutoseletronica[busca]
                            if BDP.scqtdeprodutoeletronica[busca1] >= scqtdevendas:
                                BDP.scqtdeprodutoeletronica[busca1] -= scqtdevendas
                                BDP.scqtdeprovendaseletronica[busca1] += scqtdevendas
                                precov = (BDP.scprecoeletronicav[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecoeletronicav[busca] + lucromaior
                                npc = BDP.scprecoeletronicac[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['sclojaele'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                sleep(4)
                            else:
                                scqtdevendas = BDP.scqtdeprodutoeletronica[busca1]
                                BDP.scqtdeprodutoeletronica[busca1] -= scqtdevendas
                                BDP.scqtdeprovendaseletronica[busca1] += scqtdevendas
                                precov = (BDP.scprecoeletronicav[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecoeletronicav[busca] + lucromaior
                                npc = BDP.scprecoeletronicac[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['sclojaele'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                sleep(4)
                        break
                else:
                    print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função atendente.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
                    break
            else:
                print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
                break
        else:
            print('\033[33mErro: \033[mVocê não tem um caixa.')
            print('Vá para a loja de móveis.')
            sleep(2)
            break


def scvendasupermercado():
    while True:
        sorteio = randint(0, 2)
        qtdevendaslevel = BDP.habilidades['Habilidade de vendas'] * 1
        precoreduzido = BDP.habilidades['Habilidade de reduzir preco'] * 0.50
        lucromaior = BDP.habilidades['Habilidade de lucro'] * 2
        scvenda = BDP.scqtdemoveissupermercado['Caixa'] * 2
        scqtdevendas = qtdevendaslevel + scvenda
        if BDP.scqtdemoveissupermercado['Caixa'] >= 1:
            if BDP.scqtdefuncoessupermercado['Caixa'] >= 1:
                if BDP.scqtdefuncoessupermercado['Repositor'] >= 1:
                    if sorteio == 0:
                        escolha = choice(BDP.scprodutossm)
                        if BDP.scqtdeprodutosm[escolha] >= 1:
                            busca = BDP.scprodutossm.index(escolha)
                            busca1 = BDP.scprodutossm[busca]
                            if BDP.scqtdeprodutosm[busca1] >= scqtdevendas:
                                BDP.scqtdeprodutosm[busca1] -= scqtdevendas
                                BDP.scqtdeprovendasupermercado[busca1] += scqtdevendas
                                precov = (BDP.scprecovendasm[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecovendasm[busca] + lucromaior
                                npc = BDP.scprecocomprasm[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['scsm'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                sleep(4)
                            else:
                                scqtdevendas = BDP.scqtdeprodutosm[busca1]
                                BDP.scqtdeprovendasupermercado[busca1] += scqtdevendas
                                precov = (BDP.scprecovendasm[busca] + lucromaior) * scqtdevendas
                                BDP.dinheiro += precov
                                npv = BDP.scprecovendasm[busca] + lucromaior
                                npc = BDP.scprecocomprasm[busca] - precoreduzido
                                lucro = (npv - npc) * scqtdevendas
                                BDP.lucro['scsm'] += lucro
                                somaexp = (20 + BDP.maisexp) * scqtdevendas
                                BDP.nivel['qtdeexp'] += somaexp
                                print('Você vendeu {} {} por R${:.2f}'.format(scqtdevendas, busca1, precov))
                                print('você teve um lucro de R${:.2f}'.format(lucro))
                                print('Você ganhou {} exp'.format(somaexp))
                                BDP.scqtdeprodutosm[busca1] -= BDP.scqtdeprodutosm[busca1]
                                sleep(4)
                        break
                else:
                    print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função repositor.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
                    break
            else:
                print('\033[33mErro: \033[mVocê não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
                break
        else:
            print('\033[33mErro: \033[mVocê não tem um caixa.')
            print('Vá para a loja de móveis.')
            sleep(2)
            break


def scdepositoacougue():
    quantisaidadeposito = 0

    for pos, cont in enumerate(BDP.scnmoveisa):
        buscamoveis = BDP.scnmoveisa.index(cont)
        busca1moveis = BDP.scmoveisacougue[buscamoveis]
        busca2moveis = BDP.sclimiteitensmoveisacougue[pos]
        if BDP.scqtdemoveisacougue[busca1moveis] >= 1:
            quantisaidadeposito += busca2moveis * BDP.scqtdemoveisacougue[busca1moveis]

    for pos, cont in enumerate(BDP.scnpa):
        quantiproduto = 0  # quantidade que cabe no açougue
        for conta in BDP.scprodutosacougue:
            quantiproduto += BDP.scqtdeprodutoacougue[conta]
        falta = quantisaidadeposito - quantiproduto
        buscaitem = BDP.scnpa.index(cont)
        buscad = BDP.scprodutosacougue[buscaitem]
        if BDP.scqtdeprodepositoacougue[buscad] >= 1:
            if BDP.scqtdeprodepositoacougue[buscad] >= falta:
                BDP.scqtdeprodutoacougue[buscad] += falta
                BDP.scqtdeprodepositoacougue[buscad] -= falta

            elif BDP.scqtdeprodepositoacougue[buscad] < falta:
                BDP.scqtdeprodutoacougue[buscad] += BDP.scqtdeprodepositoacougue[buscad]
                BDP.scqtdeprodepositoacougue[buscad] -= BDP.scqtdeprodepositoacougue[buscad]


def scdepositopadaria():
    boleira = BDP.scqtdemoveispadaria['Boleira'] * BDP.sclimiteitensmoveispadaria[1]

    mesap = BDP.scqtdemoveispadaria['MesaP'] * BDP.sclimiteitensmoveispadaria[2]
    mesam = BDP.scqtdemoveispadaria['MesaM'] * BDP.sclimiteitensmoveispadaria[3]
    mesag = BDP.scqtdemoveispadaria['MesaG'] * BDP.sclimiteitensmoveispadaria[4]
    saidamesa = mesap + mesam + mesag

    geladeirap = BDP.scqtdemoveispadaria['GeladeiraP'] * BDP.sclimiteitensmoveispadaria[5]
    geladeiram = BDP.scqtdemoveispadaria['GeladeiraM'] * BDP.sclimiteitensmoveispadaria[6]
    geladeirag = BDP.scqtdemoveispadaria['GeladeiraG'] * BDP.sclimiteitensmoveispadaria[7]
    saidageladeira = geladeirap + geladeiram + geladeirag

    pasteleirap = BDP.scqtdemoveispadaria['PasteleiraP'] * BDP.sclimiteitensmoveispadaria[8]
    pasteleiram = BDP.scqtdemoveispadaria['PasteleiraM'] * BDP.sclimiteitensmoveispadaria[9]
    pasteleirag = BDP.scqtdemoveispadaria['PasteleiraG'] * BDP.sclimiteitensmoveispadaria[10]
    saidapasteleira = pasteleirap + pasteleiram + pasteleirag

    prateleirap = BDP.scqtdemoveispadaria['PrateleiraP'] * BDP.sclimiteitensmoveispadaria[11]
    prateleiram = BDP.scqtdemoveispadaria['PrateleiraM'] * BDP.sclimiteitensmoveispadaria[12]
    prateleirag = BDP.scqtdemoveispadaria['PrateleiraG'] * BDP.sclimiteitensmoveispadaria[13]
    saidaprateleira = prateleirap + prateleiram + prateleirag

    for i in BDP.scprodutospadaria:
        busca = BDP.scprodutospadaria.index(i)
        buscad = BDP.scprodutospadaria[busca]

        if BDP.scqtdeprodepositopadaria[buscad] >= 1:
            if 'Bolo' in buscad:
                bolo = BDP.scqtdeprodutopadaria['Bolo']
                faltaboleira = boleira - bolo
                if BDP.scqtdeprodepositopadaria[buscad] >= faltaboleira:
                    BDP.scqtdeprodutopadaria[buscad] += faltaboleira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltaboleira

                elif BDP.scqtdeprodepositopadaria[buscad] < faltaboleira:
                    BDP.scqtdeprodutopadaria[buscad] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]

            elif buscad in 'Cuca' or buscad in 'Pao' or 'Rosquinha' in buscad:
                produtosmesa = (BDP.scqtdeprodutopadaria['Cuca'] + BDP.scqtdeprodutopadaria['Pao'] +
                                BDP.scqtdeprodutopadaria['Rosquinha'])
                faltamesa = saidamesa - produtosmesa
                if BDP.scqtdeprodepositopadaria[buscad] >= faltamesa:
                    BDP.scqtdeprodutopadaria[buscad] += faltamesa
                    BDP.scqtdeprodepositopadaria[buscad] -= faltamesa

                elif BDP.scqtdeprodepositopadaria[buscad] < faltamesa:
                    BDP.scqtdeprodutopadaria[buscad] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]

            if buscad in 'Bolinho' or buscad in 'Coxinha' or buscad in 'Pao_de_queijo' or 'Pastel' in buscad:
                produtospasteleira = (BDP.scqtdeprodutopadaria['Bolinho'] + BDP.scqtdeprodutopadaria['Coxinha'] +
                                      BDP.scqtdeprodutopadaria['Pao_de_queijo'] + BDP.scqtdeprodutopadaria['Pastel'])

                faltapasteleira = saidapasteleira - produtospasteleira
                if BDP.scqtdeprodepositopadaria[buscad] >= faltapasteleira:
                    BDP.scqtdeprodutopadaria[buscad] += faltapasteleira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltapasteleira

                elif BDP.scqtdeprodepositopadaria[buscad] < faltapasteleira:
                    BDP.scqtdeprodutopadaria[buscad] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]

            if buscad in 'Bolacha' or 'Cafe' in buscad:
                produtosprateleira = BDP.scqtdeprodutopadaria['Bolacha'] + BDP.scqtdeprodutopadaria['Cafe']
                faltaprateleira = saidaprateleira - produtosprateleira
                if BDP.scqtdeprodepositopadaria[buscad] >= faltaprateleira:
                    BDP.scqtdeprodutopadaria[buscad] += faltaprateleira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltaprateleira

                elif BDP.scqtdeprodepositopadaria[buscad] < faltaprateleira:
                    BDP.scqtdeprodutopadaria[buscad] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]

            if (buscad in 'Leite' or buscad in 'Margarina' or buscad in 'Nata' or buscad in 'Presunto' or
                    buscad in 'Queijo' or buscad in 'Sorvete' or 'Yogurt' in buscad):
                produtosgeladeira = (BDP.scqtdeprodutopadaria['Leite'] + BDP.scqtdeprodutopadaria['Margarina'] +
                                     BDP.scqtdeprodutopadaria['Nata'] + BDP.scqtdeprodutopadaria['Presunto'] +
                                     BDP.scqtdeprodutopadaria['Queijo'] + BDP.scqtdeprodutopadaria['Sorvete'] +
                                     BDP.scqtdeprodutopadaria['Yogurt'])

                faltageladeira = saidageladeira - produtosgeladeira
                if BDP.scqtdeprodepositopadaria[buscad] >= faltageladeira:
                    BDP.scqtdeprodutopadaria[buscad] += faltageladeira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltageladeira

                elif BDP.scqtdeprodepositopadaria[buscad] < faltageladeira:
                    BDP.scqtdeprodutopadaria[buscad] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]


def scdepositoeletronico():
    saidamesap = BDP.sclimiteitensmoveiseletronica[1] * BDP.scqtdemoveiseletronica['MesaP']
    saidamesam = BDP.sclimiteitensmoveiseletronica[2] * BDP.scqtdemoveiseletronica['MesaM']
    saidamesag = BDP.sclimiteitensmoveiseletronica[3] * BDP.scqtdemoveiseletronica['MesaG']
    saidamesa = saidamesap + saidamesam + saidamesag

    saidaprateleirap = BDP.sclimiteitensmoveiseletronica[4] * BDP.scqtdemoveiseletronica['PrateleiraP']
    saidaprateleiram = BDP.sclimiteitensmoveiseletronica[5] * BDP.scqtdemoveiseletronica['PrateleiraM']
    saidaprateleirag = BDP.sclimiteitensmoveiseletronica[6] * BDP.scqtdemoveiseletronica['PrateleiraG']
    saidaprateleira = saidaprateleirap + saidaprateleiram + saidaprateleirag

    for i in BDP.scnpe:
        buscaitem = BDP.scnpe.index(i)
        buscad = BDP.scprodutoseletronica[buscaitem]

        if BDP.scqtdeprodepositoeletronica[buscad] >= 1:
            if (buscad in 'Celular' or buscad in 'Computador' or buscad in 'Notebook' or buscad in 'Tablet' or
                    'Televisao' in buscad):

                produtosmesa = (BDP.scqtdeprodutoeletronica['Celular'] + BDP.scqtdeprodutoeletronica['Computador'] +
                                BDP.scqtdeprodutoeletronica['Notebook'] + BDP.scqtdeprodutoeletronica['Tablet'] +
                                BDP.scqtdeprodutoeletronica['Televisao'])
                faltamesa = saidamesa - produtosmesa

                if BDP.scqtdeprodepositoeletronica[buscad] >= faltamesa:
                    BDP.scqtdeprodutoeletronica[buscad] += faltamesa
                    BDP.scqtdeprodepositoeletronica[buscad] -= faltamesa

                elif BDP.scqtdeprodepositoeletronica[buscad] < faltamesa:
                    BDP.scqtdeprodutoeletronica[buscad] += BDP.scqtdeprodepositoeletronica[buscad]
                    BDP.scqtdeprodepositoeletronica[buscad] -= BDP.scqtdeprodepositoeletronica[buscad]

            elif buscad in 'Ipad' or buscad in 'Mouse' or 'Teclado' in buscad:
                produtosprateleira = (BDP.scqtdeprodutoeletronica['Ipad'] + BDP.scqtdeprodutoeletronica['Mouse'] +
                                      BDP.scqtdeprodutoeletronica['Teclado'])
                faltaprateleira = saidaprateleira - produtosprateleira

                if BDP.scqtdeprodepositoeletronica[buscad] >= faltaprateleira:
                    BDP.scqtdeprodutoeletronica[buscad] += faltaprateleira
                    BDP.scqtdeprodepositoeletronica[buscad] -= faltaprateleira

                elif BDP.scqtdeprodepositoeletronica[buscad] < faltaprateleira:
                    BDP.scqtdeprodutoeletronica[buscad] += BDP.scqtdeprodepositoeletronica[buscad]
                    BDP.scqtdeprodepositoeletronica[buscad] -= BDP.scqtdeprodepositoeletronica[buscad]


def scdepositosupermercado():
    saidafruteirap = BDP.sclimiteitensmoveissm[1] * BDP.scqtdemoveissupermercado['FruteiraP']
    saidafruteiram = BDP.sclimiteitensmoveissm[2] * BDP.scqtdemoveissupermercado['FruteiraM']
    saidafruteirag = BDP.sclimiteitensmoveissm[3] * BDP.scqtdemoveissupermercado['FruteiraG']
    saidafruteira = saidafruteirap + saidafruteiram + saidafruteirag

    saidaprateleirap = BDP.sclimiteitensmoveissm[4] * BDP.scqtdemoveissupermercado['PrateleiraP']
    saidaprateleiram = BDP.sclimiteitensmoveissm[5] * BDP.scqtdemoveissupermercado['PrateleiraM']
    saidaprateleirag = BDP.sclimiteitensmoveissm[6] * BDP.scqtdemoveissupermercado['PrateleiraG']
    saidaprateleira = saidaprateleirap + saidaprateleiram + saidaprateleirag

    for i in BDP.scnprodutossm:
        somafv = 0
        somalhg = 0
        for nprodutos in BDP.scnprodutossm:
            busca = BDP.scnprodutossm.index(nprodutos)
            busca1 = BDP.scprodutossm[busca]
            if busca1 in BDP.scprodutossupermercadofv:
                somafv += BDP.scqtdeprodutosm[busca1]
            elif busca1 in BDP.scprodutossupermercadolh or BDP.scprodutossupermercadog:
                somalhg += BDP.scqtdeprodutosm[busca1]

        buscaitem = BDP.scnprodutossm.index(i)
        buscad = BDP.scprodutossm[buscaitem]
        if BDP.scqtdeprodepositosm[buscad] >= 1:
            if buscad in BDP.scprodutossupermercadofv:
                faltafruteira = saidafruteira - somafv
                if BDP.scqtdeprodepositosm[buscad] >= faltafruteira:
                    BDP.scqtdeprodutosm[buscad] += faltafruteira
                    BDP.scqtdeprodepositosm[buscad] -= faltafruteira

                elif BDP.scqtdeprodepositosm[buscad] < faltafruteira:
                    BDP.scqtdeprodutosm[buscad] += BDP.scqtdeprodepositosm[buscad]
                    BDP.scqtdeprodepositosm[buscad] -= BDP.scqtdeprodepositosm[buscad]

            if buscad in BDP.scprodutossupermercadolh or buscad in BDP.scprodutossupermercadog:
                faltaprateleira = saidaprateleira - somalhg
                if BDP.scqtdeprodepositosm[buscad] >= faltaprateleira:
                    BDP.scqtdeprodutosm[buscad] += faltaprateleira
                    BDP.scqtdeprodepositosm[buscad] -= faltaprateleira

                elif BDP.scqtdeprodepositosm[buscad] < faltaprateleira:
                    BDP.scqtdeprodutosm[buscad] += BDP.scqtdeprodepositosm[buscad]
                    BDP.scqtdeprodepositosm[buscad] -= BDP.scqtdeprodepositosm[buscad]


def sclojamoveis(buscatm1, buscanome1):
    while True:
        Tipo_Mercado = buscatm1
        Nome_Mercado = buscanome1
        print('==' * 10)
        print('\033[34mLoja de Móveis:\033[m')
        print('==' * 10)
        sleep(1)

        if Tipo_Mercado in 'Acougue':
            for i in range(len(BDP.scmoveisacougue)):
                print(f'[{i}] {BDP.scmoveisacougue[i]} ({BDP.sclimiteitensmoveisacougue[i]} produtos)'
                      f' ({BDP.scespacomoveisacougue[i]} espaço) R${BDP.scprecomoveisacougue[i]}.')

        elif Tipo_Mercado in 'Padaria':
            for i in range(len(BDP.scmoveispadaria)):
                print(f'[{i}] {BDP.scmoveispadaria[i]} ({BDP.sclimiteitensmoveispadaria[i]} produtos)'
                      f' ({BDP.scespacomoveispadaria[i]} espaço) R${BDP.scprecomoveispadaria[i]}.')

        elif Tipo_Mercado in 'Loja de Eletronica':
            for i in range(len(BDP.scmoveiseletronica)):
                print(f'[{i}] {BDP.scmoveiseletronica[i]} ({BDP.sclimiteitensmoveiseletronica[i]} produtos)'
                      f' ({BDP.scespacomoveiseletronico[i]} espaço) R${BDP.scprecomoveiseletronica[i]}.')

        elif Tipo_Mercado in 'SuperMercado':
            for i in range(len(BDP.scmoveissupermercado)):
                print(
                    f'[{i}] {BDP.scmoveissupermercado[i]} ({BDP.sclimiteitensmoveissm[i]} produtos)'
                    f' ({BDP.scespacomoveissm[i]} espaço) R${BDP.scprecomoveissupermercado[i]}.')

        print('[C] voltar.')
        while True:
            compramoveis1 = input(f'Que Móveis você quer comprar para a(o) {Nome_Mercado}: ').strip(' ').title()
            if compramoveis1 in '':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            else:
                if Tipo_Mercado in 'Acougue' and compramoveis1 in BDP.scnmoveisa or compramoveis1 in 'C':
                    break

                elif Tipo_Mercado in 'Padaria' and compramoveis1 in BDP.scnmoveisp or compramoveis1 in 'C':
                    break

                elif Tipo_Mercado in 'Loja de Eletronica' and compramoveis1 in BDP.scnmoveise or compramoveis1 in 'C':
                    break

                elif Tipo_Mercado in 'SuperMercado' and compramoveis1 in BDP.scnmoveiss or compramoveis1 in 'C':
                    break

                else:
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if compramoveis1 in 'C':
            break

        custol = tamanhofalta = espaco = 0
        busca1moveis = ''

        if Tipo_Mercado in 'Acougue':
            buscamoveis = BDP.scnmoveisa.index(compramoveis1)
            busca1moveis = BDP.scmoveisacougue[buscamoveis]
            custol = BDP.scprecomoveisacougue[buscamoveis]
            espaco = BDP.scespacomoveisacougue[buscamoveis]
            tamanhofalta = BDP.limiteevolucaoimovel['scacougue'] - BDP.tamanhoocupado['scacougue']

        elif Tipo_Mercado in 'Padaria':
            buscamoveis = BDP.scnmoveisp.index(compramoveis1)
            busca1moveis = BDP.scmoveispadaria[buscamoveis]
            custol = BDP.scprecomoveispadaria[buscamoveis]
            espaco = BDP.scespacomoveispadaria[buscamoveis]
            tamanhofalta = BDP.limiteevolucaoimovel['scpadaria'] - BDP.tamanhoocupado['scpadaria']

        elif Tipo_Mercado in 'Loja de Eletronica':
            buscamoveis = BDP.scnmoveise.index(compramoveis1)
            busca1moveis = BDP.scmoveiseletronica[buscamoveis]
            custol = BDP.scprecomoveiseletronica[buscamoveis]
            espaco = BDP.scespacomoveiseletronico[buscamoveis]
            tamanhofalta = BDP.limiteevolucaoimovel['sclojaele'] - BDP.tamanhoocupado['sclojaele']

        elif Tipo_Mercado in 'SuperMercado':
            buscamoveis = BDP.scnmoveiss.index(compramoveis1)
            busca1moveis = BDP.scmoveissupermercado[buscamoveis]
            custol = BDP.scprecomoveissupermercado[buscamoveis]
            espaco = BDP.scespacomoveissm[buscamoveis]
            tamanhofalta = BDP.limiteevolucaoimovel['scsm'] - BDP.tamanhoocupado['scsm']

        qtdemaxima = BDP.dinheiro / custol
        qtdecompra = tamanhofalta / espaco
        while True:
            if qtdemaxima < qtdecompra:
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            else:
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdecompra)))
            quantimoveis1 = str(input('Quantidade de {}: '.format(busca1moveis)))
            numeric = quantimoveis1.isnumeric()
            strnumeric = str(numeric)
            ebool = strnumeric.find('False')
            strfind = str(ebool)
            if strfind in '0':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                sleep(1)
            else:
                quantimoveis1 = int(quantimoveis1)
                tamanho = espaco * quantimoveis1
                if tamanho > tamanhofalta:
                    print('\033[33mErro: \033[m{} cheio.'.format(Tipo_Mercado))
                else:
                    valortotal = custol * quantimoveis1
                    if BDP.dinheiro >= valortotal:
                        BDP.dinheiro -= valortotal
                        break

                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')

        print('Na loja de móveis, o móvel {} custa R${} cada.'
              ' totalizando R${:.2f} com {} móveis.'.format(busca1moveis, custol, valortotal, quantimoveis1))
        sleep(3)

        if Tipo_Mercado in 'Acougue':
            BDP.scqtdemoveisacougue[busca1moveis] += quantimoveis1
            BDP.tamanhoocupado['scacougue'] += tamanho

        elif Tipo_Mercado in 'Padaria':
            BDP.scqtdemoveispadaria[busca1moveis] += quantimoveis1
            BDP.tamanhoocupado['scpadaria'] += tamanho

        elif Tipo_Mercado in 'Loja de Eletronica':
            BDP.scqtdemoveiseletronica[busca1moveis] += quantimoveis1
            BDP.tamanhoocupado['sclojaele'] += tamanho

        elif Tipo_Mercado in 'SuperMercado':
            BDP.scqtdemoveissupermercado[busca1moveis] += quantimoveis1
            BDP.tamanhoocupado['scsm'] += tamanho


def scmercado(buscatm1, buscanome1):
    while True:
        Tipo_Mercado = buscatm1
        Nome_Mercado = buscanome1
        print('==' * 10)
        print('\033[34mMercado Do Zé:\033[m')
        print('==' * 10)
        sleep(1)
        precoreduzido = BDP.habilidades['Habilidade de reduzir preco'] * 0.50

        if Tipo_Mercado in 'Acougue':
            for i in range(len(BDP.scprodutosacougue)):
                print('[{}] {} R${}.'.format(i, BDP.scprodutosacougue[i], BDP.scprecoacouguec[i] - precoreduzido))

        elif Tipo_Mercado in 'Padaria':
            for i in range(len(BDP.scprodutospadaria)):
                print('[{}] {} R${}.'.format(i, BDP.scprodutospadaria[i], BDP.scprecopadariac[i] - precoreduzido))

        elif Tipo_Mercado in 'Loja de Eletronica':
            for i in range(len(BDP.scprodutoseletronica)):
                print('[{}] {} R${}.'.format(i, BDP.scprodutoseletronica[i], BDP.scprecoeletronicac[i] - precoreduzido))

        elif Tipo_Mercado in 'SuperMercado':
            for i in range(len(BDP.scprodutossm)):
                print('[{}] {} R${}.'.format(i, BDP.scprodutossm[i], BDP.scprecocomprasm[i] - precoreduzido))

        print('[C] Voltar.')
        custo = 0
        buscaitem = ''
        while True:
            compraproduto1 = input(f'Que produto você quer comprar para a(o) {Nome_Mercado}: ').strip(' ').title()
            if compraproduto1 in '':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif compraproduto1 in 'C':
                break

            else:
                if Tipo_Mercado in 'Acougue':
                    if compraproduto1 in BDP.scnpa:
                        if (BDP.scqtdemoveisacougue['FreezerP'] or BDP.scqtdemoveisacougue['FreezerM'] or
                                BDP.scqtdemoveisacougue['FreezerG'] >= 1):
                            buscamercado = BDP.scnpa.index(compraproduto1)
                            buscaitem = BDP.scprodutosacougue[buscamercado]
                            custo = BDP.scprecoacouguec[buscamercado] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem um freezer.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                elif Tipo_Mercado in 'Padaria':
                    pasteleira = ['1', '4', '10', '11']
                    prateleira = ['0', '3']
                    mesa = ['5', '9', '14']
                    geladeira = ['6', '7', '8', '12', '13', '15', '16']

                    if compraproduto1 in pasteleira:
                        if (BDP.scqtdemoveispadaria['PasteleiraP'] or BDP.scqtdemoveispadaria['PasteleiraM'] or
                                BDP.scqtdemoveispadaria['PasteleiraG'] >= 1):
                            buscamercado = BDP.scnpp.index(compraproduto1)
                            buscaitem = BDP.scprodutospadaria[buscamercado]
                            custo = BDP.scprecopadariac[buscamercado] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma pasteleira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

                    elif compraproduto1 in '2':
                        if BDP.scqtdemoveispadaria['Boleira'] >= 1:
                            buscamercado = BDP.scnpp.index(compraproduto1)
                            buscaitem = BDP.scprodutospadaria[buscamercado]
                            custo = BDP.scprecopadariac[buscamercado] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma boleira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

                    elif compraproduto1 in prateleira:
                        if (BDP.scqtdemoveispadaria['PrateleiraP'] or BDP.scqtdemoveispadaria['PrateleiraM'] or
                                BDP.scqtdemoveispadaria['PrateleiraG'] >= 1):
                            buscamercado = BDP.scnpp.index(compraproduto1)
                            buscaitem = BDP.scprodutospadaria[buscamercado]
                            custo = BDP.scprecopadariac[buscamercado] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

                    elif compraproduto1 in mesa:
                        if (BDP.scqtdemoveispadaria['MesaP'] or BDP.scqtdemoveispadaria['MesaM'] or
                                BDP.scqtdemoveispadaria['MesaG'] >= 1):
                            buscamercado = BDP.scnpp.index(compraproduto1)
                            buscaitem = BDP.scprodutospadaria[buscamercado]
                            custo = BDP.scprecopadariac[buscamercado] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma mesa.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

                    elif compraproduto1 in geladeira:
                        if (BDP.scqtdemoveispadaria['GeladeiraP'] or BDP.scqtdemoveispadaria['GeladeiraM'] or
                                BDP.scqtdemoveispadaria['GeladeiraG'] >= 1):
                            buscamercado = BDP.scnpp.index(compraproduto1)
                            buscaitem = BDP.scprodutospadaria[buscamercado]
                            custo = BDP.scprecopadariac[buscamercado] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma geladeira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                elif Tipo_Mercado in 'Loja de Eletronica':
                    mesa = ['0', '1', '4', '5', '7']
                    prateleira = ['2', '3', '6']
                    if compraproduto1 in mesa:
                        if (BDP.scqtdemoveiseletronica['MesaP'] or BDP.scqtdemoveiseletronica['MesaM'] or
                                BDP.scqtdemoveiseletronica['MesaG'] >= 1):
                            busca = BDP.scnpe.index(compraproduto1)
                            buscaitem = BDP.scprodutoseletronica[busca]
                            custo = BDP.scprecoeletronicac[busca] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma mesa.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

                    elif compraproduto1 in prateleira:
                        if (BDP.scqtdemoveiseletronica['PrateleiraP'] or BDP.scqtdemoveiseletronica['PrateleiraM'] or
                                BDP.scqtdemoveiseletronica['PrateleiraG'] >= 1):
                            busca = BDP.scnpe.index(compraproduto1)
                            buscaitem = BDP.scprodutoseletronica[busca]
                            custo = BDP.scprecoeletronicac[busca] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)
                    else:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                elif Tipo_Mercado in 'SuperMercado':
                    if compraproduto1 in BDP.scnpsfv:
                        if (BDP.scqtdemoveissupermercado['FruteiraP'] or BDP.scqtdemoveissupermercado['FruteiraM'] or
                                BDP.scqtdemoveissupermercado['FruteiraG'] >= 1):
                            busca = BDP.scnpsfv.index(compraproduto1)
                            buscaitem = BDP.scprodutossupermercadofv[busca]
                            custo = BDP.scprecosupermercadocfv[busca] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma fruteira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

                    elif compraproduto1 in BDP.scnpslh or compraproduto1 in BDP.scnpsg:
                        if (BDP.scqtdemoveissupermercado['PrateleiraP'] or BDP.scqtdemoveissupermercado['PrateleiraM']
                                or BDP.scqtdemoveissupermercado['PrateleiraG'] >= 1):
                            produtoslhg = BDP.scprodutossupermercadolh + BDP.scprodutossupermercadog
                            nprodutoslhg = BDP.scnpslh + BDP.scnpsg
                            precoprodutoslhg = BDP.scprecosupermercadoclh + BDP.scprecosupermercadocg
                            busca = nprodutoslhg.index(compraproduto1)
                            buscaitem = produtoslhg[busca]
                            custo = precoprodutoslhg[busca] - precoreduzido
                            break
                        else:
                            print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                            print('Vá para uma loja de móveis.')
                            sleep(3)

        if compraproduto1 in 'C':
            break

        else:
            maxima = 0
            if Tipo_Mercado in 'Acougue':
                qtdemaximaproduto = 0
                for qtde in BDP.scprodutosacougue:
                    qtdemaximaproduto += BDP.scqtdeprodepositoacougue[qtde]
                maxima = BDP.limiteevolucaoimovel['scacougued'] - qtdemaximaproduto

            elif Tipo_Mercado in 'Padaria':
                qtdemaximaproduto = 0
                for qtde in BDP.scprodutospadaria:
                    qtdemaximaproduto += BDP.scqtdeprodepositopadaria[qtde]
                maxima = BDP.limiteevolucaoimovel['scpadariad'] - qtdemaximaproduto

            elif Tipo_Mercado in 'Loja de Eletronica':
                qtdemaximaproduto = 0
                for qtde in BDP.scprodutoseletronica:
                    qtdemaximaproduto += BDP.scqtdeprodepositoeletronica[qtde]
                maxima = BDP.limiteevolucaoimovel['sclojaeled'] - qtdemaximaproduto

            elif Tipo_Mercado in 'SuperMercado':
                qtdemaximaproduto = 0
                for qtde in BDP.scprodutossm:
                    qtdemaximaproduto += BDP.scqtdeprodepositosm[qtde]
                maxima = BDP.limiteevolucaoimovel['scsmd'] - qtdemaximaproduto

            qtdemaxima = BDP.dinheiro / custo
            while True:
                if qtdemaxima < maxima:
                    print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                else:
                    print('Compra máxima de {:.0f} unidade'.format(trunc(maxima)))
                quantiproduto = str(input('Quantidade de {}: '.format(buscaitem)))
                numeric = quantiproduto.isnumeric()
                strnumeric = str(numeric)
                ebool = strnumeric.find('False')
                strfind = str(ebool)
                if strfind in '0':
                    print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    sleep(1)
                else:
                    quantiproduto = int(quantiproduto)
                    if quantiproduto > maxima:
                        print('\033[33mErro: \033[mDepósito cheio.')
                        sleep(1)

                    elif quantiproduto < 0:
                        print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                    else:
                        valortotalpma = custo * quantiproduto
                        if BDP.dinheiro >= valortotalpma:
                            break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)

            BDP.dinheiro -= valortotalpma
            print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'.format(
                buscaitem, custo, valortotalpma, quantiproduto))
            sleep(3)

            if Tipo_Mercado in 'Acougue':
                BDP.scqtdeprodepositoacougue[buscaitem] += quantiproduto
            elif Tipo_Mercado in 'Padaria':
                BDP.scqtdeprodepositopadaria[buscaitem] += quantiproduto
            elif Tipo_Mercado in 'Loja de Eletronica':
                BDP.scqtdeprodepositoeletronica[buscaitem] += quantiproduto
            elif Tipo_Mercado in 'SuperMercado':
                BDP.scqtdeprodepositosm[buscaitem] += quantiproduto


def scfuncionarios(buscatm1):
    Tipo_Mercado = buscatm1
    while True:
        print('Contratar:')
        for f in range(len(BDP.funcionario)):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip().title()
            if funcionario1 in '':
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

            elif funcionario1 in 'C':
                break

            elif funcionario1 in '01':
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]

                if Tipo_Mercado in 'Acougue':
                    if BDP.scqtdefuncionariosacougue[busca0] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                        break

                    if BDP.dinheiro >= BDP.precofuncionario[busca]:
                        pass

                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
                        sleep(1)
                        break
                    BDP.scqtdefuncionariosacougue[busca0] += 1
                    print('Funcão para {}:'.format(busca0))
                    for fa in range(len(BDP.scfuncoesacougue)):
                        print('[{}] {}.'.format(fa, BDP.scfuncoesacougue[fa]))
                    while True:
                        tecla = str(input('Tecla: '))
                        inteiro = tecla.isnumeric()
                        strinteiro = str(inteiro)
                        ebool = strinteiro.find('True')
                        if ebool == 0:
                            tecla = int(tecla)
                            if tecla == 1 or tecla == 0:
                                funcao = BDP.scfuncoesacougue[tecla]
                                if BDP.scqtdefuncoesacougue[funcao] == 0:
                                    break
                                else:
                                    print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    sleep(1)
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                    BDP.scqtdefuncoesacougue[funcao] += 1
                    BDP.scacouguepgmtfuntotal += valorf1
                    BDP.dinheiro -= valorf1
                    print(f'Você contratou o(a) {busca0} e a sua funcão é {funcao} e o seu sálario é de R${valorf1}.')
                    sleep(3)
                    break

                elif Tipo_Mercado in 'Padaria':
                    if BDP.scqtdefuncionariospadaria[busca0] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                        break

                    if BDP.dinheiro >= BDP.precofuncionario[busca]:
                        pass

                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
                        sleep(1)
                        break
                    BDP.scqtdefuncionariospadaria[busca0] += 1
                    print('Funcão para {}:'.format(busca0))
                    for fa in range(len(BDP.scfuncoespadaria)):
                        print('[{}] {}.'.format(fa, BDP.scfuncoespadaria[fa]))
                    while True:
                        tecla = str(input('Tecla: '))
                        inteiro = tecla.isnumeric()
                        strinteiro = str(inteiro)
                        ebool = strinteiro.find('True')
                        if ebool == 0:
                            tecla = int(tecla)
                            if tecla == 1 or tecla == 0:
                                funcao = BDP.scfuncoespadaria[tecla]
                                if BDP.scqtdefuncoespadaria[funcao] == 0:
                                    break
                                else:
                                    print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    sleep(1)
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')

                    BDP.scqtdefuncoespadaria[funcao] += 1
                    BDP.scpadariapgmtfuntotal += valorf1
                    BDP.dinheiro -= valorf1
                    print(f'Você contratou o(a) {busca0} e a sua funcão é {funcao} e o seu sálario é de R${valorf1}.')
                    sleep(3)
                    break

                elif Tipo_Mercado in 'Loja de Eletronica':
                    if BDP.scqtdefuncionarioseletronica[busca0] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                        break

                    if BDP.dinheiro >= BDP.precofuncionario[busca]:
                        pass

                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
                        sleep(1)
                        break
                    BDP.scqtdefuncionarioseletronica[busca0] += 1
                    print('Funcão para {}:'.format(busca0))
                    for fa in range(len(BDP.scfuncoeseletronica)):
                        print('[{}] {}.'.format(fa, BDP.scfuncoeseletronica[fa]))
                    while True:
                        tecla = str(input('Tecla: '))
                        inteiro = tecla.isnumeric()
                        strinteiro = str(inteiro)
                        ebool = strinteiro.find('True')
                        if ebool == 0:
                            tecla = int(tecla)
                            if tecla == 1 or tecla == 0:
                                funcao = BDP.scfuncoeseletronica[tecla]
                                if BDP.scqtdefuncoeseletronica[funcao] == 0:
                                    break
                                else:
                                    print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    sleep(1)
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    BDP.scqtdefuncoeseletronica[funcao] += 1
                    BDP.scelepgmtfuntotal += valorf1
                    BDP.dinheiro -= valorf1
                    print(f'Você contratou o(a) {busca0} e a sua funcão é {funcao} e o seu sálario é de R${valorf1}.')
                    sleep(3)
                    break

                elif Tipo_Mercado in 'SuperMercado':
                    if BDP.scqtdefuncionariossupermercado[busca0] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                        break

                    if BDP.dinheiro >= BDP.precofuncionario[busca]:
                        pass

                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
                        sleep(1)
                        break
                    BDP.scqtdefuncionariossupermercado[busca0] += 1
                    print('Funcão para {}:'.format(busca0))
                    for fa in range(len(BDP.scfuncoessupermercado)):
                        print('[{}] {}.'.format(fa, BDP.scfuncoessupermercado[fa]))
                    while True:
                        tecla = str(input('Tecla: '))
                        inteiro = tecla.isnumeric()
                        strinteiro = str(inteiro)
                        ebool = strinteiro.find('True')
                        if ebool == 0:
                            tecla = int(tecla)
                            if tecla == 1 or tecla == 0:
                                funcao = BDP.scfuncoessupermercado[tecla]
                                if BDP.scqtdefuncoessupermercado[funcao] == 0:
                                    break
                                else:
                                    print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    sleep(1)
                            else:
                                print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                        else:
                            print('\033[31mErro:  \033[mOpção inválida, tente novamente')
                    BDP.scqtdefuncoessupermercado[funcao] += 1
                    BDP.scsmpgmtfuntotal += valorf1
                    BDP.dinheiro -= valorf1
                    print(f'Você contratou o(a) {busca0} e a sua funcão é {funcao} e o seu sálario é de R${valorf1}.')
                    sleep(3)
                    break
            else:
                print('\033[31mErro:  \033[mOpção inválida, tente novamente')

        if funcionario1 in 'C':
            break


JogoInicio()

# Versão 2.0

from time import sleep
import BDP
from math import trunc
from random import choice


def Abrir_Mercados():
    while True:
        print('[0] Abrir um novo mercado.')
        print('[1] Acessar um mercado existente.')
        print('[C] voltar.')
        while True:
            tecla1 = input('Tecla: ').strip().title()
            if tecla1 in 'C':
                JogoInicio()
            elif tecla1 in '0':
                print('Estado em que seu mercado ficará: ')
                tamanhom = len(BDP.cmapa)
                while True:
                    for i in range(tamanhom):
                        print('[{}] {}'.format(i, BDP.cmapa[i]))
                    print('[C] Voltar')
                    while True:
                        tecla2 = input('Tecla: ').title().strip()
                        if tecla2 in BDP.nmapa:
                            buscamapa = BDP.nmapa.index(tecla2)
                            buscamapa1 = BDP.mapa[buscamapa]
                            print('Tipos de Mercados:')
                            print('Qual será seu mercado')
                            tamanho2 = len(BDP.tipo_de_mercado)
                            for i in range(tamanho2):
                                print('[{}] {} = R${}.'.format(i, BDP.tipo_de_mercado[i], BDP.preco_mercado[i]))
                            print('[C] Voltar.')
                            while True:
                                tecla3 = input('Tecla: ').title().strip()
                                if tecla3 in BDP.ntipo_de_mercado:
                                    busca = BDP.ntipo_de_mercado.index(tecla3)
                                    busca1 = BDP.tipo_de_mercado[busca]
                                    preco = BDP.preco_mercado[busca]
                                    if tecla2 in '0':
                                        if tecla3 in '0':
                                            if BDP.scimoveis['Acougue'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[0]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SCEstado_Mercado.append(buscamapa1)
                                                    BDP.SCTipo_Mercado.append(busca1)
                                                    BDP.SCNome_Mercado.append(NomeMercado)
                                                    BDP.SC += 1
                                                    BDP.scimoveis['Acougue'] += 1
                                                    BDP.SCnumeracao_estado.append(BDP.SC)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.scimoveis['Acougue'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem um {} nesse Estado.'.format(
                                                    busca1))

                                        elif tecla3 in '1':
                                            if BDP.scimoveis['Padaria'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[1]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SCEstado_Mercado.append(buscamapa1)
                                                    BDP.SCTipo_Mercado.append(busca1)
                                                    BDP.SCNome_Mercado.append(NomeMercado)
                                                    BDP.SC += 1
                                                    BDP.scimoveis['Padaria'] += 1
                                                    BDP.SCnumeracao_estado.append(BDP.SC)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.scimoveis['Padaria'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem uma {} nesse Estado.'.format(
                                                    busca1))

                                        elif tecla3 in '2':
                                            if BDP.scimoveis['Loja de Eletronica'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[2]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SCEstado_Mercado.append(buscamapa1)
                                                    BDP.SCTipo_Mercado.append(busca1)
                                                    BDP.SCNome_Mercado.append(NomeMercado)
                                                    BDP.SC += 1
                                                    BDP.scimoveis['Loja de Eletronica'] += 1
                                                    BDP.SCnumeracao_estado.append(BDP.SC)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.scimoveis['Loja de Eletronica'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem uma {} nesse Estado.'.format(
                                                    busca1))

                                        elif tecla3 in '3':
                                            if BDP.scimoveis['SuperMercado'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[3]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SCEstado_Mercado.append(buscamapa1)
                                                    BDP.SCTipo_Mercado.append(busca1)
                                                    BDP.SCNome_Mercado.append(NomeMercado)
                                                    BDP.SC += 1
                                                    BDP.scimoveis['SuperMercado'] += 1
                                                    BDP.SCnumeracao_estado.append(BDP.SC)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.scimoveis['SuperMercado'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem um {} nesse Estado.'.format(
                                                    busca1))

                                    elif tecla2 in '1':
                                        if tecla3 in '0':
                                            if BDP.spimoveis['Acougue'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[0]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SPEstado_Mercado.append(buscamapa1)
                                                    BDP.SPTipo_Mercado.append(busca1)
                                                    BDP.SPNome_Mercado.append(NomeMercado)
                                                    BDP.SP += 1
                                                    BDP.spimoveis['Acougue'] += 1
                                                    BDP.SPnumeracao_estado.append(BDP.SP)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.spimoveis['Acougue'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem um {} nesse Estado.'.format(
                                                    busca1))

                                        elif tecla3 in '1':
                                            if BDP.spimoveis['Padaria'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[1]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SPEstado_Mercado.append(buscamapa1)
                                                    BDP.SPTipo_Mercado.append(busca1)
                                                    BDP.SPNome_Mercado.append(NomeMercado)
                                                    BDP.SP += 1
                                                    BDP.spimoveis['Padaria'] += 1
                                                    BDP.SPnumeracao_estado.append(BDP.SP)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.spimoveis['Padaria'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem uma {} nesse Estado.'.format(
                                                    busca1))

                                        elif tecla3 in '2':
                                            if BDP.spimoveis['Loja de Eletronica'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[2]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SPEstado_Mercado.append(buscamapa1)
                                                    BDP.SPTipo_Mercado.append(busca1)
                                                    BDP.SPNome_Mercado.append(NomeMercado)
                                                    BDP.SP += 1
                                                    BDP.spimoveis['Loja de Eletronica'] += 1
                                                    BDP.SPnumeracao_estado.append(BDP.SP)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.spimoveis['Loja de Eletronica'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem uma {} nesse Estado.'.format(
                                                    busca1))

                                        elif tecla3 in '3':
                                            if BDP.spimoveis['SuperMercado'] == 0:
                                                if BDP.dinheiro >= BDP.preco_mercado[3]:
                                                    NomeMercado = input('Nome do mercado: ').strip()
                                                    BDP.SPEstado_Mercado.append(buscamapa1)
                                                    BDP.SPTipo_Mercado.append(busca1)
                                                    BDP.SPNome_Mercado.append(NomeMercado)
                                                    BDP.SP += 1
                                                    BDP.spimoveis['SuperMercado'] += 1
                                                    BDP.SPnumeracao_estado.append(BDP.SP)
                                                    BDP.dinheiro -= preco
                                                    print('Voce teve um gasto de R${} com o imóvel.'.format(preco))
                                                    sleep(1)
                                                    break
                                                else:
                                                    print('\033[33mErro: \033[mDinheiro insuficiente.')
                                            elif BDP.spimoveis['SuperMercado'] == 1:
                                                print('\033[33mErro: \033[mVoce já tem um {} nesse Estado.'.format(
                                                    busca1))

                                elif tecla3 in 'C':
                                    break
                                else:
                                    print('\033[31mErro: \033[mOpção inválida.')
                            break
                        elif tecla2 in 'C':
                            break
                        else:
                            print('\033[31mErro: \033[mOpção inválida.')
                    break
                break
            elif tecla1 in '1':
                tamanho = len(BDP.mapa)
                while True:
                    for i in range(tamanho):
                        print('[{}] {}'.format(i, BDP.mapa[i]))
                    print('[C] Voltar')
                    while True:
                        tecla2 = input('Tecla: ').strip().title()
                        if tecla2 in 'C':
                            break
                        elif tecla2 in '0':
                            busca = BDP.nmapa.index(tecla2)
                            busca1 = BDP.mapa[busca]
                            print('{}:'.format(busca1))
                            tamanho1 = len(BDP.SCEstado_Mercado)
                            for i in range(tamanho1):
                                print('[{}] {}: {}'.format(i, BDP.SCTipo_Mercado[i], BDP.SCNome_Mercado[i]))
                            if not BDP.SCTipo_Mercado and not BDP.SCNome_Mercado:
                                print('\033[33mErro: \033[mSem comércio nesse Estado')
                                sleep(1)
                                break
                            else:
                                while True:
                                    tecla3 = int(input('Tecla: '))
                                    n = tecla3
                                    if n in BDP.SCnumeracao_estado:
                                        buscatm = BDP.SCnumeracao_estado.index(n)
                                        buscatm1 = BDP.SCTipo_Mercado[buscatm]
                                        buscanome = BDP.SCnumeracao_estado.index(n)
                                        buscanome1 = BDP.SCNome_Mercado[buscanome]
                                        print('\033[36m{}: \033[m'.format(buscanome1))
                                        if buscatm1 in 'Acougue':
                                            SCDentro_Mercado_Acougue()

                                        elif buscatm1 in 'Padaria':
                                            SCDentro_Mercado_Padaria()

                                        elif buscatm1 in 'Loja de Eletronica':
                                            SCDentro_Mercado_Eletronica()

                                        elif buscatm1 in 'SuperMercado':
                                            SCDentro_Mercado_SuperMercado()

                                        break
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                break
                        elif tecla2 in '1':
                            busca = BDP.nmapa.index(tecla2)
                            busca1 = BDP.mapa[busca]
                            print('{}:'.format(busca1))
                            tamanho1 = len(BDP.SPEstado_Mercado)
                            for i in range(tamanho1):
                                print('[{}] {}: {}'.format(i, BDP.SPTipo_Mercado[i],
                                                           BDP.SPNome_Mercado[i]))
                            if not BDP.SPTipo_Mercado and not BDP.SPNome_Mercado:
                                print('\033[33mErro: \033[mSem comércio nesse Estado')
                                sleep(1)
                                break
                            else:
                                while True:
                                    tecla3 = int(input('Tecla: '))
                                    n = tecla3
                                    if n in BDP.SPnumeracao_estado:
                                        buscatm = BDP.SPnumeracao_estado.index(n)
                                        buscatm1 = BDP.SPTipo_Mercado[buscatm]
                                        buscanome = BDP.SPnumeracao_estado.index(n)
                                        buscanome1 = BDP.SPNome_Mercado[buscanome]
                                        print('\033[36m{}: \033[m'.format(buscanome1))
                                        if buscatm1 in 'Acougue':
                                            SPDentro_Mercado_Acougue()

                                        elif buscatm1 in 'Padaria':
                                            SPDentro_Mercado_Padaria()

                                        elif buscatm1 in 'Loja de Eletronica':
                                            SPDentro_Mercado_Eletronica()

                                        elif buscatm1 in 'SuperMercado':
                                            SPDentro_Mercado_SuperMercado()

                                        break
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                break
                        else:
                            print('\033[31mErro: \033[mOpção inválida.')
                    break
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
        break


def habilidades():
    while True:
        print('[0] Mostrar habilidades.')
        print('[1] Melhorar habilidade.')
        print('[C] Voltar.')
        while True:
            tecla1 = input('Tecla: ').title()
            if tecla1 in '0':
                print('Habilidade de vendas Lv. {}'.format(BDP.levelhabi['lvhv']))
                print('Habilidade de reduzir preco Lv.{}'.format(BDP.levelhabi['lvhp']))
                print('Habilidade de lucro Lv.{}'.format(BDP.levelhabi['lvhl']))
                print('Habilidade de ganhar mais exp Lv.{}'.format(BDP.levelhabi['lvhe']))
                sleep(1)
                break
            elif tecla1 in '1':
                while True:
                    print('Melhorar:')
                    valor_habilidadev = BDP.precohavendas * BDP.habilidades['Habilidade de vendas']
                    valor_habilidadep = BDP.precohapreco * BDP.habilidades['Habilidade de reduzir preco']
                    valor_habilidadel = BDP.precohalucro * BDP.habilidades['Habilidade de lucro']
                    valor_habilidadee = BDP.precohaexp * BDP.habilidades['Habilidade de ganhar mais exp']
                    print('[0] Habilidade de vendas = {} Diamantes'.format(valor_habilidadev))
                    print('[1] Habilidade de reduzir preco = {} diamantes'.format(valor_habilidadep))
                    print('[2] Habilidade de lucro = {} diamantes'.format(valor_habilidadel))
                    print('[3] Habilidade de ganhar mais exp = {} diamantes'.format(valor_habilidadee))
                    print('[C] Voltar.')
                    while True:
                        tecla2 = input('Tecla: ').title()
                        if tecla2 in '0':
                            if BDP.diamante >= valor_habilidadev:
                                if BDP.levelhabi['lvhv'] == 10:
                                    print('\033[33mErro: \033[mHabilidade no level máximo')
                                    sleep(1)

                                else:
                                    BDP.habilidades['Habilidade de vendas'] += 1
                                    BDP.levelhabi['lvhv'] += 1
                                    BDP.diamante -= valor_habilidadev
                                    print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format(
                                        valor_habilidadev))
                                    print('Você aumentou o Lv. de habilidade de vendas.')
                                    sleep(2)
                                break
                            else:
                                print('\033[33mErro:  \033[mDiamante insuficiente.')

                        elif tecla2 in '1':
                            if BDP.diamante >= valor_habilidadep:
                                if BDP.levelhabi['lvhp'] == 5:
                                    print('\033[33mErro: \033[mHabilidade no level máximo')
                                    sleep(1)

                                else:
                                    BDP.habilidades['Habilidade de reduzir preco'] += 1
                                    BDP.levelhabi['lvhp'] += 1
                                    BDP.diamante -= valor_habilidadep
                                    print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format(
                                        valor_habilidadep))
                                    print('Você aumentou o Lv. de habilidade de reduzir preco.')
                                    sleep(2)
                                break
                            else:
                                print('\033[33mErro: \033[mDiamante insuficiente.')

                        elif tecla2 in '2':
                            if BDP.diamante >= valor_habilidadel:
                                if BDP.levelhabi['lvhl'] == 10:
                                    print('\033[33mErro: \033[mHabilidade no level máximo')
                                    sleep(1)

                                else:
                                    BDP.habilidades['Habilidade de lucro'] += 1
                                    BDP.levelhabi['lvhl'] += 1
                                    BDP.diamante -= valor_habilidadel
                                    print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format(
                                        valor_habilidadel))
                                    print('Você aumentou o Lv. de habilidade de lucro.')
                                    sleep(2)
                                    break
                            else:
                                print('\033[33mErro: \033[mDiamante insuficiente.')

                        elif tecla2 in '3':
                            if BDP.diamante >= valor_habilidadee:
                                if BDP.levelhabi['lvhe'] == 10:
                                    print('\033[33mErro: \033[mHabilidade no level máximo')
                                    sleep(1)

                                else:
                                    BDP.habilidades['Habilidade de ganhar mais exp'] += 1
                                    BDP.levelhabi['lvhe'] += 1
                                    BDP.diamante -= valor_habilidadee
                                    BDP.maisexp += 5
                                    print('Você teve um gasto de {} diamantes com o aumento de habilidade.'.format(
                                        valor_habilidadee))
                                    print('Você aumentou o Lv. de habilidade de ganhar mais exp.')
                                    sleep(2)
                                break
                            else:
                                print('\033[33mErro: \033[mDiamante insuficiente.')

                        elif tecla2 in 'C':
                            break
                        else:
                            print('\033[31mErro: \033[mOpção inválida.')
                    break
                break
            elif tecla1 in 'C':
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
        break


def sistemalevel():
    while True:
        if BDP.nivel['qtdeexp'] >= BDP.nivel['uplevel']:
            while True:
                BDP.nivel['uplevel'] *= 2
                BDP.nivel['level'] += 1
                print('Up level {}'.format(BDP.nivel['level']))
                sleep(1.5)
                break
        else:
            break


# 2.238
# 2.271
# 5.001


def boasvinda():
    print('Bem-Vindo ao Mercadolândia')
    JogoInicio()


def JogoInicio():
    while True:
        print('Funções de controle:')
        print('[A] Visualizar mapa.')
        print('[B] Abrir Mercado.')
        print('[C] Mostrar habilidades.')
        print('[D] Mostrar conquistar.')
        print('[E] Comprar Moeda.')
        print('[F] Informações.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'A':
                print('Mapa do Jogo: ')
                sleep(1)
                tamanho = len(BDP.mapa)
                for i in range(tamanho):
                    print(BDP.mapa[i])
                break

            elif tecla in 'B':
                Abrir_Mercados()
                break

            elif tecla in 'C':
                habilidades()
                break

            elif tecla in 'D':
                break

            elif tecla in 'E':
                while True:
                    print('[0] Comprar diamante.')
                    print('[1] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        elif tecla1 in '0':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '1':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break
            elif tecla in 'F':
                while True:
                    print('[0] Mostrar saldo.')
                    print('[1] Mostrar imóveis.')
                    print('[2] Mostrar Level.')
                    while True:
                        tecla2 = input('Tecla: ').strip()
                        if tecla2 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(2)
                            break
                        elif tecla2 in '1':
                            tamanho = len(BDP.SCTipo_Mercado)
                            print('Santa Catarina:')
                            if not BDP.SCNome_Mercado:
                                print('\033[33mErro: \033[mSem comércio nesse Estado')
                                sleep(1)

                            else:
                                for m in range(tamanho):
                                    print('[{}] {} = {}'.format(m, BDP.SCNome_Mercado[m], BDP.SCTipo_Mercado[m]))
                                    sleep(1)

                            tamanho = len(BDP.SPTipo_Mercado)
                            print('São Paulo:')
                            if not BDP.SPNome_Mercado:
                                print('\033[33mErro: \033[mSem comércio nesse Estado')
                                sleep(1)
                            else:
                                for m in range(tamanho):
                                    print('[{}] {} = {}'.format(m, BDP.SPNome_Mercado[m], BDP.SPTipo_Mercado[m]))
                                    sleep(1)
                            break
                        elif tecla2 in '2':
                            expproximolv = BDP.nivel['uplevel'] - BDP.nivel['qtdeexp']
                            print('Lv.{}'.format(BDP.nivel['level']))
                            print('Quantidade de exp: {}'.format(BDP.nivel['qtdeexp']))
                            print('Exp ate o proximo level: {}'.format(expproximolv))
                            sleep(2)
                            break
                    break
                break
            else:
                print('\033[31mErro:  \033[mOpção inválida.')
            break


def scdepositoacougue():
    quantisaidadeposito = 0
    v = 0
    vm = 0

    if vm == 4:
        vm -= 4
    for _ in BDP.scmoveisacougue:
        ns = str(vm)
        buscamoveis = BDP.scnmoveisa.index(ns)
        busca1moveis = BDP.scmoveisacougue[buscamoveis]
        busca2moveis = BDP.sclimiteitensmoveisacougue[vm]
        vm += 1
        if BDP.scqtdemoveisacougue[busca1moveis] >= 1:
            quantisaidadeposito += busca2moveis * BDP.scqtdemoveisacougue[busca1moveis]
    quantiproduto = 0
    somav = 0
    for deposito in BDP.scprodutosdepositoacougue:
        somav += BDP.scqtdeprodepositoacougue[deposito]
    for conta in BDP.scprodutosacougue:
        quantiproduto += BDP.scqtdeprodutoacougue[conta]
    falta = quantisaidadeposito - quantiproduto
    while True:
        vs = str(v)
        teste1 = 0
        buscaitem = BDP.scnpa.index(vs)
        buscad = BDP.scprodutosdepositoacougue[buscaitem]
        buscav = BDP.scprodutosacougue[buscaitem]
        if BDP.scqtdeprodepositoacougue[buscad] >= 1:
            if BDP.scqtdeprodepositoacougue[buscad] <= falta:
                BDP.scqtdeprodutoacougue[buscav] += BDP.scqtdeprodepositoacougue[buscad]
                BDP.scqtdeprodepositoacougue[buscad] -= BDP.scqtdeprodepositoacougue[buscad]
                teste1 += BDP.scqtdeprodutoacougue[buscav]

            elif BDP.scqtdeprodepositoacougue[buscad] > falta:
                BDP.scqtdeprodutoacougue[buscav] += falta
                BDP.scqtdeprodepositoacougue[buscad] -= falta
                teste1 += falta

        v += 1
        if v == 8:
            v -= 8
            break


# scdepositopadaria


def scdepositopadaria():
    v = 0

    saidaboleira = 0

    mesap = 0
    mesam = 0
    mesag = 0

    geladeirap = 0
    geladeiram = 0
    geladeirag = 0

    pasteleirap = 0
    pasteleiram = 0
    pasteleirag = 0

    prateleirap = 0
    prateleiram = 0
    prateleirag = 0

    saidatotal = 0

    saidaboleira += BDP.scqtdemoveispadaria['Boleira'] * BDP.sclimiteitensmoveispadaria[1]

    mesap += BDP.scqtdemoveispadaria['MesaP'] * BDP.sclimiteitensmoveispadaria[2]
    mesam += BDP.scqtdemoveispadaria['MesaM'] * BDP.sclimiteitensmoveispadaria[3]
    mesag += BDP.scqtdemoveispadaria['MesaG'] * BDP.sclimiteitensmoveispadaria[4]
    saidamesa = mesap + mesam + mesag

    geladeirap += BDP.scqtdemoveispadaria['GeladeiraP'] * BDP.sclimiteitensmoveispadaria[5]
    geladeiram += BDP.scqtdemoveispadaria['GeladeiraM'] * BDP.sclimiteitensmoveispadaria[6]
    geladeirag += BDP.scqtdemoveispadaria['GeladeiraG'] * BDP.sclimiteitensmoveispadaria[7]
    saidageladeira = geladeirap + geladeiram + geladeirag

    pasteleirap += BDP.scqtdemoveispadaria['PasteleiraP'] * BDP.sclimiteitensmoveispadaria[8]
    pasteleiram += BDP.scqtdemoveispadaria['PasteleiraM'] * BDP.sclimiteitensmoveispadaria[9]
    pasteleirag += BDP.scqtdemoveispadaria['PasteleiraG'] * BDP.sclimiteitensmoveispadaria[10]
    saidapasteleira = pasteleirap + pasteleiram + pasteleirag

    prateleirap += BDP.scqtdemoveispadaria['PrateleiraP'] * BDP.sclimiteitensmoveispadaria[11]
    prateleiram += BDP.scqtdemoveispadaria['PrateleiraM'] * BDP.sclimiteitensmoveispadaria[12]
    prateleirag += BDP.scqtdemoveispadaria['PrateleiraG'] * BDP.sclimiteitensmoveispadaria[13]
    saidaprateleira = prateleirap + prateleiram + prateleirag

    saidatotal += saidaboleira + saidamesa + saidageladeira + saidapasteleira + saidaprateleira
    produtosboleira = 0

    while True:
        somav = 0
        for deposito in BDP.scprodutosdepositopadaria:
            somav += BDP.scqtdeprodepositopadaria[deposito]
        vs = str(v)
        if v == 17:
            v -= 17
            break
        buscaitem = BDP.scnpp.index(vs)
        buscad = BDP.scprodutosdepositopadaria[buscaitem]
        buscav = BDP.scprodutospadaria[buscaitem]
        teste1 = 0
        if BDP.scqtdeprodepositopadaria[buscad] >= 1:
            if buscad == 'dBolo':
                produtosboleira += BDP.scqtdeprodutopadaria['Bolo']
                faltaboleira = saidaboleira - produtosboleira
                if BDP.scqtdeprodepositopadaria[buscad] <= faltaboleira:
                    BDP.scqtdeprodutopadaria[buscav] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]
                    teste1 += BDP.scqtdeprodutopadaria[buscav]

                elif BDP.scqtdeprodepositopadaria[buscad] > faltaboleira:
                    BDP.scqtdeprodutopadaria[buscav] += faltaboleira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltaboleira
                    teste1 += faltaboleira

            elif buscad == 'dCuca' or buscad == 'dPao' or buscad == 'dRosquinha':
                produtosmesa = (BDP.scqtdeprodutopadaria['Cuca'] + BDP.scqtdeprodutopadaria['Pao'] +
                                BDP.scqtdeprodutopadaria['Rosquinha'])
                faltamesa = saidamesa - produtosmesa
                if BDP.scqtdeprodepositopadaria[buscad] <= faltamesa:
                    BDP.scqtdeprodutopadaria[buscav] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]
                    teste1 += BDP.scqtdeprodutopadaria[buscav]

                elif BDP.scqtdeprodepositopadaria[buscad] > faltamesa:
                    BDP.scqtdeprodutopadaria[buscav] += faltamesa
                    BDP.scqtdeprodepositopadaria[buscad] -= faltamesa
                    teste1 += faltamesa

            if buscad == 'dBolinho' or buscad == 'dCoxinha' or buscad == 'dPao_de_queijo' or buscad == 'dPastel':
                produtospasteleira = (BDP.scqtdeprodutopadaria['Bolinho'] + BDP.scqtdeprodutopadaria['Coxinha'] +
                                      BDP.scqtdeprodutopadaria['Pao_de_queijo'] + BDP.scqtdeprodutopadaria['Pastel'])

                faltapasteleira = saidapasteleira - produtospasteleira
                if BDP.scqtdeprodepositopadaria[buscad] <= faltapasteleira:
                    BDP.scqtdeprodutopadaria[buscav] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]
                    teste1 += BDP.scqtdeprodutopadaria[buscav]

                elif BDP.scqtdeprodepositopadaria[buscad] > faltapasteleira:
                    BDP.scqtdeprodutopadaria[buscav] += faltapasteleira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltapasteleira
                    teste1 += faltapasteleira

            if buscad == 'dBolacha' or buscad == 'dCafe':
                produtosprateleira = BDP.scqtdeprodutopadaria['Bolacha'] + BDP.scqtdeprodutopadaria['Cafe']
                faltaprateleira = saidaprateleira - produtosprateleira
                if BDP.scqtdeprodepositopadaria[buscad] <= faltaprateleira:
                    BDP.scqtdeprodutopadaria[buscav] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]
                    teste1 += BDP.scqtdeprodutopadaria[buscav]

                elif BDP.scqtdeprodepositopadaria[buscad] > faltaprateleira:
                    BDP.scqtdeprodutopadaria[buscav] += faltaprateleira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltaprateleira
                    teste1 += faltaprateleira

            if (buscad == 'dLeite' or buscad == 'dMargarina' or buscad == 'dNata' or buscad == 'Presunto' or
                    buscad == 'dQueijo' or buscad == 'dSorvete' or buscad == 'dYogurt'):
                produtosgeladeira = (BDP.scqtdeprodutopadaria['Leite'] + BDP.scqtdeprodutopadaria['Margarina'] +
                                     BDP.scqtdeprodutopadaria['Nata'] + BDP.scqtdeprodutopadaria['Presunto'] +
                                     BDP.scqtdeprodutopadaria['Queijo'] + BDP.scqtdeprodutopadaria['Sorvete'] +
                                     BDP.scqtdeprodutopadaria['Yogurt'])
                faltageladeira = saidageladeira - produtosgeladeira
                if BDP.scqtdeprodepositopadaria[buscad] <= faltageladeira:
                    BDP.scqtdeprodutopadaria[buscav] += BDP.scqtdeprodepositopadaria[buscad]
                    BDP.scqtdeprodepositopadaria[buscad] -= BDP.scqtdeprodepositopadaria[buscad]
                    teste1 += BDP.scqtdeprodutopadaria[buscav]

                elif BDP.scqtdeprodepositopadaria[buscad] > faltageladeira:
                    BDP.scqtdeprodutopadaria[buscav] += faltageladeira
                    BDP.scqtdeprodepositopadaria[buscad] -= faltageladeira
                    teste1 += faltageladeira

        v += 1


def scdepositoeletronico():
    v = 0
    saidamesap = 0
    saidamesam = 0
    saidamesag = 0

    saidaprateleirap = 0
    saidaprateleiram = 0
    saidaprateleirag = 0

    saidamesap += BDP.sclimiteitensmoveiseletronica[1] * BDP.scqtdemoveiseletronica['MesaP']
    saidamesam += BDP.sclimiteitensmoveiseletronica[2] * BDP.scqtdemoveiseletronica['MesaM']
    saidamesag += BDP.sclimiteitensmoveiseletronica[3] * BDP.scqtdemoveiseletronica['MesaG']
    saidamesa = saidamesap + saidamesam + saidamesag

    saidaprateleirap += BDP.sclimiteitensmoveiseletronica[4] * BDP.scqtdemoveiseletronica['PrateleiraP']
    saidaprateleiram += BDP.sclimiteitensmoveiseletronica[5] * BDP.scqtdemoveiseletronica['PrateleiraM']
    saidaprateleirag += BDP.sclimiteitensmoveiseletronica[6] * BDP.scqtdemoveiseletronica['PrateleiraG']
    saidaprateleira = saidaprateleirap + saidaprateleiram + saidaprateleirag

    while True:
        somav = 0
        for deposito in BDP.scprodutosdepositoeletronica:
            somav += BDP.scqtdeprodepositoeletronica[deposito]
        vs = str(v)
        if v == 8:
            v -= 8
            break
        buscaitem = BDP.scnpe.index(vs)
        buscad = BDP.scprodutosdepositoeletronica[buscaitem]
        buscav = BDP.scprodutoseletronica[buscaitem]
        teste1 = 0
        if BDP.scqtdeprodepositoeletronica[buscad] >= 1:
            if (buscad == 'dCelular' or buscad == 'dComputador' or buscad == 'dNotebook' or buscad == 'dTablet' or
                    buscad == 'dTelevisao'):

                produtosmesa = (BDP.scqtdeprodutoeletronica['Celular'] + BDP.scqtdeprodutoeletronica['Computador'] +
                                BDP.scqtdeprodutoeletronica['Notebook'] + BDP.scqtdeprodutoeletronica['Tablet'] +
                                BDP.scqtdeprodutoeletronica['Televisao'])
                faltamesa = saidamesa - produtosmesa
                if BDP.scqtdeprodepositoeletronica[buscad] <= faltamesa:
                    BDP.scqtdeprodutoeletronica[buscav] += BDP.scqtdeprodepositoeletronica[buscad]
                    BDP.scqtdeprodepositoeletronica[buscad] -= BDP.scqtdeprodepositoeletronica[buscad]
                    teste1 += BDP.scqtdeprodutoeletronica[buscav]

                elif BDP.scqtdeprodepositoeletronica[buscad] > faltamesa:
                    BDP.scqtdeprodutoeletronica[buscav] += faltamesa
                    BDP.scqtdeprodepositoeletronica[buscad] -= faltamesa
                    teste1 += faltamesa

            elif buscad == 'dIpad' or buscad == 'dMouse' or buscad == 'dTeclado':
                produtosprateleira = (BDP.scqtdeprodutoeletronica['Ipad'] + BDP.scqtdeprodutoeletronica['Mouse'] +
                                      BDP.scqtdeprodutoeletronica['Teclado'])
                faltaprateleira = saidaprateleira - produtosprateleira
                if BDP.scqtdeprodepositoeletronica[buscad] <= faltaprateleira:
                    BDP.scqtdeprodutoeletronica[buscav] += BDP.scqtdeprodepositoeletronica[buscad]
                    BDP.scqtdeprodepositoeletronica[buscad] -= BDP.scqtdeprodepositoeletronica[buscad]
                    teste1 += BDP.scqtdeprodutoeletronica[buscav]

                elif BDP.scqtdeprodepositoeletronica[buscad] > faltaprateleira:
                    BDP.scqtdeprodutoeletronica[buscav] += faltaprateleira
                    BDP.scqtdeprodepositoeletronica[buscad] -= faltaprateleira
                    teste1 += faltaprateleira

        v += 1


def scdepositosupermercado():
    v = 0
    saidafruteirap = 0
    saidafruteiram = 0
    saidafruteirag = 0

    saidaprateleirap = 0
    saidaprateleiram = 0
    saidaprateleirag = 0

    saidafruteirap += BDP.sclimiteitensmoveissm[1] * BDP.scqtdemoveissupermercado['FruteiraP']
    saidafruteiram += BDP.sclimiteitensmoveissm[2] * BDP.scqtdemoveissupermercado['FruteiraM']
    saidafruteirag += BDP.sclimiteitensmoveissm[3] * BDP.scqtdemoveissupermercado['FruteiraG']
    saidafruteira = saidafruteirap + saidafruteiram + saidafruteirag

    saidaprateleirap += BDP.sclimiteitensmoveissm[4] * BDP.scqtdemoveissupermercado['PrateleiraP']
    saidaprateleiram += BDP.sclimiteitensmoveissm[5] * BDP.scqtdemoveissupermercado['PrateleiraM']
    saidaprateleirag += BDP.sclimiteitensmoveissm[6] * BDP.scqtdemoveissupermercado['PrateleiraG']
    saidaprateleira = saidaprateleirap + saidaprateleiram + saidaprateleirag

    while True:
        somafv = 0
        somalhg = 0
        for produtos in range(0, 34):
            n = str(produtos)
            buscafv = BDP.scnprodutossm.index(n)
            busca1fv = BDP.scprodutossm[buscafv]
            if busca1fv in BDP.scprodutossupermercadofv:
                somafv += BDP.scqtdeprodutosm[busca1fv]
            elif busca1fv in BDP.scprodutossupermercadolh or BDP.scprodutossupermercadog:
                somalhg += BDP.scqtdeprodutosm[busca1fv]

        vs = str(v)
        if v == 34:
            v -= 34
            break
        buscaitem = BDP.scnprodutossm.index(vs)
        buscad = BDP.scprodutosdepositosm[buscaitem]
        buscav = BDP.scprodutossm[buscaitem]
        teste1 = 0
        if BDP.scqtdeprodepositosm[buscad] >= 1:
            if buscad in BDP.scprodutosdepositosmfv:
                faltafruteira = saidafruteira - somafv
                if BDP.scqtdeprodepositosm[buscad] <= faltafruteira:
                    BDP.scqtdeprodutosm[buscav] += BDP.scqtdeprodepositosm[buscad]
                    BDP.scqtdeprodepositosm[buscad] -= BDP.scqtdeprodepositosm[buscad]
                    teste1 += BDP.scqtdeprodutosm[buscav]

                elif BDP.scqtdeprodepositosm[buscad] > faltafruteira:
                    BDP.scqtdeprodutosm[buscav] += faltafruteira
                    BDP.scqtdeprodepositosm[buscad] -= faltafruteira
                    teste1 += faltafruteira

            if buscad in BDP.scprodutosdepositosmlh or buscad in BDP.scprodutosdepositosmg:
                faltaprateleira = saidaprateleira - somalhg
                if BDP.scqtdeprodepositosm[buscad] <= faltaprateleira:
                    BDP.scqtdeprodutosm[buscav] += BDP.scqtdeprodepositosm[buscad]
                    BDP.scqtdeprodepositosm[buscad] -= BDP.scqtdeprodepositosm[buscad]
                    teste1 += BDP.scqtdeprodutosm[buscav]

                elif BDP.scqtdeprodepositosm[buscad] > faltaprateleira:
                    BDP.scqtdeprodutosm[buscav] += faltaprateleira
                    BDP.scqtdeprodepositosm[buscad] -= faltaprateleira
                    teste1 += faltaprateleira

        v += 1


def sccontratarfuncionarioacougue():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SCDentro_Mercado_Acougue()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.scqtdefuncionariosacougue['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.scqtdefuncionariosacougue['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoesacougue)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoesacougue[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoesacougue['Fcaixa'] == 0:
                                            BDP.scqtdefuncoesacougue['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoesacougue['Facougueiro'] == 0:
                                            BDP.scqtdefuncoesacougue['Facougueiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.scqtdefuncionariosacougue['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.scqtdefuncionariosacougue['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoesacougue)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoesacougue[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoesacougue['Fcaixa'] == 0:
                                            BDP.scqtdefuncoesacougue['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoesacougue['Facougueiro'] == 0:
                                            BDP.scqtdefuncoesacougue['Facougueiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SCDentro_Mercado_Acougue()


def sccontratarfuncionariopadaria():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SCDentro_Mercado_Padaria()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.scqtdefuncionariospadaria['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.scqtdefuncionariospadaria['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoespadaria)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoespadaria[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoespadaria['Fcaixa'] == 0:
                                            BDP.scqtdefuncoespadaria['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoespadaria['Fpadeiro'] == 0:
                                            BDP.scqtdefuncoespadaria['Fpadeiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.scqtdefuncionariospadaria['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.scqtdefuncionariospadaria['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoespadaria)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoespadaria[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoespadaria['Fcaixa'] == 0:
                                            BDP.scqtdefuncoespadaria['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoespadaria['Fpadeiro'] == 0:
                                            BDP.scqtdefuncoesacougue['Fpadeiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SCDentro_Mercado_Padaria()


def sccontratarfuncionarioeletronica():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SCDentro_Mercado_Eletronica()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.scqtdefuncionarioseletronica['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.scqtdefuncionarioseletronica['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoeseletronica)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoeseletronica[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoeseletronica['Fcaixa'] == 0:
                                            BDP.scqtdefuncoeseletronica['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoeseletronica['Fatendente'] == 0:
                                            BDP.scqtdefuncoeseletronica['Fatendente'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.scqtdefuncionarioseletronica['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.scqtdefuncionarioseletronica['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoeseletronica)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoeseletronica[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoeseletronica['Fcaixa'] == 0:
                                            BDP.scqtdefuncoeseletronica['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoeseletronica['Fatendente'] == 0:
                                            BDP.scqtdefuncoeseletronica['Fatendente'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SCDentro_Mercado_Eletronica()


def sccontratarfuncionariosupermercado():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SCDentro_Mercado_SuperMercado()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.scqtdefuncionariossupermercado['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.scqtdefuncionariossupermercado['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoessupermercado)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoessupermercado[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoessupermercado['Fcaixa'] == 0:
                                            BDP.scqtdefuncoessupermercado['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoessupermercado['Frepositor'] == 0:
                                            BDP.scqtdefuncoessupermercado['Frepositor'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.scqtdefuncionariossupermercado['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.scqtdefuncionariossupermercado['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.scfuncoessupermercado)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.scfuncoessupermercado[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.scqtdefuncoessupermercado['Fcaixa'] == 0:
                                            BDP.scqtdefuncoessupermercado['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.scqtdefuncoessupermercado['Frepositor'] == 0:
                                            BDP.scqtdefuncoessupermercado['Frepositor'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SCDentro_Mercado_SuperMercado()


def SCDentro_Mercado_Acougue():
    while True:
        scvendaacougue()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar Açougue.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in 'C':
                        break
                    elif tecla1 in '0':
                        sclojamoveisacougue()
                        break

                    elif tecla1 in '1':
                        scmercadoacougue()
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break

            elif tecla in '1':
                sccontratarfuncionarioacougue()

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                scvendaacougue()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no depósito')
                print('[3] Quantidade de vendas.')
                print('[4] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveisacougue in BDP.scqtdemoveisacougue:
                            print('{} = {}'.format(moveisacougue, BDP.scqtdemoveisacougue[moveisacougue]))
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtoacougue in BDP.scqtdeprodutoacougue:
                            print('{} = {}'.format(produtoacougue, BDP.scqtdeprodutoacougue[produtoacougue]))
                        sleep(2)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositoacougue in BDP.scqtdeprodepositoacougue:
                            print('{} = {}'.format(depositoacougue, BDP.scqtdeprodepositoacougue[depositoacougue]))
                        sleep(2)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendaacougue in BDP.scqtdeprovendasacougue:
                            print('{} = {}'.format(vendaacougue, BDP.scqtdeprovendasacougue[vendaacougue]))
                        sleep(2)
                        break

                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funciacougue in BDP.scqtdefuncionariosacougue:
                            print('{} = {}'.format(funciacougue, BDP.scqtdefuncionariosacougue[funciacougue]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def SCDentro_Mercado_Padaria():
    while True:
        scvendapadaria()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar Padaria.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in 'C':
                        break
                    if tecla1 in '0':
                        sclojamoveispadaria()
                        break

                    elif tecla1 in '1':
                        scmercadopadaria()
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')

            elif tecla in '1':
                sccontratarfuncionariopadaria()
                break

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                scvendapadaria()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no depósito.')
                print('[2] Quantidade de vendas.')
                print('[3] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveispadaria in BDP.scqtdemoveispadaria:
                            print('{} = {}'.format(moveispadaria, BDP.scqtdemoveispadaria[moveispadaria]))
                        sleep(2)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtopadaria in BDP.scqtdeprodutopadaria:
                            print('{} = {}'.format(produtopadaria, BDP.scqtdeprodutopadaria[produtopadaria]))
                        sleep(3)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositopadaria in BDP.scqtdeprodepositopadaria:
                            print('{} = {}'.format(depositopadaria, BDP.scqtdeprodepositopadaria[depositopadaria]))
                        sleep(3)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendapadaria in BDP.scqtdeprovendaspadaria:
                            print('{} = {}'.format(vendapadaria, BDP.scqtdeprovendaspadaria[vendapadaria]))
                        sleep(3)
                        break

                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funcipadaria in BDP.scqtdefuncionariospadaria:
                            print('{} = {}'.format(funcipadaria, BDP.scqtdefuncionariospadaria[funcipadaria]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break

            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def SCDentro_Mercado_Eletronica():
    while True:
        scvendaeletronica()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar Loja Eletronica.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in 'C':
                        break
                    elif tecla1 in '0':
                        sclojamoveiseletronica()
                        break

                    elif tecla1 in '1':
                        scmercadoeletronica()
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break

            elif tecla in '1':
                sccontratarfuncionarioeletronica()

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                scvendaeletronica()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no depósito.')
                print('[2] Quantidade de vendas.')
                print('[3] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveiseletronico in BDP.scqtdemoveiseletronica:
                            print('{} = {}'.format(moveiseletronico, BDP.scqtdemoveiseletronica[moveiseletronico]))
                        sleep(2)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtoeletro in BDP.scqtdeprodutoeletronica:
                            print('{} = {}'.format(produtoeletro, BDP.scqtdeprodutoeletronica[produtoeletro]))
                        sleep(2)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositoele in BDP.scqtdeprodepositoeletronica:
                            print('{} = {}'.format(depositoele, BDP.scqtdeprodepositoeletronica[depositoele]))
                        sleep(3)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendaeletro in BDP.scqtdeprovendaseletronica:
                            print('{} = {}'.format(vendaeletro, BDP.scqtdeprovendaseletronica[vendaeletro]))
                        sleep(3)
                        break

                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funcieletro in BDP.scqtdefuncionarioseletronica:
                            print('{} = {}'.format(funcieletro, BDP.scqtdefuncionarioseletronica[funcieletro]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def SCDentro_Mercado_SuperMercado():
    while True:
        scvendasupermercado()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar SuperMercado.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in '0':
                        sclojamoveissupermercado()
                        break

                    elif tecla1 in '1':
                        scmercadosupermercado()
                        break

                    elif tecla1 in 'C':
                        break

                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            elif tecla in '1':
                sccontratarfuncionariosupermercado()
                break

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                        break
                    break
            elif tecla in '3':
                scvendasupermercado()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no depósito.')
                print('[3] Quantidade de vendas.')
                print('[4] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveissm in BDP.scqtdemoveissupermercado:
                            print('{} = {}'.format(moveissm, BDP.scqtdemoveissupermercado[moveissm]))
                        sleep(2)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtofvsm in BDP.scqtdeprodutosm:
                            print('{} = {}'.format(produtofvsm, BDP.scqtdeprodutosm[produtofvsm]))
                        sleep(3)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositosm in BDP.scqtdeprodepositosm:
                            print('{} = {}'.format(depositosm, BDP.scqtdeprodepositosm[depositosm]))
                        sleep(3)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendasmfv in BDP.scqtdeprovendasupermercado:
                            print('{} = {}'.format(vendasmfv, BDP.scqtdeprovendasupermercado[vendasmfv]))
                        sleep(3)
                        break
                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funcism in BDP.scqtdefuncionariossupermercado:
                            print('{} = {}'.format(funcism, BDP.scqtdefuncionariossupermercado[funcism]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break

            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def sclojamoveisacougue():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.scmoveisacougue)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.scmoveisacougue[i], BDP.sclimiteitensmoveisacougue[i],
                                                   BDP.scprecomoveisacougue[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SCDentro_Mercado_Acougue()
        elif compramoveis1 in BDP.scnmoveisa:
            buscamoveisa = BDP.scnmoveisa.index(compramoveis1)
            busca1moveisa = BDP.scmoveisacougue[buscamoveisa]
            custola = BDP.scprecomoveisacougue[buscamoveisa]
            while True:
                qtdemaxima = BDP.dinheiro / custola
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1la = int(input('Quantidade de {}: '.format(busca1moveisa)))
                if quantimoveis1la < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    valortotal = custola * quantimoveis1la
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveisa, custola, valortotal, quantimoveis1la))
            sleep(3)
            BDP.scqtdemoveisacougue[busca1moveisa] += quantimoveis1la
            break

        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SCDentro_Mercado_Acougue()


def scmercadoacougue():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        tamanho = len(BDP.scprodutosacougue)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, BDP.scprodutosacougue[i], BDP.scprecoacouguec[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = input('Que produto voce quer comprar para seu mercado: ').strip(' ').title()
            if compraproduto1 in BDP.scnpa:
                if (BDP.scqtdemoveisacougue['FreezerP'] or BDP.scqtdemoveisacougue['FreezerM'] or
                        BDP.scqtdemoveisacougue['FreezerG'] >= 1):
                    buscamercadoa = BDP.scnpa.index(compraproduto1)
                    busca1mercadoa = BDP.scprodutosacougue[buscamercadoa]
                    buscaitem = BDP.scprodutosdepositoacougue[buscamercadoa]
                    customa = BDP.scprecoacouguec[buscamercadoa] - precoreduzido
                    while True:
                        qtdemaxima = BDP.dinheiro / customa
                        print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                        quantiproduto1ma = int(input('Quantidade de {}: '.format(busca1mercadoa)))
                        valortotalpma = customa * quantiproduto1ma
                        sleep(1)
                        if quantiproduto1ma < 0:
                            print('\033[33mErro: \033[mQuantidade não permitido.')
                        else:
                            if BDP.dinheiro >= valortotalpma:
                                break
                            else:
                                print('\033[33mErro: \033[mDinheiro insuficiente.')
                    BDP.dinheiro -= valortotalpma
                    print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'.format(
                        busca1mercadoa, customa, valortotalpma, quantiproduto1ma))
                    sleep(3)
                    BDP.scqtdeprodepositoacougue[buscaitem] += quantiproduto1ma
                    break

                else:
                    print('\033[33mErro: \033[mVocê não tem um freezer.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    break
            elif compraproduto1 in 'C':
                SCDentro_Mercado_Acougue()
            else:
                print('\033[31mErro: \033[mOpção inválida.')
        break

    SCDentro_Mercado_Acougue()


def sclojamoveispadaria():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.scmoveispadaria)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.scmoveispadaria[i], BDP.sclimiteitensmoveispadaria[i],
                                                   BDP.scprecomoveispadaria[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SCDentro_Mercado_Padaria()
        elif compramoveis1 in BDP.scnmoveisp:
            buscamoveisp = BDP.scnmoveisp.index(compramoveis1)
            busca1moveisp = BDP.scmoveispadaria[buscamoveisp]
            custolp = BDP.scprecomoveispadaria[buscamoveisp]
            while True:
                qtdemaxima = BDP.dinheiro / custolp
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1 = int(input('Quantidade de {}: '.format(busca1moveisp)))
                if quantimoveis1 < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    valortotal = custolp * quantimoveis1
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveisp, custolp, valortotal, quantimoveis1))
            sleep(3)
            BDP.scqtdemoveispadaria[busca1moveisp] += quantimoveis1
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SCDentro_Mercado_Padaria()


def scmercadopadaria():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        tamanho = len(BDP.scprodutospadaria)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, BDP.scprodutospadaria[i], BDP.scprecopadariac[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = str(input('Que produto voce quer comprar para seu mercado: ')).strip(' ').title()
            pasteleira = ['1', '4', '10', '11']
            prateleira = ['0', '3']
            mesa = ['5', '9', '14']
            geladeira = ['6', '7', '8', '12', '13', '15', '16']
            if compraproduto1 in 'C':
                SCDentro_Mercado_Padaria()
            if compraproduto1 in pasteleira:
                if (BDP.scqtdemoveispadaria['PasteleiraP'] or BDP.scqtdemoveispadaria['PasteleiraM'] or
                        BDP.scqtdemoveispadaria['PasteleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma pasteleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Padaria()

            elif compraproduto1 in '2':
                if BDP.scqtdemoveispadaria['Boleira'] >= 1:
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma boleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Padaria()

            elif compraproduto1 in prateleira:
                if (BDP.scqtdemoveispadaria['PrateleiraP'] or BDP.scqtdemoveispadaria['PrateleiraM'] or
                        BDP.scqtdemoveispadaria['PrateleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Padaria()

            elif compraproduto1 in mesa:
                if (BDP.scqtdemoveispadaria['MesaP'] or BDP.scqtdemoveispadaria['MesaM'] or
                        BDP.scqtdemoveispadaria['MesaG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma mesa.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Padaria()

            elif compraproduto1 in geladeira:
                if (BDP.scqtdemoveispadaria['GeladeiraP'] or BDP.scqtdemoveispadaria['GeladeiraM'] or
                        BDP.scqtdemoveispadaria['GeladeiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma geladeira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Padaria()
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        buscamercadop = BDP.scnpp.index(compraproduto1)
        busca1mercadop = BDP.scprodutospadaria[buscamercadop]
        buscaitem = BDP.scprodutosdepositopadaria[buscamercadop]
        customp = BDP.scprecopadariac[buscamercadop] - precoreduzido
        while True:
            qtdemaxima = BDP.dinheiro / customp
            print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            quantiproduto1mp = int(input('Quantidade de {}: '.format(busca1mercadop)))
            valortotalpmp = customp * quantiproduto1mp
            sleep(1)
            if quantiproduto1mp < 0:
                print('\033[33mErro: \033[mQuantidade não permitido.')
            else:
                if BDP.dinheiro >= valortotalpmp:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')
        BDP.dinheiro -= valortotalpmp
        print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'
              .format(busca1mercadop, customp, valortotalpmp, quantiproduto1mp))
        sleep(3)
        BDP.scqtdeprodepositopadaria[buscaitem] += quantiproduto1mp
        break

    SCDentro_Mercado_Padaria()


def sclojamoveiseletronica():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.scmoveiseletronica)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.scmoveiseletronica[i],
                                                   BDP.sclimiteitensmoveiseletronica[i],
                                                   BDP.scprecomoveiseletronica[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SCDentro_Mercado_Eletronica()
        elif compramoveis1 in BDP.scnmoveise:
            buscamoveise = BDP.scnmoveise.index(compramoveis1)
            busca1moveise = BDP.scmoveiseletronica[buscamoveise]
            custome = BDP.scprecomoveiseletronica[buscamoveise]
            while True:
                qtdemaxima = BDP.dinheiro / custome
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1 = int(input('Quantidade de {}: '.format(busca1moveise)))
                valortotal = custome * quantimoveis1
                if quantimoveis1 < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveise, custome, valortotal, quantimoveis1))
            sleep(3)
            BDP.scqtdemoveiseletronica[busca1moveise] += quantimoveis1
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SCDentro_Mercado_Eletronica()


def scmercadoeletronica():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        tamanho = len(BDP.scprodutoseletronica)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, BDP.scprodutoseletronica[i], BDP.scprecoeletronicac[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = input('Que produto voce quer comprar para seu mercado: ').strip(' ').title()
            mesa = ['0', '1', '4', '5', '7']
            prateleira = ['2', '3', '6']
            if compraproduto1 in mesa:
                if (BDP.scqtdemoveiseletronica['MesaP'] or BDP.scqtdemoveiseletronica['MesaM'] or
                        BDP.scqtdemoveiseletronica['MesaG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma mesa.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Eletronica()
            elif compraproduto1 in prateleira:
                if (BDP.scqtdemoveiseletronica['PrateleiraP'] or BDP.scqtdemoveiseletronica['PrateleiraM'] or
                        BDP.scqtdemoveiseletronica['PrateleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_Eletronica()

            elif compraproduto1 in 'C':
                SCDentro_Mercado_Eletronica()
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        busca = BDP.scnpe.index(compraproduto1)
        busca1 = BDP.scprodutoseletronica[busca]
        buscaitem = BDP.scprodutosdepositoeletronica[busca]
        custo = BDP.scprecoeletronicac[busca] - precoreduzido
        while True:
            qtdemaxima = BDP.dinheiro / custo
            print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            quantiproduto1 = int(input('Quantidade de {}: '.format(busca1)))
            valortotalp = custo * quantiproduto1
            sleep(1)
            if quantiproduto1 < 0:
                print('\033[33mErro: \033[mQuantidade não permitido, \033[0;33mlimite de 1 até 300\033[m.')
            else:
                if BDP.dinheiro >= valortotalp:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')
        BDP.dinheiro -= valortotalp
        print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'
              .format(busca1, custo, valortotalp, quantiproduto1))
        sleep(3)
        BDP.scqtdeprodepositoeletronica[buscaitem] += quantiproduto1
        break

    SCDentro_Mercado_Eletronica()


def sclojamoveissupermercado():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.scmoveissupermercado)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.scmoveissupermercado[i], BDP.sclimiteitensmoveissm[i],
                                                   BDP.scprecomoveissupermercado[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SCDentro_Mercado_SuperMercado()
        elif compramoveis1 in BDP.scnmoveiss:
            buscamoveiss = BDP.scnmoveiss.index(compramoveis1)
            busca1moveiss = BDP.scmoveissupermercado[buscamoveiss]
            custolp = BDP.scprecomoveissupermercado[buscamoveiss]
            while True:
                qtdemaxima = BDP.dinheiro / custolp
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1 = int(input('Quantidade de {}: '.format(busca1moveiss)))
                valortotal = custolp * quantimoveis1
                if quantimoveis1 < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')
            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveiss, custolp, valortotal, quantimoveis1))
            sleep(3)
            BDP.scqtdemoveissupermercado[busca1moveiss] += quantimoveis1
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SCDentro_Mercado_SuperMercado()


def scmercadosupermercado():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        ntpsm = BDP.scnpsfv + BDP.scnpslh + BDP.scnpsg
        tpsm = BDP.scprodutossupermercadofv + BDP.scprodutossupermercadolh + BDP.scprodutossupermercadog
        tppsm = BDP.scprecosupermercadocfv + BDP.scprecosupermercadoclh + BDP.scprecosupermercadocg
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        tamanho = len(tpsm)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, tpsm[i], tppsm[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = str(input('Que produto voce quer comprar para seu mercado: ')).strip(' ').title()
            if compraproduto1 in 'C':
                SCDentro_Mercado_SuperMercado()

            elif compraproduto1 in BDP.scnpsfv:
                if (BDP.scqtdemoveissupermercado['FruteiraP'] or BDP.scqtdemoveissupermercado['FruteiraM'] or
                        BDP.scqtdemoveissupermercado['FruteiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma fruteira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_SuperMercado()

            elif compraproduto1 in BDP.scnpslh or compraproduto1 in BDP.scnpsg:
                if (BDP.scqtdemoveissupermercado['PrateleiraP'] or BDP.scqtdemoveissupermercado['PrateleiraM'] or
                        BDP.scqtdemoveissupermercado['PrateleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SCDentro_Mercado_SuperMercado()
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        buscamercado = ntpsm.index(compraproduto1)
        busca1mercado = tpsm[buscamercado]
        buscaitem = BDP.scprodutosdepositosm[buscamercado]
        custo = tppsm[buscamercado] - precoreduzido
        while True:
            qtdemaxima = BDP.dinheiro / custo
            print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            quantiproduto1 = int(input('Quantidade: '))
            valortotal = custo * quantiproduto1
            sleep(1)
            if quantiproduto1 < 0:
                print('\033[33mErro: \033[mQuantidade não permitido, \033[0;33mlimite de 1 até 300\033[m.')
            else:
                if BDP.dinheiro >= valortotal:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')

        BDP.dinheiro -= valortotal
        print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'
              .format(busca1mercado, custo, valortotal, quantiproduto1))
        sleep(3)
        BDP.scqtdeprodepositosm[buscaitem] += quantiproduto1
        break

    SCDentro_Mercado_SuperMercado()


def scvendaacougue():
    while True:
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        scva2 = BDP.scqtdemoveisacougue['Caixa'] * 2
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        lucromaior = BDP.levelhabi['lvhl'] * 2
        scqtdevendasacougue = qtdevendaslevel * scva2
        if BDP.scqtdemoveisacougue['Caixa'] >= 1:
            if BDP.scqtdefuncoesacougue['Fcaixa'] >= 1:
                if BDP.scqtdefuncoesacougue['Facougueiro'] >= 1:
                    if sorteio == 0:
                        for item in BDP.scqtdeprodutoacougue:
                            if BDP.scqtdeprodutoacougue[item] >= 1:
                                busca = BDP.scprodutosacougue.index(item)
                                busca1 = BDP.scprodutosacougue[busca]
                                bv = BDP.scprodutovendasacougue[busca]
                                if BDP.scqtdeprodutoacougue[busca1] >= scqtdevendasacougue:
                                    BDP.scqtdeprodutoacougue[busca1] -= scqtdevendasacougue
                                    BDP.scqtdeprovendasacougue[bv] += scqtdevendasacougue
                                    BDP.dinheiro += (BDP.scprecoacouguev[busca] + lucromaior) * scqtdevendasacougue
                                    precov = (BDP.scprecoacouguev[busca] + lucromaior) * scqtdevendasacougue
                                    npv = BDP.scprecoacouguev[busca] + lucromaior
                                    npc = BDP.scprecoacouguec[busca] - precoreduzido
                                    lucro = (npv - npc) * scqtdevendasacougue
                                    somaexp = (25 + BDP.maisexp) * scqtdevendasacougue
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(scqtdevendasacougue, busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.scqtdeprovendasacougue[bv] += BDP.scqtdeprodutoacougue[busca1]
                                    BDP.dinheiro += ((BDP.scprecoacouguev[busca] + lucromaior) *
                                                     BDP.scqtdeprodutoacougue[busca1])
                                    precov = ((BDP.scprecoacouguev[busca] + lucromaior) *
                                              BDP.scqtdeprodutoacougue[busca1])
                                    npv = BDP.scprecoacouguev[busca] + lucromaior
                                    npc = BDP.scprecoacouguec[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.scqtdeprodutoacougue[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.scqtdeprodutoacougue[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(BDP.scqtdeprodutoacougue[busca1],
                                                                                  busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.scqtdeprodutoacougue[busca1] -= BDP.scqtdeprodutoacougue[busca1]
                                    sleep(2)

                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função açougueiro.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um Caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        scdepositoacougue()
        break


def scvendapadaria():
    while True:
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        scvp2 = BDP.scqtdemoveispadaria['Caixa'] * 2
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        lucromaior = BDP.levelhabi['lvhl'] * 2
        scqtdevendaspadaria = qtdevendaslevel * scvp2
        if BDP.scqtdemoveispadaria['Caixa'] >= 1:
            if BDP.scqtdefuncoespadaria['Fcaixa'] >= 1:
                if BDP.scqtdefuncoespadaria['Fpadeiro'] >= 1:
                    if sorteio == 0:
                        for item in BDP.scqtdeprodutopadaria:
                            if BDP.scqtdeprodutopadaria[item] >= 1:
                                busca = BDP.scprodutospadaria.index(item)
                                busca1 = BDP.scprodutospadaria[busca]
                                bv = BDP.scprodutovendaspadaria[busca]
                                if BDP.scqtdeprodutopadaria[busca1] >= scqtdevendaspadaria:
                                    BDP.scqtdeprodutopadaria[busca1] -= scqtdevendaspadaria
                                    BDP.scqtdeprovendaspadaria[bv] += scqtdevendaspadaria
                                    BDP.dinheiro += (BDP.scprecopadariav[busca] + lucromaior) * scqtdevendaspadaria
                                    precov = (BDP.scprecopadariav[busca] + lucromaior) * scqtdevendaspadaria
                                    npv = BDP.scprecopadariav[busca] + lucromaior
                                    npc = BDP.scprecopadariac[busca] - precoreduzido
                                    lucro = (npv - npc) * scqtdevendaspadaria
                                    somaexp = (25 + BDP.maisexp) * scqtdevendaspadaria
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(scqtdevendaspadaria, busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.scqtdeprovendaspadaria[bv] += BDP.scqtdeprodutopadaria[busca1]
                                    BDP.dinheiro += ((BDP.scprecopadariav[busca] + lucromaior) *
                                                     BDP.scqtdeprodutopadaria[busca1])
                                    precov = ((BDP.scprecopadariav[busca] + lucromaior) *
                                              BDP.scqtdeprodutopadaria[busca1])
                                    npv = BDP.scprecopadariav[busca] + lucromaior
                                    npc = BDP.scprecopadariac[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.scqtdeprodutopadaria[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.scqtdeprodutopadaria[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(BDP.scqtdeprodutopadaria[busca1],
                                                                                  busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.scqtdeprodutopadaria[busca1] -= BDP.scqtdeprodutopadaria[busca1]
                                    sleep(2)

                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função padeiro.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um Caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        scdepositopadaria()
        break


def scvendaeletronica():
    while True:
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        scve2 = BDP.scqtdemoveiseletronica['Caixa'] * 2
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        lucromaior = BDP.levelhabi['lvhl'] * 2
        scqtdevendaseletronica = qtdevendaslevel * scve2
        if BDP.scqtdemoveiseletronica['Caixa'] >= 1:
            if BDP.scqtdefuncoeseletronica['Fcaixa'] >= 1:
                if BDP.scqtdefuncoeseletronica['Fatendente'] >= 1:
                    if sorteio == 0:
                        for item in BDP.scqtdeprodutoeletronica:
                            if BDP.scqtdeprodutoeletronica[item] >= 1:
                                busca = BDP.scprodutoseletronica.index(item)
                                busca1 = BDP.scprodutoseletronica[busca]
                                bv = BDP.scprodutovendaseletronica[busca]
                                if BDP.scqtdeprodutoeletronica[busca1] >= scqtdevendaseletronica:
                                    BDP.scqtdeprodutoeletronica[busca1] -= scqtdevendaseletronica
                                    BDP.scqtdeprovendaseletronica[bv] += scqtdevendaseletronica
                                    BDP.dinheiro += ((BDP.scprecoeletronicav[busca] + lucromaior) *
                                                     scqtdevendaseletronica)
                                    precov = (BDP.scprecoeletronicav[busca] + lucromaior) * scqtdevendaseletronica
                                    npv = BDP.scprecoeletronicav[busca] + lucromaior
                                    npc = BDP.scprecoeletronicac[busca] - precoreduzido
                                    lucro = (npv - npc) * scqtdevendaseletronica
                                    somaexp = (25 + BDP.maisexp) * scqtdevendaseletronica
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(scqtdevendaseletronica, busca1,
                                                                                  precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.scqtdeprovendaseletronica[bv] += BDP.scqtdeprodutoeletronica[busca1]
                                    BDP.dinheiro += ((BDP.scprecoeletronicav[busca] + lucromaior) *
                                                     BDP.scqtdeprodutoeletronica[busca1])
                                    precov = ((BDP.scprecoeletronicav[busca] + lucromaior) *
                                              BDP.scqtdeprodutoeletronica[busca1])
                                    npv = BDP.scprecoeletronicav[busca] + lucromaior
                                    npc = BDP.scprecoeletronicac[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.scqtdeprodutoeletronica[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.scqtdeprodutoeletronica[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(BDP.scqtdeprodutoeletronica[busca1],
                                                                                  busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.scqtdeprodutoeletronica[busca1] -= BDP.scqtdeprodutoeletronica[busca1]
                                    sleep(2)
                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função atendente.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        scdepositoeletronico()
        break


def scvendasupermercado():
    while True:
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        lucromaior = BDP.levelhabi['lvhl'] * 2
        scvs2 = BDP.scqtdemoveissupermercado['Caixa'] * 2
        scqtdevendassupermercado = qtdevendaslevel * scvs2
        if BDP.scqtdemoveissupermercado['Caixa'] >= 1:
            if BDP.scqtdefuncoessupermercado['Fcaixa'] >= 1:
                if BDP.scqtdefuncoessupermercado['Frepositor'] >= 1:
                    if sorteio == 0:
                        for item in BDP.scqtdeprodutosm:
                            if BDP.scqtdeprodutosm[item] >= 1:
                                busca = BDP.scprodutossm.index(item)
                                busca1 = BDP.scprodutossm[busca]
                                bv = BDP.scprodutovendasm[busca]
                                if BDP.scqtdeprodutosm[busca1] >= scqtdevendassupermercado:
                                    BDP.scqtdeprodutosm[busca1] -= scqtdevendassupermercado
                                    BDP.scqtdeprovendasupermercado[bv] += scqtdevendassupermercado
                                    BDP.dinheiro += (BDP.scprecovendasm[busca] + lucromaior) * scqtdevendassupermercado
                                    precov = (BDP.scprecovendasm[busca] + lucromaior) * scqtdevendassupermercado
                                    npv = BDP.scprecocomprasm[busca] + lucromaior
                                    npc = BDP.scprecovendasm[busca] - precoreduzido
                                    lucro = (npv - npc) * scqtdevendassupermercado
                                    somaexp = (25 + BDP.maisexp) * scqtdevendassupermercado
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(scqtdevendassupermercado, busca1,
                                                                                  precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.scqtdeprovendasupermercado[bv] += BDP.scqtdeprodutosm[busca1]
                                    BDP.dinheiro += ((BDP.scprecovendasm[busca] + lucromaior) *
                                                     BDP.scqtdeprodutosm[busca1])
                                    precov = ((BDP.scprecovendasm[busca] + lucromaior) *
                                              BDP.scqtdeprodutosm[busca1])
                                    npv = BDP.scprecocomprasm[busca] + lucromaior
                                    npc = BDP.scprecovendasm[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.scqtdeprodutosm[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.scqtdeprodutosm[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${:.2f}'.format(
                                        BDP.scqtdeprodutosm[busca1], busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.scqtdeprodutosm[busca1] -= BDP.scqtdeprodutosm[busca1]
                                    sleep(2)
                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função repositor.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        scdepositosupermercado()
        break


def spdepositoacougue():
    quantisaidadeposito = 0
    v = 0
    vm = 0

    if vm == 4:
        vm -= 4
    for _ in BDP.spmoveisacougue:
        ns = str(vm)
        buscamoveis = BDP.spnmoveisa.index(ns)
        busca1moveis = BDP.spmoveisacougue[buscamoveis]
        busca2moveis = BDP.splimiteitensmoveisacougue[vm]
        vm += 1
        if BDP.spqtdemoveisacougue[busca1moveis] >= 1:
            quantisaidadeposito += busca2moveis * BDP.spqtdemoveisacougue[busca1moveis]
    quantiproduto = 0
    somav = 0
    for deposito in BDP.spprodutosdepositoacougue:
        somav += BDP.spqtdeprodepositoacougue[deposito]
    for conta in BDP.spprodutosacougue:
        quantiproduto += BDP.spqtdeprodutoacougue[conta]
    falta = quantisaidadeposito - quantiproduto
    while True:
        vs = str(v)
        teste1 = 0
        buscaitem = BDP.spnpa.index(vs)
        buscad = BDP.spprodutosdepositoacougue[buscaitem]
        buscav = BDP.spprodutosacougue[buscaitem]
        if BDP.spqtdeprodepositoacougue[buscad] >= 1:
            if BDP.spqtdeprodepositoacougue[buscad] <= falta:
                BDP.spqtdeprodutoacougue[buscav] += BDP.spqtdeprodepositoacougue[buscad]
                BDP.spqtdeprodepositoacougue[buscad] -= BDP.spqtdeprodepositoacougue[buscad]
                teste1 += BDP.spqtdeprodutoacougue[buscav]

            elif BDP.spqtdeprodepositoacougue[buscad] > falta:
                BDP.spqtdeprodutoacougue[buscav] += falta
                BDP.spqtdeprodepositoacougue[buscad] -= falta
                teste1 += falta

        v += 1
        if v == 8:
            v -= 8
            break


# scdepositopadaria


def spdepositopadaria():
    v = 0

    saidaboleira = 0

    mesap = 0
    mesam = 0
    mesag = 0

    geladeirap = 0
    geladeiram = 0
    geladeirag = 0

    pasteleirap = 0
    pasteleiram = 0
    pasteleirag = 0

    prateleirap = 0
    prateleiram = 0
    prateleirag = 0

    saidatotal = 0

    saidaboleira += BDP.spqtdemoveispadaria['Boleira'] * BDP.splimiteitensmoveispadaria[1]

    mesap += BDP.spqtdemoveispadaria['MesaP'] * BDP.splimiteitensmoveispadaria[2]
    mesam += BDP.spqtdemoveispadaria['MesaM'] * BDP.splimiteitensmoveispadaria[3]
    mesag += BDP.spqtdemoveispadaria['MesaG'] * BDP.splimiteitensmoveispadaria[4]
    saidamesa = mesap + mesam + mesag

    geladeirap += BDP.spqtdemoveispadaria['GeladeiraP'] * BDP.splimiteitensmoveispadaria[5]
    geladeiram += BDP.spqtdemoveispadaria['GeladeiraM'] * BDP.splimiteitensmoveispadaria[6]
    geladeirag += BDP.spqtdemoveispadaria['GeladeiraG'] * BDP.splimiteitensmoveispadaria[7]
    saidageladeira = geladeirap + geladeiram + geladeirag

    pasteleirap += BDP.spqtdemoveispadaria['PasteleiraP'] * BDP.splimiteitensmoveispadaria[8]
    pasteleiram += BDP.spqtdemoveispadaria['PasteleiraM'] * BDP.splimiteitensmoveispadaria[9]
    pasteleirag += BDP.spqtdemoveispadaria['PasteleiraG'] * BDP.splimiteitensmoveispadaria[10]
    saidapasteleira = pasteleirap + pasteleiram + pasteleirag

    prateleirap += BDP.spqtdemoveispadaria['PrateleiraP'] * BDP.splimiteitensmoveispadaria[11]
    prateleiram += BDP.spqtdemoveispadaria['PrateleiraM'] * BDP.splimiteitensmoveispadaria[12]
    prateleirag += BDP.spqtdemoveispadaria['PrateleiraG'] * BDP.splimiteitensmoveispadaria[13]
    saidaprateleira = prateleirap + prateleiram + prateleirag

    saidatotal += saidaboleira + saidamesa + saidageladeira + saidapasteleira + saidaprateleira
    produtosboleira = 0

    while True:
        somav = 0
        for deposito in BDP.spprodutosdepositopadaria:
            somav += BDP.spqtdeprodepositopadaria[deposito]
        vs = str(v)
        if v == 17:
            v -= 17
            break
        buscaitem = BDP.spnpp.index(vs)
        buscad = BDP.spprodutosdepositopadaria[buscaitem]
        buscav = BDP.spprodutospadaria[buscaitem]
        teste1 = 0
        if BDP.spqtdeprodepositopadaria[buscad] >= 1:
            if buscad == 'dBolo':
                produtosboleira += BDP.spqtdeprodutopadaria['Bolo']
                faltaboleira = saidaboleira - produtosboleira
                if BDP.spqtdeprodepositopadaria[buscad] <= faltaboleira:
                    BDP.spqtdeprodutopadaria[buscav] += BDP.spqtdeprodepositopadaria[buscad]
                    BDP.spqtdeprodepositopadaria[buscad] -= BDP.spqtdeprodepositopadaria[buscad]
                    teste1 += BDP.spqtdeprodutopadaria[buscav]

                elif BDP.spqtdeprodepositopadaria[buscad] > faltaboleira:
                    BDP.spqtdeprodutopadaria[buscav] += faltaboleira
                    BDP.spqtdeprodepositopadaria[buscad] -= faltaboleira
                    teste1 += faltaboleira

            elif buscad == 'dCuca' or buscad == 'dPao' or buscad == 'dRosquinha':
                produtosmesa = (BDP.spqtdeprodutopadaria['Cuca'] + BDP.spqtdeprodutopadaria['Pao'] +
                                BDP.spqtdeprodutopadaria['Rosquinha'])
                faltamesa = saidamesa - produtosmesa
                if BDP.spqtdeprodepositopadaria[buscad] <= faltamesa:
                    BDP.spqtdeprodutopadaria[buscav] += BDP.spqtdeprodepositopadaria[buscad]
                    BDP.spqtdeprodepositopadaria[buscad] -= BDP.spqtdeprodepositopadaria[buscad]
                    teste1 += BDP.spqtdeprodutopadaria[buscav]

                elif BDP.spqtdeprodepositopadaria[buscad] > faltamesa:
                    BDP.spqtdeprodutopadaria[buscav] += faltamesa
                    BDP.spqtdeprodepositopadaria[buscad] -= faltamesa
                    teste1 += faltamesa

            if buscad == 'dBolinho' or buscad == 'dCoxinha' or buscad == 'dPao_de_queijo' or buscad == 'dPastel':
                produtospasteleira = (BDP.spqtdeprodutopadaria['Bolinho'] + BDP.spqtdeprodutopadaria['Coxinha'] +
                                      BDP.spqtdeprodutopadaria['Pao_de_queijo'] + BDP.spqtdeprodutopadaria['Pastel'])

                faltapasteleira = saidapasteleira - produtospasteleira
                if BDP.spqtdeprodepositopadaria[buscad] <= faltapasteleira:
                    BDP.spqtdeprodutopadaria[buscav] += BDP.spqtdeprodepositopadaria[buscad]
                    BDP.spqtdeprodepositopadaria[buscad] -= BDP.spqtdeprodepositopadaria[buscad]
                    teste1 += BDP.spqtdeprodutopadaria[buscav]

                elif BDP.spqtdeprodepositopadaria[buscad] > faltapasteleira:
                    BDP.spqtdeprodutopadaria[buscav] += faltapasteleira
                    BDP.spqtdeprodepositopadaria[buscad] -= faltapasteleira
                    teste1 += faltapasteleira

            if buscad == 'dBolacha' or buscad == 'dCafe':
                produtosprateleira = BDP.spqtdeprodutopadaria['Bolacha'] + BDP.spqtdeprodutopadaria['Cafe']
                faltaprateleira = saidaprateleira - produtosprateleira
                if BDP.spqtdeprodepositopadaria[buscad] <= faltaprateleira:
                    BDP.spqtdeprodutopadaria[buscav] += BDP.spqtdeprodepositopadaria[buscad]
                    BDP.spqtdeprodepositopadaria[buscad] -= BDP.spqtdeprodepositopadaria[buscad]
                    teste1 += BDP.spqtdeprodutopadaria[buscav]

                elif BDP.spqtdeprodepositopadaria[buscad] > faltaprateleira:
                    BDP.spqtdeprodutopadaria[buscav] += faltaprateleira
                    BDP.spqtdeprodepositopadaria[buscad] -= faltaprateleira
                    teste1 += faltaprateleira

            if (buscad == 'dLeite' or buscad == 'dMargarina' or buscad == 'dNata' or buscad == 'Presunto' or
                    buscad == 'dQueijo' or buscad == 'dSorvete' or buscad == 'dYogurt'):
                produtosgeladeira = (BDP.spqtdeprodutopadaria['Leite'] + BDP.spqtdeprodutopadaria['Margarina'] +
                                     BDP.spqtdeprodutopadaria['Nata'] + BDP.spqtdeprodutopadaria['Presunto'] +
                                     BDP.spqtdeprodutopadaria['Queijo'] + BDP.spqtdeprodutopadaria['Sorvete'] +
                                     BDP.spqtdeprodutopadaria['Yogurt'])
                faltageladeira = saidageladeira - produtosgeladeira
                if BDP.spqtdeprodepositopadaria[buscad] <= faltageladeira:
                    BDP.spqtdeprodutopadaria[buscav] += BDP.spqtdeprodepositopadaria[buscad]
                    BDP.spqtdeprodepositopadaria[buscad] -= BDP.spqtdeprodepositopadaria[buscad]
                    teste1 += BDP.spqtdeprodutopadaria[buscav]

                elif BDP.spqtdeprodepositopadaria[buscad] > faltageladeira:
                    BDP.spqtdeprodutopadaria[buscav] += faltageladeira
                    BDP.spqtdeprodepositopadaria[buscad] -= faltageladeira
                    teste1 += faltageladeira

        v += 1


def spdepositoeletronico():
    v = 0
    saidamesap = 0
    saidamesam = 0
    saidamesag = 0

    saidaprateleirap = 0
    saidaprateleiram = 0
    saidaprateleirag = 0

    saidamesap += BDP.splimiteitensmoveiseletronica[1] * BDP.spqtdemoveiseletronica['MesaP']
    saidamesam += BDP.splimiteitensmoveiseletronica[2] * BDP.spqtdemoveiseletronica['MesaM']
    saidamesag += BDP.splimiteitensmoveiseletronica[3] * BDP.spqtdemoveiseletronica['MesaG']
    saidamesa = saidamesap + saidamesam + saidamesag

    saidaprateleirap += BDP.splimiteitensmoveiseletronica[4] * BDP.spqtdemoveiseletronica['PrateleiraP']
    saidaprateleiram += BDP.splimiteitensmoveiseletronica[5] * BDP.spqtdemoveiseletronica['PrateleiraM']
    saidaprateleirag += BDP.splimiteitensmoveiseletronica[6] * BDP.spqtdemoveiseletronica['PrateleiraG']
    saidaprateleira = saidaprateleirap + saidaprateleiram + saidaprateleirag

    while True:
        somav = 0
        for deposito in BDP.spprodutosdepositoeletronica:
            somav += BDP.spqtdeprodepositoeletronica[deposito]
        vs = str(v)
        if v == 8:
            v -= 8
            break
        buscaitem = BDP.spnpe.index(vs)
        buscad = BDP.spprodutosdepositoeletronica[buscaitem]
        buscav = BDP.spprodutoseletronica[buscaitem]
        teste1 = 0
        if BDP.spqtdeprodepositoeletronica[buscad] >= 1:
            if (buscad == 'dCelular' or buscad == 'dComputador' or buscad == 'dNotebook' or buscad == 'dTablet' or
                    buscad == 'dTelevisao'):

                produtosmesa = (BDP.spqtdeprodutoeletronica['Celular'] + BDP.spqtdeprodutoeletronica['Computador'] +
                                BDP.spqtdeprodutoeletronica['Notebook'] + BDP.spqtdeprodutoeletronica['Tablet'] +
                                BDP.spqtdeprodutoeletronica['Televisao'])
                faltamesa = saidamesa - produtosmesa
                if BDP.spqtdeprodepositoeletronica[buscad] <= faltamesa:
                    BDP.spqtdeprodutoeletronica[buscav] += BDP.spqtdeprodepositoeletronica[buscad]
                    BDP.spqtdeprodepositoeletronica[buscad] -= BDP.spqtdeprodepositoeletronica[buscad]
                    teste1 += BDP.spqtdeprodutoeletronica[buscav]

                elif BDP.spqtdeprodepositoeletronica[buscad] > faltamesa:
                    BDP.spqtdeprodutoeletronica[buscav] += faltamesa
                    BDP.spqtdeprodepositoeletronica[buscad] -= faltamesa
                    teste1 += faltamesa

            elif buscad == 'dIpad' or buscad == 'dMouse' or buscad == 'dTeclado':
                produtosprateleira = (BDP.spqtdeprodutoeletronica['Ipad'] + BDP.spqtdeprodutoeletronica['Mouse'] +
                                      BDP.spqtdeprodutoeletronica['Teclado'])
                faltaprateleira = saidaprateleira - produtosprateleira
                if BDP.spqtdeprodepositoeletronica[buscad] <= faltaprateleira:
                    BDP.spqtdeprodutoeletronica[buscav] += BDP.spqtdeprodepositoeletronica[buscad]
                    BDP.spqtdeprodepositoeletronica[buscad] -= BDP.spqtdeprodepositoeletronica[buscad]
                    teste1 += BDP.spqtdeprodutoeletronica[buscav]

                elif BDP.spqtdeprodepositoeletronica[buscad] > faltaprateleira:
                    BDP.spqtdeprodutoeletronica[buscav] += faltaprateleira
                    BDP.spqtdeprodepositoeletronica[buscad] -= faltaprateleira
                    teste1 += faltaprateleira

        v += 1


def spdepositosupermercado():
    v = 0
    saidafruteirap = 0
    saidafruteiram = 0
    saidafruteirag = 0

    saidaprateleirap = 0
    saidaprateleiram = 0
    saidaprateleirag = 0

    saidafruteirap += BDP.splimiteitensmoveissm[1] * BDP.spqtdemoveissupermercado['FruteiraP']
    saidafruteiram += BDP.splimiteitensmoveissm[2] * BDP.spqtdemoveissupermercado['FruteiraM']
    saidafruteirag += BDP.splimiteitensmoveissm[3] * BDP.spqtdemoveissupermercado['FruteiraG']
    saidafruteira = saidafruteirap + saidafruteiram + saidafruteirag

    saidaprateleirap += BDP.splimiteitensmoveissm[4] * BDP.spqtdemoveissupermercado['PrateleiraP']
    saidaprateleiram += BDP.splimiteitensmoveissm[5] * BDP.spqtdemoveissupermercado['PrateleiraM']
    saidaprateleirag += BDP.splimiteitensmoveissm[6] * BDP.spqtdemoveissupermercado['PrateleiraG']
    saidaprateleira = saidaprateleirap + saidaprateleiram + saidaprateleirag

    while True:
        somafv = 0
        somalhg = 0
        for produtos in range(0, 34):
            n = str(produtos)
            buscafv = BDP.spnprodutossm.index(n)
            busca1fv = BDP.spprodutossm[buscafv]
            if busca1fv in BDP.spprodutossupermercadofv:
                somafv += BDP.spqtdeprodutosm[busca1fv]
            elif busca1fv in BDP.spprodutossupermercadolh or BDP.spprodutossupermercadog:
                somalhg += BDP.spqtdeprodutosm[busca1fv]

        vs = str(v)
        if v == 34:
            v -= 34
            break
        buscaitem = BDP.spnprodutossm.index(vs)
        buscad = BDP.spprodutosdepositosm[buscaitem]
        buscav = BDP.spprodutossm[buscaitem]
        teste1 = 0
        if BDP.spqtdeprodepositosm[buscad] >= 1:
            if buscad in BDP.spprodutosdepositosmfv:
                faltafruteira = saidafruteira - somafv
                if BDP.spqtdeprodepositosm[buscad] <= faltafruteira:
                    BDP.spqtdeprodutosm[buscav] += BDP.spqtdeprodepositosm[buscad]
                    BDP.spqtdeprodepositosm[buscad] -= BDP.spqtdeprodepositosm[buscad]
                    teste1 += BDP.spqtdeprodutosm[buscav]

                elif BDP.spqtdeprodepositosm[buscad] > faltafruteira:
                    BDP.spqtdeprodutosm[buscav] += faltafruteira
                    BDP.spqtdeprodepositosm[buscad] -= faltafruteira
                    teste1 += faltafruteira

            if buscad in BDP.spprodutosdepositosmlh or buscad in BDP.spprodutosdepositosmg:
                faltaprateleira = saidaprateleira - somalhg
                if BDP.spqtdeprodepositosm[buscad] <= faltaprateleira:
                    BDP.spqtdeprodutosm[buscav] += BDP.spqtdeprodepositosm[buscad]
                    BDP.spqtdeprodepositosm[buscad] -= BDP.spqtdeprodepositosm[buscad]
                    teste1 += BDP.spqtdeprodutosm[buscav]

                elif BDP.spqtdeprodepositosm[buscad] > faltaprateleira:
                    BDP.spqtdeprodutosm[buscav] += faltaprateleira
                    BDP.spqtdeprodepositosm[buscad] -= faltaprateleira
                    teste1 += faltaprateleira

        v += 1


def spcontratarfuncionarioacougue():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        sleep(1)
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SPDentro_Mercado_Acougue()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.spqtdefuncionariosacougue['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.spqtdefuncionariosacougue['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoesacougue)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoesacougue[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoesacougue['Fcaixa'] == 0:
                                            BDP.spqtdefuncoesacougue['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoesacougue['Facougueiro'] == 0:
                                            BDP.spqtdefuncoesacougue['Facougueiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.spqtdefuncionariosacougue['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.spqtdefuncionariosacougue['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoesacougue)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoesacougue[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoesacougue['Fcaixa'] == 0:
                                            BDP.spqtdefuncoesacougue['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoesacougue['Facougueiro'] == 0:
                                            BDP.spqtdefuncoesacougue['Facougueiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SPDentro_Mercado_Acougue()


def spcontratarfuncionariopadaria():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        sleep(1)
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SPDentro_Mercado_Padaria()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.spqtdefuncionariospadaria['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.spqtdefuncionariospadaria['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoespadaria)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoespadaria[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoespadaria['Fcaixa'] == 0:
                                            BDP.spqtdefuncoespadaria['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoespadaria['Fpadeiro'] == 0:
                                            BDP.spqtdefuncoespadaria['Fpadeiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.spqtdefuncionariospadaria['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.spqtdefuncionariospadaria['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoespadaria)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoespadaria[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoespadaria['Fcaixa'] == 0:
                                            BDP.spqtdefuncoespadaria['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoespadaria['Fpadeiro'] == 0:
                                            BDP.spqtdefuncoesacougue['Fpadeiro'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SPDentro_Mercado_Padaria()


def spcontratarfuncionarioeletronica():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        sleep(1)
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SPDentro_Mercado_Eletronica()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.spqtdefuncionarioseletronica['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.spqtdefuncionarioseletronica['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoeseletronica)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoeseletronica[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoeseletronica['Fcaixa'] == 0:
                                            BDP.spqtdefuncoeseletronica['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoeseletronica['Fatendente'] == 0:
                                            BDP.spqtdefuncoeseletronica['Fatendente'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.spqtdefuncionarioseletronica['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.spqtdefuncionarioseletronica['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoeseletronica)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoeseletronica[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoeseletronica['Fcaixa'] == 0:
                                            BDP.spqtdefuncoeseletronica['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoeseletronica['Fatendente'] == 0:
                                            BDP.spqtdefuncoeseletronica['Fatendente'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SPDentro_Mercado_Eletronica()


def spcontratarfuncionariosupermercado():
    while True:
        fun = len(BDP.funcionario)
        print('Contratar:')
        for f in range(fun):
            print('[{}] {} salário de R${}.'.format(f, BDP.funcionario[f], BDP.precofuncionario[f]))
        print('[C] Cancelar.')
        sleep(1)
        while True:
            funcionario1 = str(input('Que funcionário(a) você quer contratar: ')).strip(' ').title()
            if funcionario1 in 'C':
                SPDentro_Mercado_SuperMercado()
            elif funcionario1 in BDP.nfuncionario:
                busca = BDP.nfuncionario.index(funcionario1)
                busca0 = BDP.funcionario[busca]
                valorf1 = BDP.precofuncionario[busca]
                if funcionario1 in '0':
                    if BDP.spqtdefuncionariossupermercado['Daniel'] == 1:
                        print('\033[33mErro: \033[mVocê já tem esse funcionário.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[0]:
                            BDP.spqtdefuncionariossupermercado['Daniel'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoessupermercado)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoessupermercado[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoessupermercado['Fcaixa'] == 0:
                                            BDP.spqtdefuncoessupermercado['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoessupermercado['Frepositor'] == 0:
                                            BDP.spqtdefuncoessupermercado['Frepositor'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
                elif funcionario1 in '1':
                    if BDP.spqtdefuncionariossupermercado['Jhennyfer'] == 1:
                        print('\033[33mErro: \033[mVocê já tem essa funcionária.')
                        sleep(2)
                    else:
                        if BDP.dinheiro >= BDP.precofuncionario[1]:
                            BDP.spqtdefuncionariossupermercado['Jhennyfer'] += 1
                            while True:
                                tamanho = len(BDP.spfuncoessupermercado)
                                print('Funcão para {}:'.format(busca0))
                                for fa in range(tamanho):
                                    print('[{}] {}.'.format(fa, BDP.spfuncoessupermercado[fa]))
                                while True:
                                    tecla = input('Tecla: ')
                                    if tecla in '0':
                                        if BDP.spqtdefuncoessupermercado['Fcaixa'] == 0:
                                            BDP.spqtdefuncoessupermercado['Fcaixa'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')

                                    elif tecla in '1':
                                        if BDP.spqtdefuncoessupermercado['Frepositor'] == 0:
                                            BDP.spqtdefuncoessupermercado['Frepositor'] += 1
                                            break
                                        else:
                                            print('\033[33mErro: \033[mSeu funcionário já tem essa função.')
                                    else:
                                        print('\033[31mErro: \033[mOpção inválida.')
                                BDP.dinheiro -= valorf1
                                print('Você teve um gasto de R${} com o funcionário.'.format(valorf1))
                                sleep(2)
                                break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                            sleep(1)
                    break
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        SPDentro_Mercado_SuperMercado()


def SPDentro_Mercado_Acougue():
    while True:
        spvendaacougue()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar Açougue.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in 'C':
                        break
                    elif tecla1 in '0':
                        splojamoveisacougue()
                        break

                    elif tecla1 in '1':
                        spmercadoacougue()
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break

            elif tecla in '1':
                spcontratarfuncionarioacougue()
                break

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                spvendaacougue()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos.')
                print('[2] Quantidade de produtos no depósito')
                print('[3] Quantidade de vendas.')
                print('[4] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveisacougue in BDP.spqtdemoveisacougue:
                            print('{} = {}'.format(moveisacougue, BDP.spqtdemoveisacougue[moveisacougue]))
                        sleep(1)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtoacougue in BDP.spqtdeprodutoacougue:
                            print('{} = {}'.format(produtoacougue, BDP.spqtdeprodutoacougue[produtoacougue]))
                        sleep(2)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositoacougue in BDP.spqtdeprodepositoacougue:
                            print('{} = {}'.format(depositoacougue, BDP.spqtdeprodepositoacougue[depositoacougue]))
                        sleep(2)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendaacougue in BDP.spqtdeprovendasacougue:
                            print('{} = {}'.format(vendaacougue, BDP.spqtdeprovendasacougue[vendaacougue]))
                        sleep(2)
                        break

                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funciacougue in BDP.spqtdefuncionariosacougue:
                            print('{} = {}'.format(funciacougue, BDP.spqtdefuncionariosacougue[funciacougue]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def SPDentro_Mercado_Padaria():
    while True:
        spvendapadaria()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar Padaria.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in 'C':
                        break
                    if tecla1 in '0':
                        splojamoveispadaria()
                        break

                    elif tecla1 in '1':
                        spmercadopadaria()
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')

            elif tecla in '1':
                spcontratarfuncionariopadaria()
                break

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                spvendapadaria()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no deposito.')
                print('[3] Quantindade de vendas')
                print('[4] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveispadaria in BDP.spqtdemoveispadaria:
                            print('{} = {}'.format(moveispadaria, BDP.spqtdemoveispadaria[moveispadaria]))
                        sleep(2)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtopadaria in BDP.spqtdeprodutopadaria:
                            print('{} = {}'.format(produtopadaria, BDP.spqtdeprodutopadaria[produtopadaria]))
                        sleep(2)
                        break
                    elif tecla2 in '2':
                        print('Quantidade de produtos no deposito:')
                        for vendapadaria in BDP.spqtdeprodepositopadaria:
                            print('{} = {}'.format(vendapadaria, BDP.spqtdeprodepositopadaria[vendapadaria]))
                        sleep(2)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for depositopadaria in BDP.spqtdeprovendaspadaria:
                            print('{} = {}'.format(depositopadaria, BDP.spqtdeprovendaspadaria[depositopadaria]))
                        sleep(3)
                        break

                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funcipadaria in BDP.spqtdefuncionariospadaria:
                            print('{} = {}'.format(funcipadaria, BDP.spqtdefuncionariospadaria[funcipadaria]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def SPDentro_Mercado_Eletronica():
    while True:
        spvendaeletronica()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar Loja Eletronica.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in 'C':
                        break
                    elif tecla1 in '0':
                        splojamoveiseletronica()
                        break

                    elif tecla1 in '1':
                        spmercadoeletronica()
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break

            elif tecla in '1':
                spcontratarfuncionarioeletronica()
                break

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                spvendaeletronica()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no deposito.')
                print('[3] Quantidade de vendas.')
                print('[4] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveiseletro in BDP.spqtdemoveiseletronica:
                            print('{} = {}'.format(moveiseletro, BDP.spqtdemoveiseletronica[moveiseletro]))
                        sleep(1)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos:')
                        for produtoeletro in BDP.spqtdeprodutoeletronica:
                            print('{} = {}'.format(produtoeletro, BDP.spqtdeprodutoeletronica[produtoeletro]))
                        sleep(2)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositoele in BDP.spqtdeprodepositoeletronica:
                            print('{} = {}'.format(depositoele, BDP.spqtdeprodepositoeletronica[depositoele]))
                        sleep(3)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendaeletro in BDP.spqtdeprovendaseletronica:
                            print('{} = {}'.format(vendaeletro, BDP.spqtdeprovendaseletronica[vendaeletro]))
                        sleep(2)
                        break

                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funcieletro in BDP.spqtdefuncionarioseletronica:
                            print('{} = {}'.format(funcieletro, BDP.spqtdefuncionarioseletronica[funcieletro]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def SPDentro_Mercado_SuperMercado():
    while True:
        spvendasupermercado()
        sistemalevel()
        print('Funções de controle:')
        print('[0] Fazer Compras.')
        print('[1] Contratar Funcionários.')
        print('[2] Mostrar Saldos.')
        print('[3] Tentar Vender.')
        print('[4] Mostrar SuperMercado.')
        print('[C] Voltar.')
        while True:
            tecla = input('Tecla: ').title().strip()
            if tecla in 'C':
                JogoInicio()
            if tecla in '0':
                while True:
                    print('[0] Comprar móveis.')
                    print('[1] Comprar produtos.')
                    print('[C] Voltar.')
                    tecla1 = input('Tecla: ').title()
                    if tecla1 in '0':
                        splojamoveissupermercado()
                        break

                    elif tecla1 in '1':
                        spmercadosupermercado()
                        break

                    elif tecla1 in 'C':
                        break

                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            elif tecla in '1':
                spcontratarfuncionariosupermercado()
                break

            elif tecla in '2':
                while True:
                    print('[0] Ver saldo.')
                    print('[1] Comprar diamante.')
                    print('[2] Comprar dinheiro.')
                    print('[C] Voltar.')
                    while True:
                        tecla1 = input('Tecla: ').strip().title()
                        if tecla1 in 'C':
                            break
                        if tecla1 in '0':
                            print('Dinheiro = {:.2f}'.format(BDP.dinheiro))
                            print('Dima = {}'.format(BDP.diamante))
                            sleep(1)
                            break
                        elif tecla1 in '1':
                            print('1 diamante = R$500')
                            qtdemaxima = BDP.dinheiro / 500
                            while True:
                                print('Compra máxima de {:.0f} diamante'.format(trunc(qtdemaxima)))
                                qtde = int(input('Quantidade: '))
                                total = 500 * qtde
                                if BDP.dinheiro >= total:
                                    BDP.dinheiro -= total
                                    BDP.diamante += qtde
                                    print('Você comprou {} diamante por R${}'.format(qtde, total))
                                    sleep(1)
                                    break
                                else:
                                    print('\033[33mErro: \033[mDiamante insuficiente.')
                            break
                        elif tecla1 in '2':
                            while True:
                                print('[0] R$500 = 1 diamante')
                                print('[1] R$2500 = 5 diamante')
                                print('[2] R$5000 = 10 diamante')
                                print('[C] Voltar')
                                while True:
                                    qtdemaxima = BDP.diamante * 500
                                    print('Compra máxima de R${:.0f}'.format(trunc(qtdemaxima)))
                                    tecla2 = input('Tecla: ').strip().title()
                                    if tecla2 in 'C':
                                        break
                                    if tecla2 in '0':
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
                                    else:
                                        print('\033[31mErro:  \033[mOpção inválida.')
                                break
                            break
                        else:
                            print('\033[31mErro:  \033[mOpção inválida.')
                    break

            elif tecla in '3':
                spvendasupermercado()
                break

            elif tecla in '4':
                print('[0] Quantidade de móveis.')
                print('[1] Quantidade de produtos na venda.')
                print('[2] Quantidade de produtos no deposito.')
                print('[3] Quantidade de vendas.')
                print('[4] Funcionários.')
                while True:
                    tecla2 = input('Tecla: ').strip(' ').title()
                    if tecla2 in '0':
                        print('Quantidade de móveis:')
                        for moveissm in BDP.spqtdemoveissupermercado:
                            print('{} = {}'.format(moveissm, BDP.spqtdemoveissupermercado[moveissm]))
                        sleep(1)
                        break

                    elif tecla2 in '1':
                        print('Quantidade de produtos na venda:')
                        for produtosfvsm in BDP.spqtdeprodutosm:
                            print('{} = {}'.format(produtosfvsm, BDP.spqtdeprodutosm))
                        sleep(3)
                        break

                    elif tecla2 in '2':
                        print('Quantidade de produtos no depósito:')
                        for depositosm in BDP.spqtdeprodepositosm:
                            print('{} = {}'.format(depositosm, BDP.spqtdeprodepositosm[depositosm]))
                        sleep(3)
                        break

                    elif tecla2 in '3':
                        print('Quantidade de vendas:')
                        for vendasfvsm in BDP.spqtdeprovendasupermercado:
                            print('{} = {}'.format(vendasfvsm, BDP.spqtdeprovendasupermercado[vendasfvsm]))
                        sleep(3)
                        break
                    elif tecla2 in '4':
                        print('Funcionários:')
                        for funcism in BDP.spqtdefuncionariossupermercado:
                            print('{} = {}'.format(funcism, BDP.spqtdefuncionariossupermercado[funcism]))
                        sleep(1)
                        break
                    else:
                        print('\033[31mErro: \033[mOpção inválida.')
                break
            else:
                print('\033[31mErro: \033[mOpção inválida.')
            break


def splojamoveisacougue():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.spmoveisacougue)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.spmoveisacougue[i], BDP.splimiteitensmoveisacougue[i],
                                                   BDP.spprecomoveisacougue[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SPDentro_Mercado_Acougue()
        elif compramoveis1 in BDP.spnmoveisa:
            buscamoveisa = BDP.spnmoveisa.index(compramoveis1)
            busca1moveisa = BDP.spmoveisacougue[buscamoveisa]
            custola = BDP.spprecomoveisacougue[buscamoveisa]
            while True:
                qtdemaxima = BDP.dinheiro / custola
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1la = int(input('Quantidade de {}: '.format(busca1moveisa)))
                valortotal = custola * quantimoveis1la
                if quantimoveis1la < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')

            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada. totalizando R${:.2f} com {}'
                  ' móveis.'.format(busca1moveisa, custola, valortotal, quantimoveis1la))
            sleep(3)
            BDP.spqtdemoveisacougue[busca1moveisa] += quantimoveis1la
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SPDentro_Mercado_Acougue()


def spmercadoacougue():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    precoreduzido = BDP.levelhabi['lvhp'] * 0.50
    tamanho = len(BDP.spprodutosacougue)
    for i in range(tamanho):
        print('[{}] {} R${}.'.format(i, BDP.spprodutosacougue[i], BDP.spprecoacouguec[i] - precoreduzido))
    print('[C] Voltar.')
    while True:
        compraproduto1 = input('Que produto voce quer comprar para seu mercado: ').strip(' ').title()
        if compraproduto1 in BDP.scnpa:
            if (BDP.spqtdemoveisacougue['FreezerP'] or BDP.spqtdemoveisacougue['FreezerM'] or
                    BDP.spqtdemoveisacougue['FreezerG'] >= 1):
                buscamercadoa = BDP.spnpa.index(compraproduto1)
                busca1mercadoa = BDP.spprodutosacougue[buscamercadoa]
                buscaitem = BDP.spprodutosdepositoacougue[buscamercadoa]
                customa = BDP.spprecoacouguec[buscamercadoa] - precoreduzido
                while True:
                    qtdemaxima = BDP.dinheiro / customa
                    print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                    quantiproduto1ma = int(input('Quantidade de {}: '.format(busca1mercadoa)))
                    valortotalpma = customa * quantiproduto1ma
                    sleep(1)
                    if quantiproduto1ma < 0:
                        print('\033[33mErro: \033[mQuantidade não permitido, \033[0;33mlimite de 1 até 300\033[m.')
                    else:
                        if BDP.dinheiro >= valortotalpma:
                            break
                        else:
                            print('\033[33mErro: \033[mDinheiro insuficiente.')
                BDP.dinheiro -= valortotalpma
                print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'.format(
                    busca1mercadoa, customa, valortotalpma, quantiproduto1ma))
                sleep(3)
                BDP.spqtdeprodepositoacougue[buscaitem] += quantiproduto1ma
                break
            else:
                print('\033[33mErro: \033[mVocê não tem um freezer.')
                print('Vá para uma loja de móveis.')
                sleep(3)
                break
        elif compraproduto1 in 'C':
            SPDentro_Mercado_Acougue()
        else:
            print('\033[31mErro: \033[mOpção inválida.')
        break

    SPDentro_Mercado_Acougue()


def splojamoveispadaria():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.spmoveispadaria)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.spmoveispadaria[i], BDP.splimiteitensmoveispadaria[i],
                                                   BDP.spprecomoveispadaria[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SPDentro_Mercado_Padaria()
        elif compramoveis1 in BDP.spnmoveisp:
            buscamoveisp = BDP.spnmoveisp.index(compramoveis1)
            busca1moveisp = BDP.spmoveispadaria[buscamoveisp]
            custolp = BDP.spprecomoveispadaria[buscamoveisp]
            while True:
                qtdemaxima = BDP.dinheiro / custolp
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1 = int(input('Quantidade de {}: '.format(busca1moveisp)))
                valortotal = custolp * quantimoveis1
                if quantimoveis1 < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')

            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveisp, custolp, valortotal, quantimoveis1))
            sleep(3)
            BDP.spqtdemoveispadaria[busca1moveisp] += quantimoveis1
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SPDentro_Mercado_Padaria()


def spmercadopadaria():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        tamanho = len(BDP.spprodutospadaria)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, BDP.spprodutospadaria[i], BDP.spprecopadariac[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = str(input('Que produto voce quer comprar para seu mercado: ')).strip(' ').title()
            pasteleira = ['1', '4', '10', '11']
            prateleira = ['0', '3']
            mesa = ['5', '9', '14']
            geladeira = ['6', '7', '8', '12', '13', '15', '16']
            if compraproduto1 in 'C':
                SPDentro_Mercado_Padaria()
            if compraproduto1 in pasteleira:
                if (BDP.spqtdemoveispadaria['PasteleiraP'] or BDP.spqtdemoveispadaria['PasteleiraM'] or
                        BDP.spqtdemoveispadaria['PasteleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma pasteleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Padaria()

            elif compraproduto1 in '2':
                if BDP.spqtdemoveispadaria['Boleira'] >= 1:
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma boleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Padaria()

            elif compraproduto1 in prateleira:
                if (BDP.spqtdemoveispadaria['PrateleiraP'] or BDP.spqtdemoveispadaria['PrateleiraM'] or
                        BDP.spqtdemoveispadaria['PrateleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Padaria()

            elif compraproduto1 in mesa:
                if (BDP.spqtdemoveispadaria['MesaP'] or BDP.spqtdemoveispadaria['MesaM'] or
                        BDP.spqtdemoveispadaria['MesaG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma mesa.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Padaria()

            elif compraproduto1 in geladeira:
                if (BDP.spqtdemoveispadaria['GeladeiraP'] or BDP.spqtdemoveispadaria['GeladeiraM'] or
                        BDP.spqtdemoveispadaria['GeladeiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma geladeira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Padaria()

            else:
                print('\033[31mErro: \033[mOpção inválida.')

        buscamercadop = BDP.spnpp.index(compraproduto1)
        busca1mercadop = BDP.spprodutospadaria[buscamercadop]
        buscaitem = BDP.spprodutosdepositopadaria[buscamercadop]
        customp = BDP.spprecopadariac[buscamercadop] - precoreduzido
        while True:
            qtdemaxima = BDP.dinheiro / customp
            print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            quantiproduto1mp = int(input('Quantidade de {}: '.format(busca1mercadop)))
            valortotalpmp = customp * quantiproduto1mp
            sleep(1)
            if quantiproduto1mp < 0:
                print('\033[33mErro: \033[mQuantidade não permitido, \033[0;33mlimite de 1 até 300\033[m.')
            else:
                if BDP.dinheiro >= valortotalpmp:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')

        BDP.dinheiro -= valortotalpmp
        print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'
              .format(busca1mercadop, customp, valortotalpmp, quantiproduto1mp))
        sleep(3)
        BDP.spqtdeprodepositopadaria[buscaitem] += quantiproduto1mp
        break

    SPDentro_Mercado_Padaria()


def splojamoveiseletronica():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.spmoveiseletronica)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.spmoveiseletronica[i],
                                                   BDP.splimiteitensmoveiseletronica[i],
                                                   BDP.spprecomoveiseletronica[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SPDentro_Mercado_Eletronica()
        elif compramoveis1 in BDP.spnmoveise:
            buscamoveise = BDP.spnmoveise.index(compramoveis1)
            busca1moveise = BDP.spmoveiseletronica[buscamoveise]
            custome = BDP.spprecomoveiseletronica[buscamoveise]
            while True:
                qtdemaxima = BDP.dinheiro / custome
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1 = int(input('Quantidade de {}: '.format(busca1moveise)))
                valortotal = custome * quantimoveis1
                if quantimoveis1 < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')

            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveise, custome, valortotal, quantimoveis1))
            sleep(3)
            BDP.spqtdemoveiseletronica[busca1moveise] += quantimoveis1
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SPDentro_Mercado_Eletronica()


def spmercadoeletronica():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        tamanho = len(BDP.spprodutoseletronica)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, BDP.spprodutoseletronica[i], BDP.spprecoeletronicac[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = input('Que produto voce quer comprar para seu mercado: ').strip(' ').title()
            mesa = ['0', '1', '4', '5', '7']
            prateleira = ['2', '3', '6']
            if compraproduto1 in mesa:
                if (BDP.spqtdemoveiseletronica['MesaP'] or BDP.spqtdemoveiseletronica['MesaM'] or
                        BDP.spqtdemoveiseletronica['MesaG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma mesa.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Eletronica()
            elif compraproduto1 in prateleira:
                if (BDP.spqtdemoveiseletronica['PrateleiraP'] or BDP.spqtdemoveiseletronica['PrateleiraM'] or
                        BDP.spqtdemoveiseletronica['PrateleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_Eletronica()

            elif compraproduto1 in 'C':
                SPDentro_Mercado_Eletronica()
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        busca = BDP.spnpe.index(compraproduto1)
        busca1 = BDP.spprodutoseletronica[busca]
        buscaitem = BDP.spprodutosdepositoeletronica[busca]
        custo = BDP.spprecoeletronicac[busca] - precoreduzido
        while True:
            qtdemaxima = BDP.dinheiro / custo
            print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            quantiproduto1 = int(input('Quantidade: '))
            valortotalp = custo * quantiproduto1
            sleep(1)
            if quantiproduto1 < 0:
                print('\033[33mErro: \033[mQuantidade não permitido, \033[0;33mlimite de 1 até 300\033[m.')
            else:
                if BDP.dinheiro >= valortotalp:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')

        BDP.dinheiro -= valortotalp
        print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'
              .format(busca1, custo, valortotalp, quantiproduto1))
        sleep(3)
        BDP.spqtdeprodepositoeletronica[buscaitem] += quantiproduto1
        break

    SPDentro_Mercado_Eletronica()


def splojamoveissupermercado():
    print('==' * 10)
    print('\033[34mLoja de Móveis:\033[m')
    print('==' * 10)
    sleep(1)
    tamanho = len(BDP.spmoveissupermercado)
    for i in range(tamanho):
        print('[{}] {} ({} produtos) R${}.'.format(i, BDP.spmoveissupermercado[i], BDP.splimiteitensmoveissm[i],
                                                   BDP.spprecomoveissupermercado[i]))
    print('[C] voltar.')
    while True:
        compramoveis1 = input('Que Móveis você quer comprar para seu mercado: ').strip(' ').title()
        if compramoveis1 in 'C':
            SPDentro_Mercado_SuperMercado()
        elif compramoveis1 in BDP.spnmoveiss:
            buscamoveiss = BDP.spnmoveiss.index(compramoveis1)
            busca1moveiss = BDP.spmoveissupermercado[buscamoveiss]
            custolp = BDP.spprecomoveissupermercado[buscamoveiss]
            while True:
                qtdemaxima = BDP.dinheiro / custolp
                print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
                quantimoveis1 = int(input('Quantidade de {}: '.format(busca1moveiss)))
                valortotal = custolp * quantimoveis1
                if quantimoveis1 < 0:
                    print('\033[33mErro: \033[mQuantidade não permitido')
                else:
                    if BDP.dinheiro >= valortotal:
                        break
                    else:
                        print('\033[33mErro: \033[mDinheiro insuficiente.')

            BDP.dinheiro -= valortotal
            print('Na loja de móveis, o móvel {} custa R${} cada.'
                  ' totalizando R${:.2f} com {} móveis.'.format(busca1moveiss, custolp, valortotal, quantimoveis1))
            sleep(3)
            BDP.spqtdemoveissupermercado[busca1moveiss] += quantimoveis1
            break
        else:
            print('\033[31mErro: \033[mOpção inválida.')

    SPDentro_Mercado_SuperMercado()


def spmercadosupermercado():
    print('==' * 10)
    print('\033[34mMercado Do Zé:\033[m')
    print('==' * 10)
    sleep(1)
    while True:
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        ntpsm = BDP.spnpsfv + BDP.spnpslh + BDP.spnpsg
        tpsm = BDP.spprodutossupermercadofv + BDP.spprodutossupermercadolh + BDP.spprodutossupermercadog
        tppsm = BDP.spprecosupermercadocfv + BDP.spprecosupermercadoclh + BDP.spprecosupermercadocg
        tamanho = len(tpsm)
        for i in range(tamanho):
            print('[{}] {} R${}.'.format(i, tpsm[i], tppsm[i] - precoreduzido))
        print('[C] Voltar.')
        while True:
            compraproduto1 = str(input('Que produto voce quer comprar para seu mercado: ')).strip(' ').title()
            if compraproduto1 in 'C':
                SPDentro_Mercado_SuperMercado()

            elif compraproduto1 in BDP.spnpsfv:
                if (BDP.spqtdemoveissupermercado['FruteiraP'] or BDP.spqtdemoveissupermercado['FruteiraM'] or
                        BDP.spqtdemoveissupermercado['FruteiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma fruteira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_SuperMercado()

            elif compraproduto1 in BDP.scnpslh or compraproduto1 in BDP.scnpsg:
                if (BDP.spqtdemoveissupermercado['PrateleiraP'] or BDP.spqtdemoveissupermercado['PrateleiraM'] or
                        BDP.spqtdemoveissupermercado['PrateleiraG'] >= 1):
                    break
                else:
                    print('\033[33mErro: \033[mVocê não tem uma prateleira.')
                    print('Vá para uma loja de móveis.')
                    sleep(3)
                    SPDentro_Mercado_SuperMercado()
            else:
                print('\033[31mErro: \033[mOpção inválida.')

        buscamercado = ntpsm.index(compraproduto1)
        busca1mercado = tpsm[buscamercado]
        buscaitem = BDP.spprodutosdepositosm[buscamercado]
        custo = tppsm[buscamercado] - precoreduzido
        while True:
            qtdemaxima = BDP.dinheiro / custo
            print('Compra máxima de {:.0f} unidade'.format(trunc(qtdemaxima)))
            quantiproduto1 = int(input('Quantidade: '))
            valortotal = custo * quantiproduto1
            sleep(1)
            if quantiproduto1 < 0:
                print('\033[33mErro: \033[mQuantidade não permitido, \033[0;33mlimite de 1 até 300\033[m.')
            else:
                if BDP.dinheiro >= valortotal:
                    break
                else:
                    print('\033[33mErro: \033[mDinheiro insuficiente.')

        BDP.dinheiro -= valortotal
        print('No mercado, o produto {} custa R${} cada. totalizando R${:.2f} com {} unidades.'
              .format(busca1mercado, custo, valortotal, quantiproduto1))
        sleep(3)
        BDP.spqtdeprodepositosm[buscaitem] += quantiproduto1
        break

    SPDentro_Mercado_SuperMercado()


def spvendaacougue():
    while True:
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        lucromaior = BDP.levelhabi['lvhl'] * 2
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        spva2 = BDP.spqtdemoveisacougue['Caixa'] * 2
        spqtdevendasacougue = qtdevendaslevel * spva2
        if BDP.spqtdemoveisacougue['Caixa'] >= 1:
            if BDP.spqtdefuncoesacougue['Fcaixa'] >= 1:
                if BDP.spqtdefuncoesacougue['Facougueiro'] >= 1:
                    if sorteio == 0:
                        for item in BDP.spqtdeprodutoacougue:
                            if BDP.spqtdeprodutoacougue[item] >= spqtdevendasacougue:
                                busca = BDP.spprodutosacougue.index(item)
                                busca1 = BDP.spprodutosacougue[busca]
                                bv = BDP.spprodutovendasacougue[busca]
                                if BDP.spqtdeprodutoacougue[busca1] >= spqtdevendasacougue:
                                    BDP.spqtdeprodutoacougue[busca1] -= spqtdevendasacougue
                                    BDP.spqtdeprovendasacougue[bv] += spqtdevendasacougue
                                    BDP.dinheiro += (BDP.spprecoacouguev[busca] + lucromaior) * spqtdevendasacougue
                                    precov = (BDP.spprecoacouguev[busca] + lucromaior) * spqtdevendasacougue
                                    npv = BDP.spprecoacouguev[busca] + lucromaior
                                    npc = BDP.spprecoacouguec[busca] - precoreduzido
                                    lucro = (npv - npc) * spqtdevendasacougue
                                    somaexp = (25 + BDP.maisexp) * spqtdevendasacougue
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${}'.format(spqtdevendasacougue, busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.spqtdeprovendasacougue[bv] += BDP.spqtdeprodutoacougue[busca1]
                                    BDP.dinheiro += ((BDP.spprecoacouguev[busca] + lucromaior) *
                                                     BDP.spqtdeprodutoacougue[busca1])
                                    precov = ((BDP.spprecoacouguev[busca] + lucromaior) *
                                              BDP.spqtdeprodutoacougue[busca1])
                                    npv = BDP.spprecoacouguev[busca] + lucromaior
                                    npc = BDP.spprecoacouguec[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.spqtdeprodutoacougue[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.spqtdeprodutoacougue[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${}'.format(BDP.spqtdeprodutoacougue[busca1],
                                                                              busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.spqtdeprodutoacougue[busca1] -= BDP.spqtdeprodutoacougue[busca1]
                                    sleep(2)

                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função açougueiro.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um Caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        spdepositoacougue()
        break


def spvendapadaria():
    while True:
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        lucromaior = BDP.levelhabi['lvhl'] * 2
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        spvp2 = BDP.spqtdemoveispadaria['Caixa'] * 2
        spqtdevendaspadaria = qtdevendaslevel * spvp2
        if BDP.spqtdemoveispadaria['Caixa'] >= 1:
            if BDP.spqtdefuncoespadaria['Fcaixa'] >= 1:
                if BDP.spqtdefuncoespadaria['Fpadeiro'] >= spqtdevendaspadaria:
                    if sorteio == 0:
                        for item in BDP.spqtdeprodutopadaria:
                            if BDP.spqtdeprodutopadaria[item] >= 1:
                                busca = BDP.spprodutospadaria.index(item)
                                busca1 = BDP.spprodutospadaria[busca]
                                bv = BDP.spprodutovendaspadaria[busca]
                                if BDP.spqtdeprodutopadaria[busca1] >= 1:
                                    BDP.spqtdeprodutopadaria[busca1] -= spqtdevendaspadaria
                                    BDP.spqtdeprovendaspadaria[bv] += spqtdevendaspadaria
                                    BDP.dinheiro += (BDP.spprecopadariav[busca] + lucromaior) * spqtdevendaspadaria
                                    precov = (BDP.spprecopadariav[busca] + lucromaior) * spqtdevendaspadaria
                                    npv = BDP.spprecopadariav[busca] + lucromaior
                                    npc = BDP.spprecopadariac[busca] - precoreduzido
                                    lucro = (npv - npc) * spqtdevendaspadaria
                                    somaexp = (25 + BDP.maisexp) * spqtdevendaspadaria
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${}'.format(spqtdevendaspadaria, busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.spqtdeprovendaspadaria[bv] += BDP.spqtdeprodutopadaria[busca1]
                                    BDP.dinheiro += ((BDP.spprecopadariav[busca] + lucromaior) *
                                                     BDP.spqtdeprodutopadaria[busca1])
                                    precov = ((BDP.spprecopadariav[busca] + lucromaior) *
                                              BDP.spqtdeprodutopadaria[busca1])
                                    npv = BDP.spprecopadariav[busca] + lucromaior
                                    npc = BDP.spprecopadariac[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.spqtdeprodutopadaria[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.spqtdeprodutopadaria[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${}'.format(BDP.spqtdeprodutopadaria[busca1],
                                                                              busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.spqtdeprodutopadaria[busca1] -= BDP.spqtdeprodutopadaria[busca1]
                                    sleep(2)
                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função padeiro.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um Caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        spdepositopadaria()
        break


def spvendaeletronica():
    while True:
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        lucromaior = BDP.levelhabi['lvhl'] * 2
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        spve2 = BDP.spqtdemoveiseletronica['Caixa'] * 2
        spqtdevendaseletronica = qtdevendaslevel * spve2
        if BDP.spqtdemoveiseletronica['Caixa'] >= 1:
            if BDP.spqtdefuncoeseletronica['Fcaixa'] >= 1:
                if BDP.spqtdefuncoeseletronica['Fatendente'] >= 1:
                    if sorteio == 0:
                        for item in BDP.spqtdeprodutoeletronica:
                            if BDP.spqtdeprodutoeletronica[item] >= 1:
                                busca = BDP.spprodutoseletronica.index(item)
                                busca1 = BDP.spprodutoseletronica[busca]
                                bv = BDP.spprodutovendaseletronica[busca]
                                if BDP.spqtdeprodutoeletronica[busca1] >= spqtdevendaseletronica:
                                    BDP.spqtdeprodutoeletronica[busca1] -= spqtdevendaseletronica
                                    BDP.spqtdeprovendaseletronica[bv] += spqtdevendaseletronica
                                    BDP.dinheiro += ((BDP.spprecoeletronicav[busca] + lucromaior) *
                                                     spqtdevendaseletronica)
                                    precov = (BDP.spprecoeletronicav[busca] + lucromaior) * spqtdevendaseletronica
                                    npv = BDP.spprecoeletronicav[busca] + lucromaior
                                    npc = BDP.spprecoeletronicac[busca] - precoreduzido
                                    lucro = (npv - npc) * spqtdevendaseletronica
                                    somaexp = (25 + BDP.maisexp) * spqtdevendaseletronica
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${}'.format(spqtdevendaseletronica, busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.spqtdeprovendaseletronica[bv] += BDP.spqtdeprodutoeletronica[busca1]
                                    BDP.dinheiro += ((BDP.spprecoeletronicav[busca] + lucromaior) *
                                                     BDP.spqtdeprodutoeletronica[busca1])
                                    precov = ((BDP.spprecoeletronicav[busca] + lucromaior) *
                                              BDP.spqtdeprodutoeletronica[busca1])
                                    npv = BDP.spprecoeletronicav[busca] + lucromaior
                                    npc = BDP.spprecoeletronicac[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.spqtdeprodutoeletronica[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.spqtdeprodutoeletronica[busca1]
                                    BDP.nivel['qtdeexp'] += somaexp
                                    print('Voce vendeu {} {} por R${}'.format(BDP.spqtdeprodutoeletronica[busca1],
                                                                              busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.spqtdeprodutoeletronica[busca1] -= BDP.spqtdeprodutoeletronica[busca1]
                                    sleep(2)

                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função atendente.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        spdepositoeletronico()
        break


def spvendasupermercado():
    while True:
        qtdevendaslevel = BDP.levelhabi['lvhv'] * 1
        lucromaior = BDP.levelhabi['lvhl'] * 2
        precoreduzido = BDP.levelhabi['lvhp'] * 0.50
        sorteiovenda = [0, 1]
        sorteio = choice(sorteiovenda)
        spvs2 = BDP.spqtdemoveissupermercado['Caixa'] * 2
        spqtdevendassupermercado = qtdevendaslevel * spvs2
        if BDP.spqtdemoveissupermercado['Caixa'] >= 1:
            if BDP.spqtdefuncoessupermercado['Fcaixa'] >= 1:
                if BDP.spqtdefuncoessupermercado['Frepositor'] >= 1:
                    if sorteio == 0:
                        for item in BDP.spqtdeprodutosm:
                            if BDP.spqtdeprodutosm[item] >= 1:
                                busca = BDP.spprodutossm.index(item)
                                busca1 = BDP.spprodutossm[busca]
                                bv = BDP.spprodutovendasm[busca]
                                if BDP.spqtdeprodutosm[busca1] >= spqtdevendassupermercado:
                                    BDP.spqtdeprodutosm[busca1] -= spqtdevendassupermercado
                                    BDP.spqtdeprovendasupermercado[bv] += spqtdevendassupermercado
                                    BDP.dinheiro += (BDP.spprecovendasm[busca] + lucromaior) * spqtdevendassupermercado
                                    precov = (BDP.spprecovendasm[busca] + lucromaior) * spqtdevendassupermercado
                                    npv = BDP.spprecocomprasm[busca] + lucromaior
                                    npc = BDP.spprecovendasm[busca] - precoreduzido
                                    lucro = (npv - npc) * spqtdevendassupermercado
                                    somaexp = (25 + BDP.maisexp) * spqtdevendassupermercado
                                    BDP.nivel['qtdeexp'] += spqtdevendassupermercado
                                    print('Voce vendeu {} {} por R${}'.format(spqtdevendassupermercado, busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    sleep(2)
                                else:
                                    BDP.spqtdeprovendasupermercado[bv] += BDP.spqtdeprodutosm[busca1]
                                    BDP.dinheiro += ((BDP.spprecovendasm[busca] + lucromaior) *
                                                     BDP.spqtdeprodutosm[busca1])
                                    precov = ((BDP.spprecovendasm[busca] + lucromaior) *
                                              BDP.spqtdeprodutosm[busca1])
                                    npv = BDP.spprecocomprasm[busca] + lucromaior
                                    npc = BDP.spprecovendasm[busca] - precoreduzido
                                    lucro = (npv - npc) * BDP.spqtdeprodutosm[busca1]
                                    somaexp = (25 + BDP.maisexp) * BDP.spqtdeprodutosm[busca1]
                                    BDP.nivel['qtdeexp'] += BDP.spqtdeprodutosm[busca1]
                                    print('Voce vendeu {} {} por R${}'.format(
                                        BDP.spqtdeprodutosm[busca1], busca1, precov))
                                    print('voce teve um lucro de R${:.2f}'.format(lucro))
                                    print('Voce ganhou {} exp'.format(somaexp))
                                    BDP.spqtdeprodutosm[busca1] -= BDP.spqtdeprodutosm[busca1]
                                    sleep(2)

                else:
                    print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função repositor.')
                    print('Vá contratar um para fazer vendas.')
                    sleep(2)
            else:
                print('\033[33mErro: \033[mVoce não tem um(a) funcionário(a) com a função caixa.')
                print('Vá contratar um para fazer vendas.')
                sleep(2)
        else:
            print('\033[33mErro: \033[mVoce não tem um caixa.')
            print('Vá para a loja de móveis.')
            sleep(1)
        spdepositosupermercado()
        break


JogoInicio()

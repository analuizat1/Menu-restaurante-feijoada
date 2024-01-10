print('Olá! Bem-vindo(a) ao Restaurante puro sabor!')
def volumeFeijoada(): #função do volume da feijoada
    while True:
        volume = float(input('Qual a quantidade que você deseja?(ml) '))
        if 300 <= volume <= 5000:
            return volume * 0.08
        else:
            print('Só aceitamos porções menores de 300ml ou maiores que 5l. Digite outro valor.')
        continue
        break

def opcaofeijoada(): #função das opções de feijoada
    print('           Menu Opção de Feijoada          \nb - Básica (feijão + paiol + costelinha)\np - Premium (feijão + paiol + costelinha + partes de porco)\ns - Suprema (feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)')

    while True:
        try:
            opc = str(input('Qual a opção você deseja?'))
            if opc == 'b':
                return 1.00
            elif opc == 'p':
                return 1.25
            elif opc == 's':
                return 1.50
            else:
                print('Opção inválida. Digite novamente:')
                continue
        except ValueError:
            print('Operação inválida. Digite novamente:')
def acompanhamentoFeijoada (): #função do acompanhamento da feijoada
    print('           Menu acompanhamento         \n0 - não desejo mais acompanhamentos (encerrar pedido)\n1- 200g de arroz\n2- 150g de farofa especial\n3- 100g de couve cozida\n4- Uma laranja descascada\n')
    while True:
        try:
            adicional = int(input('Deseja algo mais?'))
            if adicional == 1:
                return 5.00
            elif adicional == 2:
                return 6.00
            elif adicional == 3:
                return 7.00
            elif adicional == 4:
                return 3.00
            elif adicional == 0:
                break
            else:
                print('Operação inválida. Tente novamente!')
                continue
        except ValueError:
            print('Operação inválida. Tente novamente!')


print('*~~~ Bem-vindo a feijoada da Ana Luíza! ~~~*\n') #identificador do restaurante 

vemvolume = volumeFeijoada()
vemopcao = opcaofeijoada()
vemacompanhamento = acompanhamentoFeijoada()
vemacompanhamento = acompanhamentoFeijoada()
total = (vemvolume * vemopcao) + vemacompanhamento + vemacompanhamento
print('O valor total foi de R$ {}.'.format(total)) #preço total calculado

'''
2) Escreva um programa que verifique, em uma string, a existência da letra 'a', seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
'''

# RESOLUÇÃO

print('''
        ===========================================
        ==                                       ==
        ==              TESTE 02                 ==
        ==                                       ==
        == Programa identifica a lera 'a' e      == 
        == indica a qtd de vezes que aparece.    ==
        ===========================================
      '''
)

palavra = 1

while (palavra != 0):
    palavra = input('Digite uma palavra (ou fim para terminar): ')   
    if palavra == 'fim':
        print('\nPrograma encerrado.')
        break

    letra_procurada = input('Digite uma letra para procurar: ')

    cont = 0
    for letra in palavra.lower():
        if letra == letra_procurada.lower():
            cont += 1

    print(f'\nA letra "{letra_procurada.lower()}" aparece {cont} vezes na palavra {palavra}\n\n')
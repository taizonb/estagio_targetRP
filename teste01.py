'''
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

# RESOLUÇÃO:

print('''
        ==========================================
        ==                                      ==
        ==              TESTE 01                ==
        ==                                      ==
        == Programa que calcula a sequência de  == 
        == Fibonacci até um número definido.    ==
        ==========================================
      '''
)

numero = 1
while (numero != 0):
    try:
        numero = int(input('Digite um número inteiro positivo para o fim da Sequência de Fibonacci, ou 0 para sair do programa: '))
        if numero == 0:
            print('Fim do programa.')
            break
        if numero < 0:
            print('Número digitado não é um inteiro. Tente novamente.\n')
            continue

    except:
        print('Número digitado não é um inteiro positivo. Tente novamente.\n')
        continue
    

    # Contagem dos números
    num_list = [0, 1]
    num_atual = 1

    while (num_list[-1] < numero):
        if (num_list[-1] == 1):
            num_atual = 2
            num_list.append(num_atual)  
        else:
            num_atual = num_list[-1] + num_list[-2]
            if num_atual > numero:
                break
            else:
                num_list.append(num_atual)               
    print(num_list, end='\n\n')

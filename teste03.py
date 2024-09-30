'''
3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Ao final do processamento, qual será o valor da variável SOMA?
'''

# RESPOSTA
'''Valor da Variável SOMA = 77.

Valores da iteração:
2 / 5 / 9 / 14 / 20 / 27 / 35 / 44 / 54 / 65 / 77
'''

# RESOLUÇÃO

print('''
        ==========================================
        ==                                      ==
        ==              TESTE 03                ==
        ==                                      ==
        ==========================================
      '''
)

indice = 12
soma = 0
k = 1

while k < indice:
    k += 1
    soma = soma + k
    print(soma, end='')
    print(' / ', end='')



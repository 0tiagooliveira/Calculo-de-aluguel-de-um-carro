# Calculo-de-aluguel-de-um-carro
Este é um código em Python que solicita ao usuário a quantidade de dias que um carro foi alugado e a quantidade de quilômetros rodados, calcula o valor total a ser pago e imprime o resultado formatado. 

Aqui está uma explicação linha a linha:

dias = float(input('Quantos dias alugados? '))
Esta linha pede ao usuário para digitar o número de dias que o carro foi alugado. A função input() é usada para solicitar a entrada do usuário, e a função float() é usada para converter a entrada em um número de ponto flutuante (float).

kmrodados = float(input('Quantos KM rodados? '))
Esta linha pede ao usuário para digitar o número de quilômetros rodados pelo carro alugado. Novamente, a função input() é usada para solicitar a entrada do usuário, e a função float() é usada para converter a entrada em um número de ponto flutuante (float).

valorapagar = (dias * 60) + (kmrodados * 0.15)
Esta linha calcula o valor total a ser pago pelo aluguel do carro. O custo é de R$ 60 por dia e R$ 0,15 por quilômetro rodado. O número de dias é multiplicado por 60 e o número de quilômetros rodados é multiplicado por 0,15. Em seguida, os dois resultados são adicionados para obter o valor total a ser pago.

print('O total a pagar é de R$ {:.2f}'.format(valorapagar))
Esta linha imprime o valor total a ser pago formatado. A expressão '{:.2f}' é usada para formatar o valor como um número de ponto flutuante com duas casas decimais. A função format() é usada para inserir o valor da variável valorapagar na string formatada. O resultado é uma string que exibe o valor total a ser pago, com o símbolo de moeda R$ e duas casas decimais.

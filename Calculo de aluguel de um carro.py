dias = float(input('Quantos dias alugados? '))
kmrodados = float(input('Quantos KM rodados? '))
valorapagar = (dias * 60) + (kmrodados * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(valorapagar))

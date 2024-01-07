'''exercício imc'''

nome = 'FELIPE LIMA DE MIRANDA PARDAUIL'
altura_metros = 1.75
peso_kg = 87
imc = peso_kg / (altura_metros**2) # // fornece o valor mais exato

'''formatação de str = f-strings'''
linha1 = f'{nome} tem {altura_metros:,.2f} de altura'
linha2 = f'pesa {peso_kg} kg e o imc é {imc:.2f}'

print(linha1)
print(linha2)

# print('Peso:', peso_kg, 'kg')
# print('IMC:', imc)


# Ellipsis = place holder (pode ser utilizado para protótipos no código)
# a = input('Informe um número: ')
# print(f'o valor informado foi {a}')

a = input("informe um valor: ")
b = input("informe outro valor: ")

int_input_a = int(a)
int_input_b = int(b)

print(f"a soma dos valores é {int_input_a+int_input_b}")
print(type(a), type(b))
print(type(int_input_a), type(int_input_b))

'''A função input sempre gera uma 
variável do tipo string (str)'''
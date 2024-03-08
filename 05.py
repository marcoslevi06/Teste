
teste = 'ABCDE'
print(teste[4], len(teste))

palavra = input('Insira a palavra que desja inverter: ').replace(' ', '')

# Forma 1 usando fatiamento de strings.
nova_palavra = palavra[::-1].title()

print(f'\nNova palavra = {nova_palavra}')


# Forma 02
palavra_invertida = ''

for i in range(len(palavra) -1, -1, -1):
    palavra_invertida += palavra[i]

print(f'Palavra invertida = {palavra_invertida}')



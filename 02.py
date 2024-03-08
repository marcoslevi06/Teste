
numero = int(input('Digite um número qualquer: '))
numero_final = int(input('Informe até qual número a sequência de FIbonacci deva ser calculada: '))


penultimo = 0
ultimo = 1

atual = 0

lista_numeros = list()

while atual <= numero_final:
    
    print(f'{atual}')
    lista_numeros.append(atual)

    atual = penultimo + ultimo 
    
    penultimo = ultimo
    ultimo = atual

print(f'FIM do Loop.')
valor = f'Sim, o número {numero} faz parte da sequência gerada.' if numero in lista_numeros else f'O número {numero} não faz parte da sequência gerada.'

print(f'\nR = {valor}')
# Capicuas
# Palindromos

# Solicitar al usuario que ingrese por teclado un texto le vamos a indicar si lo ingresado es o no un palindromo

print('\tIdentificador de palindromos')

texto = input('Ingrese una frase por favor: ')
textoInv = texto[::-1]

if texto == textoInv:
    print('La palabra ingresada '+ texto + ' es un palindromo')

elif texto.lower() == textoInv.lower():
    print('Ingresaste un palindromo pero ignorando las mayusculas')

elif texto.replace(' ','') == textoInv.replace(' ',''):
    print('Palindromo ignorando los espacios')    

elif texto.lower().replace(' ', '') == textoInv.lower().replace(' ',''):
    print('Palindromo ignorando las mayúsculas y los espacios')    

else:
    print('La palabra ingresada ' + texto + ' no es un palindromo')    
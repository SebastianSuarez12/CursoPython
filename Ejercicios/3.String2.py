#Ejercicio 3
# Validar si los siguientes enlaces son correctos
#https:// y terminar con .com

link1 = 'https://www.epn.edu.ec.ecuador'
link2 = 'https://modemat.com'
link3 = 'https://fis.edu.lat'

print('El link 1 empieza con https:// ->' ,link1.startswith('https://'),'y termina con -> .com' ,link1.endswith('.com'))
print('El link 2 empieza con https:// ->' ,link2.startswith('https://'),'y termina con -> .com' ,link2.endswith('.com'))
print('El link 3 empieza con https:// ->' ,link3.startswith('https://'),'y termina con -> .com' ,link3.endswith('.com'))

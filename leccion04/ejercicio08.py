# Saber cual nro es mayor entre dos numeros
# introducidos por el usuario

print('Bienvenido alprograma para saber si un numero es mayor que otro numero');
nro1 = int(input('Introduzca el primer numero: '));
nro2 = int(input('Introduzca el segundo numero: '));

if ( nro1 > nro2 ):
  print(f'El numero {nro1} es mayor');
elif ( nro1 < nro2 ):
  print(f'El numero {nro2} es mayor');
else:
  print(f'El numero {nro1} y el numero {nro2} son iguales');

print('Fin de programa');
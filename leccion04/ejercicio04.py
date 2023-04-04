# Programa para saber si un numero esta entre 0 y 5
rangoIzquierda = 0;
rangoDerecha = 5;
print(f'Programa para saber si un numero esta entre {rangoIzquierda} y {rangoDerecha}. "limites incluyentes"');
numero = int(input('Proporcione un numero para evaluar: '));

if ( rangoIzquierda <= numero <= rangoDerecha  ):
  print('Su numero esta dentro del rango');
else:
  print('Su numero esta fuera del rango');

print('Fin de programa');
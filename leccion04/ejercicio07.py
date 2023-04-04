edad = int(input('Introduzca su edad: '));

veintes = 20 <= edad < 30;
treintas = 30 <= edad <40;
if ( veintes ):
  print("usted se encuentra entre los 20's");
elif ( treintas ):
  print("usted se encuentra entre los 30's");
else:
  print("Usted no pertenece a los rangos de 20's y 30's");

print('Fin de programa');
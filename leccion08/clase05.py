# Numero de argumentos sin definir;

# *nombres se convertira en una TUPLA
def listarNombres(*nombres):
  for nombre in nombres:
    print(nombre);
  return;

listarNombres('Juan', 'Karla', 'María', 'Ernesto');
listarNombres('Laura', 'Carlos');
print('Proporcione los siguientes datos del libro:');
nombreLibro = input('Proporciona el nombre: ');
idLibro = int(input('Proporciona el ID: '));
precioLibro = float(input('Proporciona el precio: '));
envioLibro = input('Indica si el libro es gratuito ( True/False ): ');

if ( envioLibro == 'True' ):
  envioLibro = True;
elif ( envioLibro == 'False' ):
  envioLibro = False;
else:
  precioLibro('Ha proporcionado un valor incorrecto');

print(f'''Datos del lirbo introducido: 
  Nombre: {nombreLibro}
  ID: {idLibro}
  Precio: {precioLibro}
  Envio Gratuito: {envioLibro}
''');
print('Fin de programa...');
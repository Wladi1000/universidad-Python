# Funcion input para procesar la entrada del usuario
numero1 = input('Escribe el primer numero: ');
numero2 = input('Escribe el segundo numero: ');
#como input devuelve STR hay que truncar para hacer operaciones matematicas
resultadoSTR = numero1 + numero2;
resultado = int(numero1) + int(numero2);
print('Concatenacion:', resultadoSTR);
print('Suma:', resultado);

# ----------------------------
numero1 = int(input('Escribe el primer numero: '));
numero2 = int(input('Escribe el segundo numero: '));
resultado = numero1 + numero2;
print(resultado);
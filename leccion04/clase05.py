# Operadores Logicos
# and
# or
# not

a = True;
b = True;

resultado = a and b; # 1 ^ 1
print( resultado );
resultado = a or b; # 1 or 1
print( resultado );
resultado = not(a) and b; # 0 ^ 1
print( resultado );

a = False;
b = True;

resultado = a and b; # 0 ^ 1
print( resultado );
resultado = a or b; # 0 or 1
print( resultado );
resultado = not(a) and b; # 1 ^ 1
print( resultado );

a = False;
b = False;

resultado = a and b; # 0 ^ 0
print( resultado );
resultado = a or b; # 0 or 0
print( resultado );
resultado = not(a) and b; # 1 ^ 0
print( resultado );
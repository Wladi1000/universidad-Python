# for i in range(6):
#   if i % 2 == 0:
#     print(f'Valor: {i}')

for i in range(6):
  if i % 2 != 0:
    continue; #salta a la siguiente iteracion
  print(f'Valor: {i}');
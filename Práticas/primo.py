a = int(input('Digite um número: '))

div = 0

for x in range(1, a+1):
  resto = a % x
  if resto == 0:
    div = div + 1 
    #div += 1
    
if div == 2:
  print('número {} é primo'.format(a))
else:
  print('número {} não é primo'.format(a))

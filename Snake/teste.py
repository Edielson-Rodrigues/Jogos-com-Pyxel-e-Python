'''def multiplos_valores():
  x = 10
  y = 15
  return x, y
  
a, b = multiplos_valores()
print(a) # 10
print(b) # 15'''

'''lista1 = [0, 9, 8, 7]
x = 0
listaStr = ''

for i in range(len(lista1)):
    listaStr += str(lista1[i])

listaDefinitiva = []

for i in range(4):
    listaDefinitiva.append(int(listaStr[i]))


y = 'ola'
listaDefinitiva.append(y)

print(listaDefinitiva[4])'''

'''placar = ['0088', '80168', '0888', '8888', '16088', '16888', '24088', '24888', '32088', '32888']
cont = 0 

novo = []

val = placar[9]'''
'''t = val[0] + val[1]
if val[0] + val[3] == '00':
  print('opa')
print(t)
condicao = True'''

'''for i in range(len(val)):
  if i <= len(val)-2:
    if val[i] + val[i+1] == '16' or val[i] + val[i+1] == '24' or val[i] + val[i+1] == '32':
      x = val[i] + val[i+1]
      novo.append(int(x))

  if val[i] == '0' or val[i] == '8':
    novo.append(int(val[i]))

for j in range(len(novo)):
  print(novo[j])'''

contadorPlacar = 1
posicoes = [[0, 0, 8, 8], '80168', '0888', '8888', '16088', '16888', '24088', '24888', '32088', '32888']
atual = posicoes[0]
print(atual[3])

'''val = posicoes[contadorPlacar]

if contadorPlacar == 0:
  val = posicoes[contadorPlacar]

  for i in range(len(val)):
    if i < len(val)-1:
      if val[i] + val[i+1] == '16' or val[i] + val[i+1] == '24' or val[i] + val[i+1] == '32':
        junto = val[i] + val[i+1]
        atual.append(int(junto))

    if val[i] == '0' or val[i] == '8':
      atual.append(int(val[i]))

'''


import numpy as np

def maxPos(vetor):
    aux = vetor[0]
    for i in range(len(vetor)):
        if (vetor[i] >= aux).all():
            if (vetor[i] >= 0):
                aux = vetor[i]
                pos = i
    if (aux > 0): return pos+1
    else: return None

def minPos(vetor):
    aux = vetor[0]
    for i in range(len(vetor)):
        if (vetor[i] <= aux).all():
            if (vetor[i] >= 0):
                aux = vetor[i]
                pos = i
    if (aux >= 0): return pos+1
    else: return None

def minNeg(vetor):
    aux = 0
    for i in range(len(vetor)):
        if (vetor[i] < aux).all():
            aux = vetor[i]
            pos = i
    if (aux < 0): return pos+1
    else: return None

def simplex(z = None, lhc = None, rhc = None, obj = 'max'):
  z = -z
  lenz = len(z)
  lenlhc = len(lhc)
  l = lenlhc+1
  c = lenz+lenlhc+1
  i = np.identity(lenlhc)
  aux = np.zeros(c*l).reshape(l,c)
  aux[:1, 0:lenz] = z
  aux[1:, 0:lenz] = lhc[:]
  aux[1:, lenz:c-1] = i
  aux[1:, c-1] = rhc
  itr = 1
  entra = np.empty(l, dtype=object)
  entra[0] = 'Z'
  for i in range(1,l):
      entra[i] = 'S' + str(i)
  print("-----------------------------------------------------------")
  print("Tabela %d:"%(itr))
  print(aux)

  if obj == 'max':
      while(minNeg(aux[:1, 0:lenz][0]) != None):
          itr = itr + 1
          col = minNeg(aux[:1, 0:lenz][0])
          print("Entra na base: X%d"%(col))
          rm = aux[1:, c-1]/aux[1:, col-1]
          lin = minPos(rm)
          entra[lin] = 'X'+str(col)
          print("Sai da base: S%d"%(lin))
          pivo = aux[lin][col-1]
          print("pivo", pivo)
          aux[lin,:] = aux[lin,:]/pivo

          for i in range(l):
              pivolinha = aux[i][col-1]
              for j in range(c):
                  if i != lin:
                    aux[i][j] = aux[i][j] - pivolinha*aux[lin][j]
          print("-----------------------------------------------------------")
          print("Tabela %d:"%(itr))
          print(aux)

  if obj == 'min':
      while(maxPos(aux[:1, 0:lenz][0]) != None):
          itr = itr + 1
          col = maxPos(aux[:1, 0:lenz][0])
          print("Entra na base: X%d"%(col))
          rm = aux[1:, c-1]/aux[1:, col-1]
          lin = minPos(rm)
          entra[lin] = 'X'+str(col)
          print("Sai da base: S%d"%(lin))
          pivo = aux[lin][col-1]
          print("pivo", pivo)
          aux[lin,:] = aux[lin,:]/pivo

          for i in range(l):
              pivolinha = aux[i][col-1]
              for j in range(c):
                  if i != lin:
                    aux[i][j] = aux[i][j] - pivolinha*aux[lin][j]
          print("-----------------------------------------------------------")
          print("Tabela %d:"%(itr))
          print(aux)

  print("\n+---------------+")
  print('|Solução:'+ '\t|')
  for i in range(l):
      print('|' + str(entra[i]) + ' = ' + str(aux[i][c-1]) + '\t|')
  print("+---------------+")


def main():
  #simplex function parameters
  #  z = objective function
  #lhc = left hand constraint
  #rhc = right hand constraint
  #obj = objective -> maximize = 'max' | minimize = 'min'
  z = np.array([5, -4, 6, -8])
  lhc = np.array([[1,  2, 2,  4],
                  [2, -1, 1,  2],
                  [4, -2, 1, -1]])

  rhc = np.array([40, 8, 10])
  simplex(z = z, lhc = lhc, rhc = rhc, obj='min')

if __name__ == '__main__':
    main()

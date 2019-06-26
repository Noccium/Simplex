import numpy as np

def minPos(vetor):
    aux = vetor[0]
    for i in range(len(vetor)):
        if (vetor[i] <= aux).all():
            aux = vetor[i]
            print('vetor', vetor[i])
            pos = i
            print('pos', pos)
    if (aux >= 0): return (aux, pos+1)
    else: return None

def minNeg(vetor):
    aux = 0
    for i in range(len(vetor)):
        if (vetor[i] < aux).all():
            aux = vetor[i]
            pos = i
    if (aux < 0): return (aux, pos)
    else: return None

def simplex(z = None, lhc = None, rhc = None):
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
  print(aux)

  while(minNeg(aux[:1, 0:lenz][0]) != None):
    element, col = minNeg(aux[:1, 0:lenz][0])
    rm = aux[1:, col-1]/aux[1:, c-1]
    pivo, lin = minPos(rm)
    aux[lin:,:] = aux[lin:,0:]/pivo
    aux[:lin,:] = aux[:lin,:] - aux[:lin,col]*aux[lin:,:]
    aux[lin:,:] = aux[lin:,:] - aux[lin:,col]*aux[lin:,:]

def main():
  z = np.array([1, 1, 3, 2, 5])
  lhc = np.array([[1, 2, 0, 3, 4],
                  [2, 2, 3, 0, 4],
                  [3, 2, 3, 0, 4],
                  [4, 2, 3, 0, 4]])

  rhc = np.array([1, 2, 3, 4])
  simplex(z = z, lhc = lhc, rhc = rhc)

if __name__ == '__main__':
    main()

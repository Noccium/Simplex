import numpy as np 

def simplex(z, lhc, rhc):
  z = -z
  aux = np.zeros(len(z)*len(z)).reshape(len(z))
  print(aux)

def main():
  z = np.array([1, 1, 3, 2])
  simplex(z=z)

main()

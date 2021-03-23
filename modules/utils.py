from random import randrange

def remove_all(l, x):
  '''
  removes all occurence of x in the list l
  '''
  while x in l : l.remove(x)

def count_occurences(l,x):
  '''
  returns the number of occurences of x in the list l
  '''
  cpt = 0
  for n in l : 
    if n == x : cpt = cpt+1
  return cpt

#TD3

def random_int_list(size,bound):
  '''
  returns a random list of integers
  '''
  return [int(randrange(0,bound)) for _ in range(0,size)]

def random_int_matrix(size, bound, null_diag=True, symetric=False, oriented=False):
  '''
  returns a random integer matrix with selected attributes
  '''
  if symetric : return random_symetric_int_matrix(size, bound, null_diag)
  if oriented : return random_oriented_int_matrix(size, bound, null_diag)

  res = [random_int_list(size, bound) for _ in range(0, size)]
  if null_diag : 
    for i in range(0,size): res[i][i] = 0
  return res

def random_symetric_int_matrix(size, bound, null_diag=True):
  '''
  returns a random integer symetric matrix
  '''
  res = random_int_matrix(size, bound, null_diag)
  for i in range(size):
    for j in range(i):
      res[i][j]=res[j][i]
  return res

def random_oriented_int_matrix(size, bound, null_diag=True):
  '''
  returns a random integer oriented matrix
  '''
  res = random_int_matrix(size, 20, null_diag)
  for i in range(size):
    for j in range(i):
      if res[i][j] != 0 and res[j][i] != 0 :
        if res[i][j] > res[j][i] : 
          res[i][j] = int(randrange(0,bound))
          res[j][i] = 0
        else :
          res[j][i] = int(randrange(0,bound))
          res[i][j] = 0
  return res

def random_triangular_int_matrix(size, bound, null_diag=True):
  '''
  returns a random integer (upper) triangular matrix
  '''
  res = random_int_matrix(size, bound, null_diag)
  for i in range(size):
    for j in range(i):
      res[i][j] = 0
  return res

def invert_permutation(l):
  res = [0 for _ in l]
  for i in range(len(l)):
    res[l[i]] = i
  return res

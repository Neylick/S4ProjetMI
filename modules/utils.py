from random import randrange

def remove_all(l, x):
  while x in l : l.remove(x)

def count_occurences(l,x):
  cpt = 0
  for n in l : 
    if n == x : cpt = cpt+1
  return cpt

def random_int_list(size,bound):
  return [int(randrange(0,bound)) for _ in range(0,size)]

def random_int_matrix(size, bound, null_diag=True, symetric=False, oriented=False):
  if symetric : return random_symetric_int_matrix(size, bound, null_diag)
  if oriented : return random_oriented_int_matrix(size, bound, null_diag)

  res = [random_int_list(size, bound) for _ in range(0, size)]
  if null_diag : 
    for i in range(0,size): res[i][i] = 0
  return res

def random_symetric_int_matrix(size, bound, null_diag=True):
  res = random_int_matrix(size, bound, null_diag)
  for i in range(0,size):
    for j in range(0,i):
      res[i][j]=res[j][i]
  return res

def random_oriented_int_matrix(size, bound, null_diag=True):
  res = random_int_matrix(size, bound, null_diag)
  for i in range(0,size):
    for j in range(0,i):
      if res[i][j] != 0 and res[j][i] != 0 :
        if res[i][j] > res[j][i] : 
          res[i][j] = int(randrange(0,bound))
          res[j][i] = 0
        else :
          res[j][i] = int(randrange(0,bound))
          res[i][j] = 0
  return res

def random_triangular_int_matrix(size, bound, null_diag=True):
  res = random_int_matrix(size, bound, null_diag)
  for i in range(0,size):
    for j in range(1,i):
      res[i][size-j] = 0
  return res


'''LATER:
def random_matrix(size, bound, null_diag=True, \
                  symetric=False, oriented=False, triangular=False):
'''
def remove_all(l, x):
  while x in l : l.remove(x)

def count_occurences(l,x):
  cpt = 0
  for n in l : 
    if n == x : cpt = cpt+1
  return cpt
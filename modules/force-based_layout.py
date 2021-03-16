from modules.digraph_graphics import *
import math


def distance(vertex1,vertex2):
  return math.sqrt( (vertex1.x-vertex2.x)**2 + (vertex1.y - vertex2.y)**2)

def force_based_layout(g, nb_iter=50, animation_file=None):
  '''doc : todo'''
  L = 100
  k = 1
  Q = 1
  dt = 1
  max_speed = 1000
  pos = random_layout(g)
  speed = {i:vertex(0,0) for i in g.get_nodes_ids()}
  def spring_force(id1, id2):
    pass
  def repulsive_force(id1, id2):
    pass
  
  for it in range(nb_iter):
    pass  
    
  return pos

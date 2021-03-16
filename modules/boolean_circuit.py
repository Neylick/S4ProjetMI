from modules.open_digraph import *

class bool_circ(open_digraph):
  def __init__(self, g):
    self.inputs = g.inputs
    self.outputs = g.outputs
    self.nodes = g.nodes
    
    if not self.is_well_formed() : raise TypeError("The given open_digraph cannot be converted to a boolean circuit.")

  def to_od(self):
    return open_digraph(self.inputs, self.outputs, self.nodes)
  
  def is_well_formed(self):
    if not self.is_cyclic() : return False

    for n in self.get_nodes() :
      if (n.get_label() == '&') or (n.get_label() == '|'):
        if (n.outdegree() is not 1) : return False
      elif (n.get_label == '~') :
        if (n.indegree() is not 1) or (n.outdegree() is not 1) : return False
      else : 
        if (n.indegree() is not 1) : return False
    return True
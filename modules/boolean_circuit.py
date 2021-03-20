from modules.open_digraph import *

class bool_circ(open_digraph):
  def __init__(self, g):
    '''
    initialises the boolean circuit from an open_digraph object.
    raises a TypeError if the given open_digraph is not compatible with the boolean circuit type (not well formed)
    '''
    self.inputs = g.inputs
    self.outputs = g.outputs
    self.nodes = g.nodes

    if not self.is_well_formed() : raise TypeError("The given open_digraph cannot be converted to a boolean circuit.")

  def to_od(self):
    '''
    returns the selected boolean circuit as an open digraph
    '''
    return open_digraph(self.inputs, self.outputs, self.nodes)
  
  def is_well_formed(self):
    '''
    tests if the boolean circuit is really a boolean circuit. \n
    label : & or | ->  1 as outdegree \n
    label : ~      ->  1 as outdegree AND 1 as indegree \n
    label : other  ->  1 as indegree
    '''
    if not self.is_cyclic() : return False

    for n in self.get_nodes() :
      if (n.get_label() == '&') or (n.get_label() == '|'):
        if (n.outdegree() is not 1) : return False
      elif (n.get_label() == '~') :
        if (n.indegree() is not 1) or (n.outdegree() is not 1) : return False
      else : 
        if (n.indegree() is not 1) : return False
    return True
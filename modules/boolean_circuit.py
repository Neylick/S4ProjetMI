import sys
sys.path.append('./../')

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
    label : empty  ->  1 as indegree
    '''
    if self.is_cyclic() : return False

    for n in self.get_nodes() :
      if (n.get_label() == ''):
        if ((n.indegree() != 1) and (n.get_id() not in self.get_input_ids())) :
          return False
      elif (n.get_label() == '&') or (n.get_label() == '|'):
        if (n.outdegree() != 1) and (n.get_id() not in self.get_output_ids()) : 
          return False
      elif (n.get_label() == '~') :
        if ((n.indegree() != 1) and (n.get_id() not in self.get_input_ids())) or ((n.outdegree() != 1) and (n.id not in self.get_output_ids())) : 
          return False
    return True

  # TD8:

  def dijkstra(self, src, direction=None):
    Q = [self.get_node_by_id(src).copy()]
    distances = dict()
    distances[src] = 0
    prev = dict()
    while len(Q) != 0:
      u = min(distances, key=lambda k : distances[k])
      Q.remove(u)
      neighbours = []
      if direction == 1 or direction == None :
        neighbours += self.get_node_by_id(u).parents
      if direction == -1 or direction == None :
        neighbours += self.get_node_by_id(u).children
      for v in neighbours :
        if v not in distances or distances[v] > distances[u] + 1 :
          if v not in distances : Q.append(v)
          distances[v] = distances[u]+1
          prev[v] = u
    return distances, prev
  
  #TP8 A FINIR IG

  #TD 9 : NEED TESTS

  #need to sort inputs
  def parse_parentheses(self, *args):
    g = open_digraph.empty()
    g.add_node('', [], [])

    current_node = g.get_node_by_id(0)
    current_str = ""

    labels_to_ids = dict()

    for expression in args :
      for char in expression:
        if char == '(':
          current_node.set_label(current_node.get_label()+current_str)
          nid = g.add_node('', [], [])
          current_node.add_parent_id(nid)

          l = current_node.get_label()
          if l not in labels_to_ids: 
            labels_to_ids[l] = current_node.get_id()
            if l != '|' and l != '&' and l != '~' : #First encounter with a variable, adding it to inputs
              g.add_input_id(current_node.get_id())

          elif l != '|' and l != '&' and l != '~' : #found a variable duplicate, merging nodes
            g.merge_nodes(current_node.get_id(), labels_to_ids[l])
            labels_to_ids[l] = current_node.get_id()

          current_node = g.get_node_by_id(nid)

          current_str = ""

        elif char == ')':
          current_node.set_label(current_node.get_label()+current_str)
          current_node = g.get_node_by_id( current_node.get_children_ids()[0] )

          current_str = ""

        else : current_str += char

      
      return bool_circ(g)
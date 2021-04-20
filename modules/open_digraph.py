import sys
sys.path.append('./../')

from modules.utils import *

'''
Node class
'''
class node:
  #TD1
  def __init__(self, identity, label, parents, children):
    '''
    identity: int; its unique id in the graph
    label: string;
    parents: int list; a sorted list containing the ids of its parents
    children: int list; a sorted list containing the ids of its children
    '''
    self.id = identity
    self.label = label
    self.parents = parents
    self.children = children
  
  def __str__(self):
    '''
    return the string corresponding to the current node
    '''
    return "(" + str(self.id) + ", '" +self.label + "', " +str(self.parents)+", "+str(self.children)+")"

  def __repr__(self):
    return "node"+str(self)

  def __eq__(self, n):
    return n.id == self.id and n.label == self.label and n.parents == self.parents and n.children == self.children

  def copy(self): 
    '''
    returns a copy of the node
    '''
    return node(self.id, self.label, self.parents.copy(), self.children.copy())

  def get_id(self): 
    '''
    returns the node's id
    '''
    return self.id 

  def get_label(self): 
    '''
    return the node's label
    '''
    return self.label
  
  def get_parent_ids(self): 
    '''
    return the node's parents
    '''
    return self.parents
  
  def get_children_ids(self): 
    '''
    return the node's children
    '''
    return self.children

  def set_id(self, _id): 
    '''
    sets the node's id
    '''
    self.id = _id

  def set_label(self, _label): 
    '''
    sets the node's label
    '''
    self.label = _label

  def set_parent_ids(self, _ids): 
    '''
    sets the node's parents
    '''
    self.parents = _ids
    self.parents.sort()
  
  def set_children_ids(self, _ids): 
    '''
    sets the node's children
    '''
    self.children = _ids
    self.children.sort()

  def add_child_id(self, _id): 
    '''
    add a node's id to the children list of the node
    '''
    self.children.append(_id)
    self.children.sort()

  def add_parent_id(self, _id): 
    '''
    add a node's id to the parents list of the node
    '''
    self.parents.append(_id)
    self.parents.sort()

  #TD2

  def remove_child_id(self, _id): 
    '''
    removes a node's id from the children list of the node
    '''
    self.children.remove(_id)

  def remove_parent_id(self, _id): 
    '''
    removes a node's id from the parents list of the node
    '''
    self.parents.remove(_id)

  def remove_child_id_all(self, _id): 
    '''
    remove all occurences of an id from the children list of the node
    '''
    remove_all(self.children, _id)

  def remove_parent_id_all(self, _id): 
    '''
    remove all occurences of an id from the parents list of the node
    '''
    remove_all(self.parents, _id)
  
  #TD6

  def indegree(self): 
    '''
    returns the number of parents of the node
    '''
    return len(self.get_parent_ids())

  def outdegree(self):
    '''
    returns the number of children of the node
    '''
    return len(self.get_children_ids())
  
  def degree(self):
    '''
    returns the total degree of the node
    '''
    return self.indegree() + self.outdegree()






'''
Open digraph class
'''

class open_digraph: # for open directed graph
  #TD1
  def __init__(self, inputs, outputs, nodes):
    '''
    inputs: int list; the ids of the input nodes
    outputs: int list; the ids of the output nodes
    nodes: node list;
    '''
    self.inputs = inputs
    self.outputs = outputs
    self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

  def __str__(self):
    '''
    return the string corresponding to the current digraph
    '''
    return "("+str(self.inputs)+", "+str(self.outputs)+", "+str(self.nodes)+")"

  def __repr__(self):
    return "graph"+str(self)

  def __eq__(self, g):
    '''
    wether or not the open_digraph g is equal to the selected open_digraph
    '''
    return self.inputs == g.inputs and self.outputs == g.outputs and self.nodes == g.nodes

  def empty():
    '''
    sets the open_digraph as an empty one
    '''
    return open_digraph([],[],{})

  def copy(self):
    '''
    returns a copy of the open_digraph
    '''
    return open_digraph(self.inputs, self.outputs, [self.nodes[k].copy() for k in self.nodes])

  def get_input_ids(self):
    '''
    returns the graph's input nodes' ids
    '''
    return self.inputs
  
  def get_output_ids(self):
    '''
    returns the graph's output nodes' ids
    '''
    return self.outputs
  
  def get_id_node_map(self):
    '''
    returns the graph's node dictionnary : matching id to nodes
    '''
    return self.nodes
  
  def get_nodes(self):
    '''
    returns a list of the graph's nodes object
    '''
    return [self.nodes[k] for k in self.nodes]
  
  def get_nodes_ids(self):
    '''
    returns a list of the graph's nodes' ids
    '''
    return [k for k in self.nodes]

  def get_node_by_id(self, _id):
    '''
    returns the node corresponding to the given id
    '''
    return self.nodes[_id]

  def get_nodes_by_ids(self, _ids):
    '''
    returns a list of node from a list of id
    '''
    return [self.nodes[k] for k in _ids]

  def set_input_ids(self, _ids):
    '''
    sets the graph's input nodes' ids
    '''
    self.inputs = _ids
  
  def set_output_ids(self, _ids):
    '''
    sets the graph's output nodes' ids
    '''
    self.outputs = _ids

  def add_input_id(self, _id):
    '''
    adds the given id to the input id list
    '''
    self.inputs.append(_id)

  def add_output_id(self, _id):
    '''
    adds the given id to the output id list
    '''
    self.outputs.append(_id)

  def new_id(self):
    '''
    returns an id that is not already in the digraph 
    '''
    if len(self.nodes) == 0 : return 0
    else : return max(self.get_nodes_ids()) + 1

  def add_edge(self, src, tgt):
    '''
    adds an edge between the given source and target nodes
    '''
    self.nodes[src].add_child_id(tgt)
    self.nodes[tgt].add_parent_id(src)
  
  def add_edges(self, srcs_and_tgts):
    '''
    adds edges defined by a list of sources and targets couples 
    '''
    for couple in srcs_and_tgts :
      self.add_edge(couple[0], couple[1])

  def add_node(self, label="", parents=[], children=[]):
    '''
    adds a node to the graph, with the given attributes
    '''
    indice = self.new_id()
    self.nodes[indice] = node(indice, label, parents, children)
    for p in parents : self.nodes[p].add_child_id(indice)
    for c in children : self.nodes[c].add_parent_id(indice)
    return indice

  #TD2

  def remove_edge(self, src, tgt):
    '''
    removes an edge between the src and target nodes
    '''
    self.nodes[src].remove_child_id(tgt)
    self.nodes[tgt].remove_parent_id(src)
    if src in self.inputs and len(self.nodes[src].get_children_ids()) == 0 :
      self.inputs.remove(src)
    if tgt in self.outputs and len(self.nodes[tgt].get_parent_ids()) == 0 :
      self.inputs.remove(src)

  def remove_node_by_id(self, _id):
    '''
    removes the nodes that has the given id from the graph
    '''
    is_out = _id in self.get_output_ids()
    is_in = _id in self.get_input_ids()
    for p in self.nodes[_id].get_parent_ids():
      self.nodes[p].remove_child_id_all(_id)
      if is_out : self.add_output_id(p)
    for c in self.nodes[_id].get_children_ids():
      self.nodes[c].remove_parent_id_all(_id)
      if is_in : self.add_input_id(c)
    return self.nodes.pop(_id)

  def is_well_formed(self):
    '''
    tests if the graph is well formed : every input & output in node list, 
    parents corresponding to children between nodes.
    '''
    for inp in self.inputs:
      if inp not in self.nodes : return False
    for out in self.outputs:
      if out not in self.nodes : return False
    for k in self.nodes:
      if self.nodes[k].id is not k : return False
      prev = -1
      for c in self.nodes[k].get_children_ids() :
        if c != prev :
          prev = c
          occ = count_occurences(self.nodes[k].get_children_ids(), c)
          if (count_occurences(self.nodes[c].get_parent_ids(), k) != occ) :
            return False
    return True

  #TD3

  def from_od(self, graph):
    '''
    basically __init__(opendigraph g), the copy constuctor
    '''
    self.inputs = graph.get_input_ids()
    self.outputs = graph.get_output_ids()
    self.nodes = graph.nodes

  def random(self, size, bound, inputs=[], outputs=[], form="free", loop_free=False):
    '''
    returns a random graph with the selected attributes 
    '''
    res = open_digraph.empty()

    if loop_free or "loop-free" in form or "loop_free" in form or "noloop" in form :
      if "DAG" in form: res = graph_from_adjacency_matrix(random_triangular_int_matrix(size,bound,True))
      elif "oriented" in form: res = graph_from_adjacency_matrix(random_oriented_int_matrix(size,bound,True))
      elif "undirected" in form: res = graph_from_adjacency_matrix(random_symetric_int_matrix(size,bound,True))
      #default case
      else : res = graph_from_adjacency_matrix(random_int_matrix(size,bound,True))
    else :
      if "DAG" in form: res = graph_from_adjacency_matrix(random_triangular_int_matrix(size,bound,False))
      elif "oriented" in form: res = graph_from_adjacency_matrix(random_oriented_int_matrix(size,bound,False))
      elif "undirected" in form: res = graph_from_adjacency_matrix(random_symetric_int_matrix(size,bound,False))
      #default case
      else : res = graph_from_adjacency_matrix(random_int_matrix(size,bound,False))
    
    res.set_input_ids(inputs)
    res.set_output_ids(outputs)

    self.from_od(res)

  def change_id(self, node_id, new_id):
    if new_id in self.get_nodes_ids():
      self.change_id(new_id, self.new_id())
    
    n = self.get_node_by_id(node_id)
    for p in n.parents :
      occ = count_occurences(p.get_children_ids(), node_id)
      p.remove_child_id_all(node_id)
      for _ in range(occ) : p.add_child_id(new_id)

    for c in n.children :
      occ = count_occurences(c.get_parents_ids(), node_id)
      c.remove_parent_id_all(node_id)
      for _ in range(occ) : p.add_parent_id(new_id)

    n = count_occurences(self.get_input_ids() ,node_id)
    remove_all(self.inputs, node_id)
    for _ in range(n) : self.add_input_id(new_id)

    n = count_occurences(self.get_output_ids() ,node_id)
    remove_all(self.outputs, node_id)
    for _ in range(n) : self.add_output_id(new_id)



  def change_ids(self, old_new_ids):
    sorted_on_ids = sorted(old_new_ids, key=lambda tab : tab[1])
    for a,b in sorted_on_ids :
      self.change_id(a,b)

  def normalise_ids(self):
    ids = self.get_nodes_ids()
    size = len(ids)
    onids = []
    for i in range(size): onids.append((ids[i],i))
    self.change_ids(onids)


  def adjacency_matrix(self):
    matrix = [[0 for _ in range(len(self.get_nodes_ids()))] for _ in range(len(self.get_nodes_ids()))]
    self.normalise_ids()
    for n in self.get_nodes():
      for nid in n.get_children_ids():
        matrix[n.get_id()][nid] += 1
    return matrix

  #TD6

  def max_indegree(self):
    '''
    returns the maximum of the nodes' input degrees
    '''
    m = 0
    for k in self.get_nodes_ids():
      ind = self.get_node_by_id(k).indegree()
      if k in self.get_input_ids() : ind+=1
      if ind > m : m = ind 
    return m

  def min_indegree(self):
    '''
    returns the minimum of the nodes' input degrees
    '''
    m = self.get_node_by_id(self.get_nodes_ids()[0]).indegree()+20
    for k in self.get_nodes_ids():
      ind = self.get_node_by_id(k).indegree()
      if k in self.get_input_ids() : ind+=1
      if ind < m : m = ind 
    return m

  def max_outdegree(self):
    '''
    returns the maximum of the nodes' output degrees
    '''
    m = 0
    for k in self.get_nodes_ids():
      ind = self.get_node_by_id(k).outdegree()
      if k in self.get_output_ids() : ind+=1
      if ind > m : m = ind 
    return m

  def min_outdegree(self):
    '''
    returns the minimum of the nodes' output degrees
    '''
    m = self.get_node_by_id(self.get_nodes_ids()[0]).outdegree()+20
    for k in self.get_nodes_ids():
      ind = self.get_node_by_id(k).outdegree()
      if k in self.get_input_ids() : ind+=1
      if ind < m : m = ind 
    return m

  def max_degree(self):
    '''
    returns the maximum of the nodes' total degrees
    '''
    return max(self.max_indegree(), self.max_outdegree())

  def min_degree(self):
    '''
    returns the minimum of the nodes' total degrees
    '''
    return min(self.min_indegree(), self.min_outdegree())

  def is_cyclic(self):
    '''
    tests wether or not the graph is cyclic : applying the algorithm from the diapositives
    '''
    g = self.copy()
    while len(g.get_nodes_ids()) != 0:
      found = False
      for k in g.get_nodes_ids() :
        n = g.get_node_by_id(k)
        if n.indegree() == 0 : 
          g.remove_node_by_id(k)
          found = True
          break
      if not found : return True
    return False

  #TD7 : NEED TESTS
  def min_id(self):
    return min(self.get_nodes_ids())

  def max_id(self):
    return max(self.get_nodes_ids())

  def shift_indices(self,n):
    cpls = [(i, i+n) for i in self.get_nodes_ids()]
    self.change_ids(cpls)

  def iparallel(self,g):
    self.shift_indices(g.max_id())
    for k in g.get_nodes_ids():
      self.nodes[k] = g.get_node_by_id(k)
  
  def parallel(self,g):
    res = self.copy()
    res.shift_indices(g.max_id())
    for k in g.get_nodes_ids():
      res.nodes[k] = g.get_node_by_id(k)
    return res
  
  def icompose(self,g):
    if len(g.get_output_ids()) != len(self.get_input_ids()):
      raise Exception("Compostion failed : output & input could not be linked properly")
    self.shift_indices(g.max_id())
    for k in g.get_nodes_ids():
      self.nodes[k] = g.get_node_by_id(k)
    for i in range(g.get_output_ids()):
      self.add_edge(g.get_output_ids()[i], self.get_input_ids()[i])
    self.input = g.input
    
  def compose(self, g):
    if len(g.get_output_ids()) != len(self.get_input_ids()):
      raise Exception("Compostion failed : output & input could not be linked properly")
    res = self.copy()
    res.shift_indices(g.max_id())
    for k in g.get_nodes_ids():
      res.nodes[k] = g.get_node_by_id(k)
    for i in range(g.get_output_ids()):
      res.add_edge(g.get_output_ids()[i], self.get_input_ids()[i])
    res.input = g.input
    return res

  def connected_components(self):
    dic = dict()
    def color_neighbours(n, ncomp):
      dic[n.id] = ncomp
      for neighid in n.get_children_ids() :
        if neighid not in dic : color_neighbours(self.get_node_by_id(neighid), ncomp)
      for neighid in n.get_parent_ids() :
        if neighid not in dic : color_neighbours(self.get_node_by_id(neighid), ncomp)

    count_comp = 0
    for k in self.get_nodes_ids():
      if k not in dic :
        color_neighbours(self.get_node_by_id(k), count_comp)
        count_comp+=1

    return (count_comp, dic)
  
  def split_with_invert(self):
    (nbc, dic) = self.connected_components()
    res = [open_digraph.empty() for _ in range(nbc)]
    for i in dic :
      res[dic[i]].node[i] = self.get_node_by_id(i)

    inps = []
    for i in range(len(res)):
      for nid in res[i].get_nodes_ids() :
        if nid in self.get_input_ids():
          inps.append(nid)
    sig = [inps[s] for s in self.get_input_ids()]
    inverti = invert_permutation(sig) 

    outs = []
    for i in range(len(res)):
      for nid in res[i].get_nodes_ids() :
        if nid in self.get_output_ids():
          outs.append(nid)
    sig = [outs[s] for s in self.get_output_ids()]
    inverto = invert_permutation(sig) 

    return (res, inverti, inverto)

  #TD9 : NEED TESTS

  def merge_nodes(self, id1, id2, new_label=None):
    n1 = self.get_node_by_id(id1)
    n2 = self.get_node_by_id(id2)

    for cid in n2.get_children_ids(): self.add_edge(n1, cid)
    for pid in n2.get_parent_ids(): self.add_edge(pid, n1)

    if new_label != None : n1.set_label(new_label)
    self.remove_node_by_id(id2)


#TD3 : Function

def graph_from_adjacency_matrix(matrix):
  '''
  returns a graph generated from the given matrix, treated as an adjacency matrix.
  '''
  size = len(matrix)
  res = open_digraph.empty()
  for i in range(0, size):
    for j in range(0, size):
      x = matrix[i][j]
      if x != 0 :
        if i in res.nodes and j in res.nodes :
          edges = [(i,j) for _ in range(x)]
          res.add_edges(edges)
        if i not in res.nodes :
          children = [j for _ in range(x)]
          res.nodes[i] = node(i, '%d' % i, [], children)
        if j not in res.nodes :
          parents = [i for _ in range(x)]
          res.nodes[j] = node(j,'%d' % j, parents, [])
  return res
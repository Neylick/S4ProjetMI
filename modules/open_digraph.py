from modules.utils import *

class node:
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
    return node(self.id, self.label, self.parents.copy(), self.children.copy())

  def get_id(self):
    return self.id 

  def get_label(self):
    return self.label
  
  def get_parent_ids(self):
    return self.parents
  
  def get_children_ids(self):
    return self.children

  def set_id(self, _id):
    self.id = _id

  def set_label(self, _label):
    self.label = _label

  def set_parent_ids(self, _ids):
    self.parents = _ids
    self.parents.sort()
  
  def set_children_ids(self, _ids):
    self.children = _ids
    self.children.sort()

  def add_child_id(self, _id):
    self.children.append(_id)
    self.children.sort()

  def add_parent_id(self, _id):
    self.parents.append(_id)
    self.parents.sort()

  def remove_child_id(self, _id):
    self.children.remove(_id)

  def remove_parent_id(self, _id):
    self.parents.remove(_id)

  def remove_child_id_all(self, _id):
    remove_all(self.children, _id)

  def remove_parent_id_all(self, _id):
    remove_all(self.parents, _id)

  def indegree(self):
    return len(self.parents)

  def outdegree(self):
    return len(self.children)
  
  def degree(self):
    return self.indegree() + self.outdegree()


class open_digraph: # for open directed graph
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
    return self.inputs == g.inputs and self.outputs == g.outputs and self.nodes == g.nodes

  def empty():
    return open_digraph([],[],{})

  def copy(self):
    return open_digraph(self.inputs, self.outputs, [self.nodes[k].copy() for k in self.nodes])

  def get_input_ids(self):
    return self.inputs
  
  def get_output_ids(self):
    return self.outputs
  
  def get_id_node_map(self):
    return self.nodes
  
  def get_nodes(self):
    return [self.nodes[k] for k in self.nodes]
  
  def get_nodes_ids(self):
    return [k for k in self.nodes]

  def get_node_by_id(self, _id):
    return self.nodes[_id]

  def get_nodes_by_ids(self, _ids):
    return [self.nodes[k] for k in _ids]

  def set_input_ids(self, _ids):
    self.inputs = _ids
  
  def set_output_ids(self, _ids):
    self.outputs = _ids

  def add_input_id(self, _id):
    self.inputs.append(_id)

  def add_output_id(self, _id):
    self.outputs.append(_id)

  #A tester :
  def new_id(self):
    if len(self.nodes) == 0 : return 0
    else : return max(self.get_nodes_ids()) + 1

  def add_edge(self, src, tgt):
    self.nodes[src].add_child_id(tgt)
    self.nodes[tgt].add_parent_id(src)
    if len(self.nodes[src].get_parent_ids()) == 0 and src not in self.get_input_ids() :
      self.add_input_id(src)
    if len(self.nodes[tgt].get_children_ids()) == 0 and tgt not in self.get_output_ids() :
      self.add_output_id(tgt)
  
  def add_edges(self, srcs_and_tgts):
    for couple in srcs_and_tgts :
      self.add_edge(couple[0], couple[1])

  def add_node(self, label="", parents=[], children=[]):
    indice = self.new_id()
    self.nodes[indice] = node(indice, label, parents, children)
    for p in parents : self.nodes[p].add_child_id(indice)
    for c in children : self.nodes[c].add_parent_id(indice)
    return indice

  def remove_edge(self, src, tgt):
    self.nodes[src].remove_child_id(tgt)
    self.nodes[tgt].remove_parent_id(src)
    if src in self.inputs and len(self.nodes[src].get_children_ids()) == 0 :
      self.inputs.remove(src)
    if tgt in self.outputs and len(self.nodes[tgt].get_parent_ids()) == 0 :
      self.inputs.remove(src)

  def remove_node_by_id(self, _id):
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

  def graph_from_adjacency_matrix(self, matrix):
    size = len(matrix)
    res = open_digraph.empty()
    for i in range(0, size):
      for j in range(0, size):
        x = matrix[i][j]
        if x != 0 :
          if i not in res.nodes :
            children = [j for _ in range(0,x)]
            res.nodes[i] = node(i, '%d' % i, [], children)
          if j not in res.nodes :
            parents = [i for _ in range(0, x)]
            nj = node(j,'%d' % j, parents, [])
            res.nodes[j] = nj
          
          edges = [(i,j) for _ in range(0, x)]
          res.add_edges(edges)
    return res

  def random(self, size, bound, inputs=[], outputs=[], form="free", loop_free=False):
    '''
      A COMPLETER
    '''
    res = open_digraph.empty()
    if "loop-free" in form or "loop_free" in form or "noloop" in form :
      if "DAG" in form:
        res= self.graph_from_adjacency_matrix(random_triangular_int_matrix(size,bound,True))
      elif "oriented" in form:
        res= self.graph_from_adjacency_matrix(random_oriented_int_matrix(size,bound,True))
      elif "undirected" in form:
        res= self.graph_from_adjacency_matrix(random_symetric_int_matrix(size,bound,True))
      else :
        res= self.graph_from_adjacency_matrix(random_int_matrix(size,bound,True))
    else :
      if "DAG" in form:
        res= self.graph_from_adjacency_matrix(random_triangular_int_matrix(size,bound,False))
      elif "oriented" in form:
        res= self.graph_from_adjacency_matrix(random_oriented_int_matrix(size,bound,False))
      elif "undirected" in form:
        res= self.graph_from_adjacency_matrix(random_symetric_int_matrix(size,bound,False))
      else :
        res= self.graph_from_adjacency_matrix(random_int_matrix(size,bound,False))
    res.set_input_ids(inputs)
    res.set_output_ids(outputs)
    return res

  def max_indegree(self):
    return max([n.indegree for n in self.get_nodes()])

  def min_indegree(self):
    return min([n.indegree for n in self.get_nodes()])

  def max_outdegree(self):
    return max([n.outdegree for n in self.get_nodes()])

  def min_outdegree(self):
    return min([n.outdegree for n in self.get_nodes()])

  def max_degree(self):
    return max(self.max_indegree, self.max_outdegree)

  def min_degree(self):
    return min(self.min_indegree, self.min_outdegree)

  def is_cyclic(self):
    g = self.copy()
    while len(g.get_nodes() != 0):
      for k in g.get_id_node_map() :
        n = g.get_node_by_id(k)
        if n.indegree() == 0 : 
          g.remove_node_by_id(k)
          break
      return False
    return True


'''
  def change_id(self, node_id , new_id):
    if new_id in self.nodes :
      self.change_id(new_id, self.new_id())
    n = self.get_node_by_id(node_id)
    for p in n.parents :
      self.nodes[p]. 
    for c in n.children :
      self.nodes[c].remove_parent_id_all(node_id)
'''
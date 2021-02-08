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
    if len(node) == 0 : 
      return 0
    else :
      nextid = float('-inf')
      for n in self.nodes :
        if n.id > nextid : 
          nextid = n.id+1
      return nextid

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
    n = node(indice, label, parents, children)
    self.nodes[indice] = n
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
    for p in self.nodes[_id].get_parent_ids():
      self.nodes[p].remove_child_id_all(_id)
    for c in self.nodes[_id].get_children_ids():
      self.nodes[c].remove_parent_id_all(_id)
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
          if (count_occurences(self.nodes[c].get_parents_ids(), k) != occ) :
            return False
    return True

'''
n0=node(0,'a',[],[1])
n1=node(1,'b',[1],[0])
g=open_digraph([0],[1],[n0,n1])
print(n0)
print(g)
print(open_digraph.empty())
'''
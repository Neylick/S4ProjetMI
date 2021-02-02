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
  
  def set_children_ids(self, _ids):
    self.children = _ids

  def add_child_id(self, _id):
    self.children.append(_id)

  def add_parent_id(self, _id):
    self.parents.append(_id)

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

  def new_id(self):
    if len(node) == 0 : return 0
    else :
      nextid = float('-inf')
      for n in self.nodes :
        if n.id > nextid : nextid = n.id+1
      return nextid



'''
n0=node(0,'a',[],[1])
n1=node(1,'b',[1],[0])
g=open_digraph([0],[1],[n0,n1])
print(n0)
print(g)
print(open_digraph.empty())
'''
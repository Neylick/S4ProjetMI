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
    return "("+str(self.id)+", '"+self.label+"', "+str(self.parents)+", "+str(self.children)+")"

  def __repr__(self):
    return "node"+str(self)

  def copy(self):
    return node(self.id, self.label, self.parents, self.children)

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
    return open_digraph(self.inputs, self.outputs, {n.id:n.copy() for n in self.nodes})

n0=node(0,'a',[],[1])
n1=node(1,'b',[1],[0])
g=open_digraph([0],[1],[n0,n1])
print(n0)
print(g)
print(open_digraph.empty())
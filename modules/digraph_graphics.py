#TD4

import sys
sys.path.append('./../')
from PIL import Image, ImageDraw
from modules.open_digraph import *
from random import randrange
import math

width = 500
height = 500

image = Image.new("RGB", (width, height), 'white')
draw = ImageDraw.Draw(image)


class vertex:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def coord(self):
    return (round(self.x), round(self.y))
  def copy(self):
    return vertex(self.x,self.y)
  def __add__(self, v):
    return vertex(self.x+v.x, self.y+v.y)
  def __sub__(self, v):
    return vertex(self.x-v.x, self.y-v.y)
  def __rmul__(self, scalar):
    return vertex(self.x*scalar, self.y*scalar)
  __mul__ = __rmul__
  def rotate(self, angle, v=None):
    if v is None : v = vertex(0,0)
    s = math.sin(angle)
    c = math.cos(angle)
    return v+vertex(c*(self.x-v.x) - s*(self.y-v.y), s*(self.x-v.x) + c*(self.y-v.y)) 

def drawarrow(self, v1, v2, n=1, m=0):
  '''
  draws an arrow between the two given vertices
  '''
  self.line([v1.coord(),v2.coord()], 'black')
  s = slope_angle(v1,v2)
  m1 = v1+(v2-v1)*(3/4.)
  m2 = v1+(v2-v1)*(1/4.)
  middle = v1+(v2-v1)*(1/2.)

  rm1a = m1.rotate(math.pi/2, middle)
  rm1b = m1.rotate(-math.pi/2, middle)
  rm2a = m2.rotate(math.pi/2, middle)
  rm2b = m2.rotate(-math.pi/2, middle)


  #First arrow
  self.line([m1.coord(), (rm1a-(rm1a-m1)*(3/4.)).coord()], 'black')
  self.line([m1.coord(), (rm1b-(rm1b-m1)*(3/4.)).coord()], 'black')
  #Second arrow
  self.line([m2.coord(), (rm2a-(rm2a-m2)*(3/4.)).coord()], 'black')
  self.line([m2.coord(), (rm2b-(rm2b-m2)*(3/4.)).coord()], 'black')

  #text
  self.text((m1+vertex(3,3)).coord(),str(n), fill='black')
  self.text((m2-vertex(7,7)).coord(),str(m), fill='black')

ImageDraw.ImageDraw.arrow = drawarrow

def drawnode(self, node, v, verbose=False):
  '''
  draws a node one the selected vertex, if verbose is true, also shows its id.
  '''
  self.ellipse([v.x-1, v.y-1, v.x+1, v.y+1], fill='black')
  self.text((v+vertex(5,5)).coord(), node.get_label(), fill='black')
  if verbose : self.text((v-vertex(12,12)).coord(), str(node.get_id()), fill='black')
ImageDraw.ImageDraw.node = drawnode

def drawgraph(self, graph, method='random', node_pos=dict(), input_pos=[], output_pos=[]):
  '''
  draws a graph with selected layout (and positions if manual)   
  '''
  if method == 'random' or method == 'rand' :
    layout = random_layout(graph)
    node_pos = layout[0]
    input_pos = layout[1]
    output_pos = layout[2]
  if method == 'circle' :
    layout = circle_layout(graph)
    node_pos = layout[0]
    input_pos = layout[1]
    output_pos = layout[2]
  
  for k in graph.get_id_node_map() :
    self.node(graph.get_node_by_id(k), node_pos[k])
    #missing arrows between nodes here

  
  for i in range(len(input_pos)) :
    self.arrow(input_pos[i], node_pos[graph.get_input_ids()[i]])
  for i in range(len(output_pos)) :
    self.arrow(output_pos[i], node_pos[graph.get_output_ids()[i]])

ImageDraw.ImageDraw.graph = drawgraph

def random_layout(graph):
  '''
  returns node positions, input positions, output positions, all randomized
  '''
  graph_node_dic = graph.get_id_node_map()
  graph_inputs = graph.get_input_ids()
  graph_outputs = graph.get_output_ids()

  node_pos = {k:vertex(randrange(0,width), randrange(0,height)) for k in graph_node_dic}
  input_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_inputs]
  output_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_outputs]
  return (node_pos, input_pos, output_pos)

def circle_layout(graph):
  '''
  returns node positions, input positions, output positions, making it so that it's all placed as a circle layout
  '''
  v = vertex(3*width/4, 3*height/4)
  size = len(graph.get_nodes())
  graph_inputs = graph.get_input_ids()
  graph_outputs = graph.get_output_ids()

  node_pos = {k:v.rotate(2*math.pi/size, vertex(0,0)) for k in graph.get_id_node_map()}
  input_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_inputs]
  output_pos = [node_pos[k]+vertex(randrange(0,width/10), randrange(0, height/10)) for k in graph_outputs]
  return (node_pos, input_pos, output_pos)

#TD10

def DAG_layout(graph):
  graph_inputs = graph.get_input_ids()
  graph_outputs = graph.get_output_ids()

  node_pos = { k:vertex(0,0) for k in graph.get_id_node_map() }

  topo = graph.topo_sort()
  line_count = len(topo)+2 #node line + input line + output line
  for y in range(len(topo)) :
    line = topo[y]
    for x in range(len(line)) :
      node_pos[ line[x] ] = vertex(x*width/len(line), (y+1)*height/line_count)

  input_pos = [ vertex( node_pos[k].coord().x, 0) for k in graph_inputs ]
  output_pos = [ vertex( node_pos[k].coord().x, height) for k in graph_outputs ]

  return (node_pos, input_pos, output_pos)


def slope_angle(v1, v2):
  '''
  returns the slope between the two given vector's angle 
  '''
  a = (v2.y-v1.y)/(v2.x-v1.x)
  b = v2.y%(a*v2.x)
  vertex(-b/a, 0)
  return math.atan(v1.y/(v1.x+b/a))


g = open_digraph.empty()
g.random(5,5,[],[])
draw.graph(g)
print(g)
image.save("test.jpg")



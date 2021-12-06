from copy import deepcopy


class Graph:
  def __init__(self,nodes = {}, neighbors = {}):
    self.nodes = nodes
    self.neighbors = neighbors

  def add_node(self,no,value = {}):
    self.nodes[no] = value

  def add_edge(self,no1,no2):
    self.neighbors[no1].append(no2)
  
  def degree(self,no):
    return len(self.neighbors[no])
  def remove_edge(self,no,ind):
    self.neighbors[no].pop(self.neighbors[no].index(ind))

  def copy(self):
    return deepcopy(self)

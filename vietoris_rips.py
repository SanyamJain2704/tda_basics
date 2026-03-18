import math
import networkx as nx
import numpy as np

class VietorisRips:
  def __init__(self, data, use_weights=True, max_dim=None, epsilon=None):

    self.data=data
    self.simplicial_complex={}
    self.use_weights=use_weights
    self.max_dim=max_dim
    self.epsilon=epsilon

    if isinstance(data,nx.Graph):
      self.input_type="graph"

    else:
      self.input_type="point_cloud"

  def apply_filtration(self):

    if(self.input_type=="graph"):
      return self._apply_filtration_graph(self.data)

    else:
      G=self._build_distance_graph()
      return self._apply_filtration_graph(G)

  def _apply_filtration_graph(self, G):

    self.simplicial_complex = {}

    weighted = any("weight" in data for _, _, data in G.edges(data=True))

    for clique in nx.enumerate_all_cliques(G):
        dim = len(clique) - 1

        if self.max_dim is not None and dim > self.max_dim:
            break

        if dim not in self.simplicial_complex:
            self.simplicial_complex[dim] = []

        if not weighted or not self.use_weights:
            filtration_value = dim

        else:
            if dim == 0:
                filtration_value = 0
            else:
                edges = [
                    G[u][v]["weight"]
                    for i, u in enumerate(clique)
                    for v in clique[i+1:]
                ]
                filtration_value = max(edges)

        self.simplicial_complex[dim].append((tuple(clique), filtration_value))

    return self.simplicial_complexx

  def _build_distance_graph(self):

    G=nx.Graph()
    n=len(self.data)

    for i in range(n):
      G.add_node(i)

    for i in range(n):
      for j in range(i+1,n):
        d=self._distance(self.data[i],self.data[j])
        if self.max_dim is None or d<=self.max_dim:
          G.add_edge(i,j,weight=d)

    return G

  def _distance(self,p,q):

    return np.linalg.norm(p-q)

  def get_filtration_list(self):

    if not self.simplicial_complex:
      self.apply_filtration()
    
    filtration_list=[]

    for dim in self.simplicial_complex:
      for clique,filtration_value in self.simplicial_complex[dim]:
        filtration_list.append((clique,filtration_value))

    filtration_list.sort(key = lambda x: (x[1],len(x[0])))

    return filtration_list
        




  
  

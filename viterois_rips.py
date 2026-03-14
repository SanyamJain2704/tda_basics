import math
import networkx as nx

class VietorisRips:
  def __init__(self, data):

    self.data=data
    self.simplicial_complex={}

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

  def _apply_filtration_graph(self,G):

    weighted=any( "weight" in data for _,_,data in G.edges(data=True)) ##Check if the graph is weighted

    for clique in nx.enumerate_all_cliques(G):
      dim = len(clique)-1

      if dim not in self.simplicial_complex:
        self.simplicial_complex[dim]=[]

      if not weighted:
        filtration_value=dim
      
      else:
        if dim==0:
          filtration_value=0
        
        else:
          edges=[
              G[u][v]["weight"]
              for i,u in enumerate(clique)
              for v in clique[i+1:]
          ]

          filtration_value=max(edges)

      self.simplicial_complex[dim].append((tuple(clique), filtration_value))

    return self.simplicial_complex

  def _build_distance_graph(self):

    G=nx.Graph()
    n=len(self.data)

    for i in range(n):
      G.add_node(i)

    for i in range(n):
      for j in range(i,n+1):
        d=self._distance(i,j)
        G.add_edge(i,j,weight=d)

    return G

  def _distance(self,i,j):

    return math.sqrt(sum((a-b)**2 for a,b in zip(i,j)))

  
  

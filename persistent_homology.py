import networkx as nx
import math
import numpy as np
from itertools import combinations
from vietoris_rips import VietorisRips


def face(simplex):

  face=[]
  k=len(simplex)
  
  for s in combinations(simplex,k-1):
    face.append(tuple(s))

  return face

  

def build_simplex_index(filtration):

  simplex_index={}

  for i,(simplex,_) in enumerate(filtration):
    simplex_index[simplex]=i

  return simplex_index


def build_boundary_matrix(filtration):

  simplex_index=build_simplex_index(filtration)

  boundary_matrix=[[] for _ in range(len(filtration))]
  
  for j,(simplex,_) in enumerate(filtration):

    if(len(simplex)==1):
      continue
    
    for f in face(simplex):
      boundary_matrix[j].append(simplex_index[f])

  return boundary_matrix
    

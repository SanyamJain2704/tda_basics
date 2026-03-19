import networkx as nx
import math
import numpy as np
from itertools import combinations
from vietoris_rips import VietorisRips
import matplotlib.pyplot as plt

def faces(simplex):

  faces_list=[]
  k=len(simplex)
  
  for s in combinations(simplex,k-1):
    faces_list.append(tuple(sorted(s)))

  return faces_list

  

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
    
    for f in faces(simplex):
      boundary_matrix[j].append(simplex_index[f])

    boundary_matrix[j].sort()

  return boundary_matrix

def xor_lists(a, b):
    return sorted(list(set(a) ^ set(b)))

def reduce_boundary_matrix(boundary_matrix):

    reduced = [col.copy() for col in boundary_matrix]

    low_dict = {}

    for j in range(len(reduced)):

        while True:

            if not reduced[j]:
                break

            pivot = max(reduced[j])

            if pivot in low_dict:

                k = low_dict[pivot]

                reduced[j] = xor_lists(reduced[j], reduced[k])

                reduced[j].sort()

            else:
                break

        if reduced[j]:
            pivot = max(reduced[j])
            low_dict[pivot] = j

    return reduced, low_dict

def extract_pairs(filtration, reduced, low_dict):

    pairs = []
    
    used_births = set()

    for pivot, j in low_dict.items():
        pairs.append((pivot, j))
        used_births.add(pivot)

    for i in range(len(filtration)):
        if not reduced[i] and i not in used_births:
            pairs.append((i, float('inf')))

    return pairs
    
def convert_pairs_to_times(filtration, pairs):

    timed_pairs = []

    for i, j in pairs:

        birth = filtration[i][1]

        if j == float('inf'):
            death = float('inf')
        else:
            death = filtration[j][1]

        timed_pairs.append((birth, death))

    return timed_pairs

def group_pairs_by_dimension(filtration, pairs):

    dim_pairs = {}

    for i, j in pairs:

        simplex = filtration[i][0]
        dim = len(simplex) - 1

        if dim not in dim_pairs:
            dim_pairs[dim] = []

        dim_pairs[dim].append((i, j))

    return dim_pairs

def convert_dim_pairs_to_times(filtration, dim_pairs):

    result = {}

    for dim in dim_pairs:

        result[dim] = []

        for i, j in dim_pairs[dim]:

            birth = filtration[i][1]

            if j == float('inf'):
                death = float('inf')
            else:
                death = filtration[j][1]

            result[dim].append((birth, death))

    return result

def plot_persistence_diagram(dim_times):
    
    plt.figure(figsize=(6,6))
    
    colors = {
        0: 'blue',
        1: 'red',
        2: 'green',
        3: 'purple'
    }
    
    max_val = 0
    
    for dim in dim_times:
        for birth, death in dim_times[dim]:
            if death != float('inf'):
                max_val = max(max_val, birth, death)
            else:
                max_val = max(max_val, birth)
    
    inf_proxy = max_val * 1.1 + 0.1
    
    for dim in dim_times:
        label_added = False  
        for birth, death in dim_times[dim]:
            
            plot_death = inf_proxy if death == float('inf') else death
            is_inf = death == float('inf')
            
            plt.scatter(
                birth, plot_death,
                color=colors.get(dim, 'black'),
                label=f"H{dim}" if not label_added else "",
                marker='*' if is_inf else 'o',  
                s=80,
                zorder=3
            )
            label_added = True
    
    plt.plot([0, inf_proxy], [0, inf_proxy], 'k--', linewidth=1)
    
    plt.axhline(y=inf_proxy, color='gray', linestyle=':', linewidth=1, label='∞ (never dies)')
    
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    
    plt.xlabel("Birth")
    plt.ylabel("Death")
    plt.title("Persistence Diagram")
    plt.grid(True)
    plt.show()

def plot_barcodes(dim_times):
    
    plt.figure(figsize=(8, 5))
    
    colors = {
        0: 'blue',
        1: 'red',
        2: 'green',
        3: 'purple'
    }
    
    max_val = 0
    for dim in dim_times:
        for birth, death in dim_times[dim]:
            if death != float('inf'):
                max_val = max(max_val, birth, death)
            else:
                max_val = max(max_val, birth)
    
    inf_proxy = max_val * 1.1 + 0.1
    
    y = 0  
    yticks = []
    yticklabels = []
    
    for dim in sorted(dim_times.keys()):
        for birth, death in dim_times[dim]:
            
            plot_death = inf_proxy if death == float('inf') else death
            is_inf = death == float('inf')
            
            plt.hlines(
                y=y,
                xmin=birth,
                xmax=plot_death,
                colors=colors.get(dim, 'black'),
                linewidth=2
            )
            
            if is_inf:
                plt.annotate(
                    '', 
                    xy=(plot_death + 0.01, y),
                    xytext=(plot_death, y),
                    arrowprops=dict(arrowstyle='->', color=colors.get(dim, 'black'))
                )
            
            yticks.append(y)
            yticklabels.append(f"H{dim}")
            y += 1
        
        y += 1
    
    plt.axvline(x=0, color='black', linewidth=0.8, linestyle='--')
    
    plt.yticks(yticks, yticklabels, fontsize=7)
    plt.xlabel("Filtration Value")
    plt.title("Persistence Barcodes")
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

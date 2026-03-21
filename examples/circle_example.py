import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from vitetoris_rips_from_scratch import VietorisRips
from persistent_homology import (build_boundary_matrix, reduce_boundary_matrix,
                          extract_pairs, convert_pairs_to_times,
                          group_pairs_by_dimension, convert_dim_pairs_to_times)
from point_cloud_helpers import generate_circle
from visualization import plot_persistence_diagram, plot_barcodes

if __name__ == "__main__":

    points = generate_circle()
    vr = VietorisRips(points, max_dim=2, epsilon=0.25) 
    filtration = vr.get_filtration_list()
  
    boundary_matrix = build_boundary_matrix(filtration)
    reduced, low_dict = reduce_boundary_matrix(boundary_matrix)
    pairs = extract_pairs(filtration, reduced, low_dict)
    timed_pairs = convert_pairs_to_times(filtration, pairs)
    dim_pairs = group_pairs_by_dimension(filtration, pairs)
    timed_dim_pairs = convert_dim_pairs_to_times(filtration, dim_pairs)
  
    plot_persistence_diagram(timed_dim_pairs)
    plot_barcodes(timed_dim_pairs)
    print("\nIndex pairs (birth, death):")
    print(pairs)
    print("\nFiltration value pairs:")
    print(timed_pairs)
    print("\nDimension-wise pairs:")
    print(timed_dim_pairs)

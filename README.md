# tda_basics
This repository currently implements Vietoris–Rips filtration from scratch for:
1. Graphs (NetworkX)
2. Point Clouds

Since this is a first implementation, it currently utilizes NetworkX to handle graph functionalities. 
In the future, I could move away from it.  
This repo is being made for better understanding of TDA concepts and implementing stuff from scratch.
I will try to regularly update it with the next steps in a TDA pipeline.

## For the Math enthusiasts:
1. What is a Vietoris-Rips complex?
  
   A Vietoris–Rips complex is a simplicial complex constructed from a set of points and a distance threshold $r$. A simplex is included      whenever all pairwise distances between its vertices are at most $r$. Formally, A Vietoris–Rips complex at scale $r$ is the
   simplicial complex
   $$VR(X, r) = \{ \sigma \subseteq X \mid d(x_i, x_j) \le r \text{ for all } x_i, x_j \in \sigma \}$$


3. What is a simplicial complex or a simplex?

   A simplex is the convex hull of \(k+1\) affinely independent points, forming a \(k\)-dimensional generalization of a triangle or
   tetrahedron. Simply speaking, all points independently form a $0$-simplex, and if I connect two points via an edge, they form a
   $1$-simplex. Following this, a $2$-simplex is simply a triangle! I connected three non-collinear points to form a triangle and that's it!
   This approach can be carried out to higher dimensions as well. But beware, A SQUARE IS NOT A $3$-simplex, a tetrahedron is. 

   


# Import the required libraries.
import numpy as np

# For a formatted output
import pandas as pd
from tabulate import tabulate

"""
The Graph Class
"""

class Graph:
    def __init__(self):
        # Dictionary containing keys that map to the corresponding vertex
        # object.
        self.vertices = {}
        
    def addVertex(self, key):
        # Add a vertex with the given key to the graph.
        vertex = Vertex(key)
        self.vertices[key] = vertex
        
    def getVertex(self, key):
        # Return vertex object with the corresponding key.
        return self.vertices[key]
    
    def __contains__(self, key):
        return key in self.vertices
    
    def addEdge(self, src_key, dest_key, weight=1):
        # Add edge from src_key to dest_key with given weight.
        self.vertices[src_key].addNeighbor(self.vertices[dest_key], weight)
        
    def doesEdgeExist(self, src_key, dest_key):
        # Return True if there is an edge from the given source and destination
        # key pair.
        return self.vertices[src_key].doesPointTo(self.vertices[dest_key])
    
    def __iter__(self):
        return iter(self.vertices.values())

"""
The Vertex Class
"""

class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

        # Initialize the gene_copy_number attribute.
        self.gene_copy_number = np.zeros(8)
        
    def getKey(self):
        # Return the key corresponding to this vertex object.
        return self.key
    
    def addNeighbor(self, dest, weight):
        # Make this vertex point to dest with given edge weight.
        self.points_to[dest] = weight
        
    def getNeighbors(self):
        # Return all vertices pointed to by this vertex.
        return self.points_to.keys()
    
    def getWeight(self, dest):
        # Get weight of edge from this vertex to dest.
        return self.points_to[dest]
    
    def doesPointTo(self, dest):
        # Return True if this vertex points to dest.
        return dest in self.points_to
    
    def addGeneCopyNumber(self, gcn):
        # Add an array of gene probe copy numbers for the specified cell count
        # pattern (each is represented as a vertex in our case.)
        self.gene_copy_number = gcn

    def getGeneCopyNumber(self):
        # Return the gene probe copy number for this vertex (cell count pattern).
        return self.gene_copy_number

"""
Test Run
"""

# Load the test data file into a numpy array.
data = np.loadtxt("test.txt", skiprows=2)

# Declare a Graph instance.
g = Graph()

# Compute the number of vertices (cell count patterns).
num_vertices = len(data)

# Add all the vertices to the graph object.
for idx in range(num_vertices):
    # print(row)
    g.addVertex(idx)
    vertex = g.getVertex(idx)
    vertex.addGeneCopyNumber(data[idx][3:-1].astype(int))

# Create an array to store the copy number data for vertices.
copy_number_array = np.empty([num_vertices,8]).astype(int)

for i in range(num_vertices):
    vertex = g.getVertex(i)
    copy_number_array[i] = vertex.getGeneCopyNumber().astype(int)

# Create an array to store the pairwise Manhattan distances.
manhattan_distance_matrix = np.empty([num_vertices, num_vertices]).astype(int)

for i in range(num_vertices):
    for j in range(num_vertices):
        manhattan_distance_matrix[i][j] = abs(sum(np.subtract(copy_number_array[i],
        copy_number_array[j]))).astype(int)

# # Sanity Check
# print("DEBUG: copy_number_array\n", copy_number_array)

# Print out the Manhattan Distance array in a tabular format.
manhattan_df = pd.DataFrame(manhattan_distance_matrix)
# Print out the matrix in a fancy grid format for visualization.
print(tabulate(manhattan_df, headers='keys', tablefmt="fancy_grid"))
# # Print out in the format of html table for Github README.md file.
# print(tabulate(manhattan_df, headers='keys', tablefmt="html"))
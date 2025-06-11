from Graph import Graph

class GraphShortestPath(Graph):

    def shortest_path(self, start, end): 
        """
        Calculate the shortest path from a starting node to an ending node in a sparse graph
        with potentially 10000s of nodes. Must run under 0.5 second and find the shortest distance between two nodes.

        Parameters:
        start: The starting node.
        end: The ending node.

        Returns:
        A tuple containing the total distance of the shortest path and a list of nodes representing that path.
        """
        dist = None
        path = None
        # Your code here
        return dist, path
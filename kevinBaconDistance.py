import networkx as nx
import pandas as pd

graph = nx.read_gml("files/files/actorsGraph.gml")

maxDistance = 0
agregatedDistance = 0
numberOfConnectedActors = 0
numberOfUnconnectedActors = 0

kevin = "Kevin Bacon"

for actor in graph.nodes:
    if actor != kevin:
        try:
            shortestPath = nx.shortest_path_length(graph, actor, kevin)
            agregatedDistance += shortestPath
            numberOfConnectedActors += 1

            if shortestPath > maxDistance:
                maxDistance = shortestPath

        except nx.NetworkXNoPath:
            numberOfUnconnectedActors += 1

averageDistance = agregatedDistance / numberOfConnectedActors

file = open("files/kevinBaconDistance.txt","w")

file.write("Avarage distance to Kevin Bacon is " + str(averageDistance) + "!\n")
file.write("Maximum distance to Kevin Bacon is " + str(maxDistance) + "!\n")
file.write("Number of unconnected actors is " + str(numberOfUnconnectedActors) + "!\n")

file.close()
import networkx as nx
import pandas as pd

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
actorsColumn = sheet["Actors"]
graph = nx.Graph()

for actorsRow in actorsColumn:
    actors = actorsRow.split(',')

    for i in range(len(actors)-1):
        for j in range(i+1,len(actors)):
            firstActor = actors[i].strip()
            secondActor = actors[j].strip()
            if (graph.has_edge(firstActor,secondActor)):
                graph[firstActor][secondActor]['weight'] = graph[firstActor][secondActor]['weight'] + 1
            else:
                graph.add_edge(firstActor,secondActor, weight=1)

nx.write_gml(graph, "files/actorsGraph.gml")
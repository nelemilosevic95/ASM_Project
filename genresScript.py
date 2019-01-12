import networkx as nx
import pandas as pd

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
genresColumn = sheet["Genre"]
graph = nx.Graph()

for genresRow in genresColumn:
    genres = genresRow.split(',')

    for i in range(len(genres)-1):
        for j in range(i+1,len(genres)):
            firstGenre = genres[i].strip()
            secondGenre = genres[j].strip()
            if (graph.has_edge(firstGenre,secondGenre)):
                graph[firstGenre][secondGenre]['weight'] = graph[firstGenre][secondGenre]['weight'] + 1
            else:
                graph.add_edge(firstGenre,secondGenre, weight=1)

nx.write_gml(graph, "files/genresGraph.gml")
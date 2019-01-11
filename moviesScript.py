import networkx as nx
import pandas as pd

#pre pokretanja skripte potrebno je sortirati IMDB-Movie-Data.scv po godini

sheet = pd.read_csv("IMDB-Movie-Data.csv")
titleColumn = sheet["Title"]
actorsColumn = sheet["Actors"]
graph = nx.Graph()

actorsMovies = {}

for i in range(len(titleColumn)):
    actors = actorsColumn[i].split(',')
    movieTitle = titleColumn[i].strip()

    graph.add_node(movieTitle)

    for actor in actors:
        actor = actor.strip()
        if actor not in actorsMovies:
            actorsMovies[actor] = []
        actorsMovies[actor].append(movieTitle)

for actor, movies in actorsMovies.items():
    for i in range(len(movies)-1):
        for j in range(i+1,len(movies)):
            firstMovie = movies[i]
            secondMovie = movies[j]
            if graph.has_edge(firstMovie,secondMovie):
                graph[firstMovie][secondMovie]['weight'] = graph[firstMovie][secondMovie]['weight'] + 1
            else:
                graph.add_edge(firstMovie,secondMovie,weight=1)


nx.write_gml(graph, "files/moviesGraph.gml")


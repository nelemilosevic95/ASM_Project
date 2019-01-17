import networkx as nx
import pandas as pd
import sys

#pre pokretanja skripte potrebno je sortirati IMDB-Movie-Data.scv po godini

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")

filterOn = 0

if len(sys.argv) == 2:
    filterOn = 1
    movieRevenueColumn = sheet["Revenue (Millions)"]
    filterRevenue = float(sys.argv[1])


titleColumn = sheet["Title"]
actorsColumn = sheet["Actors"]
graph = nx.Graph()

actorsMovies = {}

for i in range(len(titleColumn)):
    actors = actorsColumn[i].split(',')
    movieTitle = titleColumn[i].strip()

    if filterOn == 1:
        movieRevenue = float(movieRevenueColumn[i])
        if movieRevenue < filterRevenue:
            continue

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

if filterOn == 1:
    nx.write_gml(graph, "files/moviesGraphFiltered-" + str(filterRevenue) + ".gml")
else:
    nx.write_gml(graph, "files/moviesGraph.gml")


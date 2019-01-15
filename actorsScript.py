import networkx as nx
import pandas as pd
from actorsProductivity import ActorProductivity

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
actorsColumn = sheet["Actors"]
genresColumn = sheet["Genre"]

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

actorsProductivity = {}

for i in range(len(actorsColumn)):
    actors = actorsColumn[i].split(',')
    genres = genresColumn[i].split(',')

    for actor in actors:
        actor = actor.strip()
        if actor not in actorsProductivity:
            actorsProductivity[actor] = ActorProductivity()

        actorsProductivity[actor].incrementNumberOfMovies()

        for genre in genres:
            genre = genre.strip()
            actorsProductivity[actor].incrementGenreCount(genre)

for actor, actorsProductivity in actorsProductivity.items():
    genresInfo = actorsProductivity.getGenresInfo()
    genresInfoSorted = sorted(genresInfo.items(), key=lambda kv: kv[1], reverse=True)
    mostCommonGenres = ""

    i = 0

    for genre, genreCount in genresInfoSorted:
        mostCommonGenres += " " + genre
        if (i >= 2 or len(genresInfoSorted) <= i + 1):
            break
        i += 1

    attrs = {actor: {'genres': mostCommonGenres}}
    nx.set_node_attributes(graph, attrs)

nx.write_gml(graph, "files/actorsGraph.gml")
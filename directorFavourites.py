import pandas as pd

class ActorsInfo:

    def __init__(self):
        self.actors = {}

    def incrementActorCount(self, actor):
        if actor not in self.actors:
            self.actors[actor] = 1
        else:
            self.actors[actor] += 1

    def writeActorsInfo(self):
        sortedActorsInfo = sorted(self.actors.items(), key=lambda kv: kv[1], reverse=True)
        actorsInfo = ""
        for actor, movieCount in sortedActorsInfo:
            actorsInfo += " " + actor + ": " + str(movieCount) + "\n"

        return actorsInfo

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
actorsColumn = sheet["Actors"]
directorsColumn = sheet["Director"]

directorsFavourites = {}

for i in range(len(directorsColumn)):
    director = directorsColumn[i].strip()

    if director not in directorsFavourites:
        directorsFavourites[director] = ActorsInfo()

    actors = actorsColumn[i].split(',')

    for actor in actors:
        actor = actor.strip()
        directorsFavourites[director].incrementActorCount(actor)

file = open("files/directorsFavourites.txt","w")

for director, actorsInfo in directorsFavourites.items():
    file.write("Director: " + director + "\n")
    file.write(actorsInfo.writeActorsInfo() + "\n")

file.close()
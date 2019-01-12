import pandas as pd

class ActorProductivity:

    def __init__(self):
        self.numberOfMovies = 0
        self.genresInfo = {}

    def writeActorsProductivity(self):
        actorInfo = "Number of movies: " + str(self.numberOfMovies) + "\n"

        for genre, genreCount in self.genresInfo.items():
            actorInfo += "  " + genre + ": " + str(genreCount) + "\n"

        return actorInfo

    def incrementNumberOfMovies(self):
        self.numberOfMovies += 1

    def incrementGenreCount(self, genre):
        if genre not in self.genresInfo:
            self.genresInfo[genre] = 1
        else:
            self.genresInfo[genre] += 1

    def __lt__(self, other):
        return self.numberOfMovies < other.numberOfMovies

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
actorsColumn = sheet["Actors"]
genresColumn = sheet["Genre"]

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

sortedActorsProductivity = sorted(actorsProductivity.items(), key=lambda kv: kv[1], reverse=True)

file = open("files/actorsProductivity.txt","w")

for actor, actorProductivity in sortedActorsProductivity:
    file.write(actor + "\n")
    file.write(actorProductivity.writeActorsProductivity() + "\n")

file.close()


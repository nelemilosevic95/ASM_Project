import pandas as pd

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
directors = sheet["Director"]

directorsProductivity = {}

for director in directors:
    director = director.strip()
    if director not in directorsProductivity:
        directorsProductivity[director] = 0

    directorsProductivity[director] += 1

file = open("files/directorsProductivity.txt","w")

sortedDirectorsProductivity = sorted(directorsProductivity.items(), key=lambda kv: kv[1], reverse=True)

for directorName, movieCount in sortedDirectorsProductivity:
    file.write(directorName + "\n")
    file.write("    Number of movies: " + str(movieCount) + "\n\n")

file.close()
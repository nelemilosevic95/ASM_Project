import pandas as pd

sheet = pd.read_csv("files/IMDB-Movie-Data.csv")
years = sheet["Year"]

yearsProductivity = {}

for year in years:
    year = str(year).strip()
    if year not in yearsProductivity:
        yearsProductivity[year] = 0

    yearsProductivity[year] += 1

file = open("files/yearsProductivity.txt","w")

sortedYearsProductivity = sorted(yearsProductivity.items(), key=lambda kv: kv[1], reverse=True)

for year, movieCount in sortedYearsProductivity:
    file.write("Year " + str(year) + "\n")
    file.write("    Number of movies: " + str(movieCount) + "\n\n")

file.close()
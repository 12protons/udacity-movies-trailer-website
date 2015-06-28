"""
Displays a movie trailer page from movies defined in the
accompanied csv file.

The CSV file that contains movie info must be defined as follows:

    Title, Description, Image URL, Trailer URL
"""

import csv
import fresh_tomatoes
import media

#Initialize list of movies
movies_list = []

#Open CSV file and load movies into movies_list
with open('movies.csv', 'rb') as movies_file:
    movies_reader = csv.reader(movies_file, delimiter=',', quotechar='"')
    for row in movies_reader:
        movie = media.Movie(row[0], row[1], row[2], row[3])
        movies_list.append(movie)

#Open movies page with populated movies_list array
fresh_tomatoes.open_movies_page(movies_list)

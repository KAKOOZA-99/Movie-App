from funct.new_movie import *
def searchall():
    print('Searching for a Movie...')
    keyword = input("Enter search term: >>> ")
    for movie in add_movie.movies_list:
        if keyword in movie:
            print(movie)

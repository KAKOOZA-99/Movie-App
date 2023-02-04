import json

def add_movie():
    from ast import keyword

    try:
        movies_list = []
        infile = open("MovieList.txt", "r")
        line = infile.readline()
        while line:
            movies_list.append(line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()

    except FileNotFoundError:
        print("<theMovieList>.txt> file is not found")
        print("Starting a new movies list!")
        movies_list = []

    print('Adding a movie...')
    nMovie = input('Enter the Movie name: >>> ')
    nDirector = input('Enter the Movie Director: >>> ')
    nWriter = input('Enter the Movie Writer: >>> ')
    nCast = input('Enter the Movie Cast: >>> ')
    nRating = input('Enter the Movie Rating: >>> ')
    nCopies = input('Enter the Movie Copies: >>> ')
    nYear = input('Enter the Movie Year of release: >>> ')
    movies_list.append([nMovie, nDirector, nWriter, nCast, nRating, nCopies, nYear])
    print(nMovie + " has been succesfully added to your movies.\n "
                           "Go to main menu and choose option 10 to display all movies")
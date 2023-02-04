from funct.new_movie import *

def delete1():
    delete1 = input("Select the Movie to delete: ")
    for movie in add_movie.movies:
        if movie.nMovie == delete1:
            add_movie.movies.remove(movie)
            print(f"{movie.nMovie} has been deleted successfully please check the remaining movies to confirm")
        else:
            print(f"there is no movie called {movie.nMovie} in the stock")
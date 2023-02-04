from funct.new_movie import *
def updateMovie():
    update1 = input("Which Movie do you want to Update: ")
    for movie in add_movie.movies:
        if movie.name == update1:
            set_name = input("Name: ")
            set_director = input("Director: ")
            set_writer = input("Writer: ")
            set_rating = input("Rating: ")
            set_copies = input("Copies: ")
            set_year = input("Year: ")
            add_movie.movies.update(set_name)
            add_movie.movies.update(set_director)
            add_movie.movies.update(set_writer)
            add_movie.movies.update(set_rating)
            add_movie.movies.update(set_copies)
            add_movie.movies.update(set_year)

            print("Movie after updating",add_movie.movies)
        else:
            print(f"there is no movie called {update1} in the stock")
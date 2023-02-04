from funct.new_movie import * 
def search():
  print("Checking movie availability...")
  movie_check = input("Enter the name of the movie: >>> ")
  for movie in add_movie.movies_list:
      if movie_check in movie:
          print("The movie" + movie[0] + " is available")
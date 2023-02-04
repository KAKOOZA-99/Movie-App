import funct.new_movie 
from funct.member import *
from funct.avail import *
from funct.update import *
import funct.delete
from funct.search import *


menu = ['Add New Movie', 
        'Rent out a Movie',
        'Check Movie Availabilty',
        'Search movie',
        'Movie Copies Available',
        'Add a Member',
        'Update a Movie',
        'Delete a Movie',
        'Display all Movies',
        'Quit']


print('\t===Movie App===\n')
pay = int(input("Please Enter 10k: "))

while True:
    print()
    print('       ******************MOVIE LIBRARY******************         ')
    print("******************WELCOME TO KENNETH MOVIE LIBRARY******************")
    print("-----------------------------USER------------------------------")
    print()
    #Loop thru out list of menu items
    print('Pick an option to continue')
    i=0  
    while i < len(menu):
        print('\t'+str(i)+'-'+menu[i])
        i+=1
    choice = input('Pick an operation to continue\n')
    
    try:
        choice = int(choice)
        if(choice>=len(menu)):
            print("Invalid selection, try again")

        elif choice == 0 and pay == 10000:
            add_movie()

        elif choice == 1 and pay == 10000:
            pass

        elif choice == 2 and pay == 10000:
            search()

        elif choice == 3 and pay == 10000:
            searchall()

        elif choice == 4 and pay == 10000:
            Name = input("Enter the Movie name to find the copies: ")
            for copy in add_movie.movies:
                if copy.name == Name:
                   if copy.copies > 0:
                       print("The movies available are:  {copy.copies}")
                   else:
                       print("All copies have been rented out")
                else:
                    print("Movie is not Available")

            
        elif choice == 5 and pay == 10000:
            new_member()

        elif choice == 6 and pay == 10000:
            updateMovie()

        elif choice == 7 and pay == 10000:
            funct.delete.delete1()

        elif choice == 8 and pay == 10000:
            for i in range(len(add_movie.movies_list)):
                print(add_movie.movies_list[i])

        elif choice == 9:
            break

        else:
            print("Please first pay the 10k")

    except Exception as e:
        print("Error Occured:",e)
        
print("You chose to quit, bye")
exit(0)
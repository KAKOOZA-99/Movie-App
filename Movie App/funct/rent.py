class Customer:
    rentedMovies = []
    def __init__(self):
        self.first_name = input("Enter customer's first name:"),
        self.last_name = input("Enter customer's last name"),
        self.middle_name = input("Enter customer'smiddle name"),
        self.user_name = input("Enter customer's name"),
        self.phone = input("Enter customer's phone number"),
        self.date_of_birth = input("Enter customer's date of birth")
        
    def __str__(self):
        return f"Customer(username:{self.user_name},contact: {self.phone})"
    
    def rent_movie(self, movie_name):
        self.rentedMovies.append(self.movie_name) 
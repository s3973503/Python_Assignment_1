''' Name :Prathiksha Chamarajanagar Padmaprasad
    student id:3973503
    The highest pasrt you have attempted:3
    No problem with the code
    Global lists {Declaring all the lists globally because we need to use them for one or more function}
    creating a dictionary to store the movie input given by the user becuase we 
    need to display the popular movie and also need to display all the movie type and how many 
    tickets have been sold for the particular movie.'''
customer_list = ['Mary', 'James']
customer_reward_program_list = ['Mary']
available_movies = dict(avatar=50, titanic=50, starwar=50)
availabale_ticket_types = dict(
    adult=25.0, child=19.5, senior=17.0, student=20.5, concession=20.5)#we chose dictionary instead of list to store both key and values togeteher.
purchase_details = {
    "avatar": {
        "overall_cost": 0,
        "type_n_quantity": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    },
    "titanic": {
        "overall_cost": 0,
        "type_n_quantity": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    },
    "starwar": {
        "overall_cost": 0,
        "type_n_quantity": {
            "adult": 0,
            "child": 0,
            "senior": 0,
            "student": 0,
            "concession": 0
        }
    }
}


# Function to display the main menu to choose from the below options to perform necessary actions.
def menu():
    print("""You can choose from the following option\n
            1:Purchase a ticket
            2:Add new movies
            3:Display existing customer information 
            4:Display exisiting movie information
            5:Display the most popular movie
            6:Display all movie records
            0: Exit the program""")
    print("####################################################################")
    operation = input("choose one option")
    return operation


# Asking customer to enter their name and take the input and return the value 
def get_name():
    customer_name = input("Enter the name of the customer [eg. Huong]:\n").capitalize()
    return customer_name


# Asking user to enter the movie name of thier choice from the movies that are already stored in the dictionary
def movie_choose():
    while True:
        print("Enter the name of the movie [enter a valid name only ,e.g. avatar,titanic,starwar]:")  
        movie = input()
        if movie in available_movies:
            return movie
        else:
            print("This is not a valid movie.Pleae enter a valid movie ")


# Asking the customer to choose  the ticket type which are already in dictionary
'''using while loop instead of for loop because 
    we are handling the invalid inputs from the user.It has run until the user gives valid input '''
'''strip and split functions are used because the input has been taken in the form of lists
    so to access indivisual input and check if the entered type is correct or not '''
def ticket():
    while True:
        ticket_type = input( "Enter the list of ticket type [e.g. adult,child,senior,student,concession]:").strip().split(",")
        returned_value = check_input(ticket_type)
        if returned_value == True:
            ticket_list = []
            for type in ticket_type:
                ticket_type = type.strip()
                ticket_list.append(ticket_type)
            return ticket_list
        elif returned_value == False:
            print("The ticket type is not valid \n Please Enter a valid ticket type")


# to check if the ticket type entered by the user is in the available ticket type dictonary 
def check_input(ticket_type):
    for type in ticket_type:
        type_of_ticket = type.strip()
        if type_of_ticket not in availabale_ticket_types:
            return False
    return True


# Asking the ticket quantity from the user
def quantity(movie, ticket_type):
    while True:
        print("Enter the list of ticket quantity")
        ticket_quantity = input().strip().split(",")
        return_value = check_quantity(ticket_quantity, movie, ticket_type)
        if return_value == True:
            quantity_list = []
            for quantity in ticket_quantity:
                ticket_q = int(quantity.strip())
                quantity_list.append(ticket_q)
            return quantity_list
        elif return_value == False:
            print("The ticket type is not valid")


# Handling error inputs from the user
def check_quantity(ticket_quantity, movie, ticket_type):
    ticket_quantity_number = []

    if len(ticket_quantity) != len(ticket_type):
        return False
    
    for quantity in ticket_quantity:
        try:
            if int(quantity) <= 0:
                return False
            ticket_quantity_number.append(int(quantity))
            if sum(ticket_quantity_number) > available_movies[movie]:
                print("The quantity must be less than number of available seats .please enter a smaller ticket quantity")
                print("Ticket Available: ", available_movies[movie])
                return False
        except ValueError:
            return False
    return True


# To check if the entered customer name is in rewardprogram list if not add the customer to the list if they want to join to the reward program else no action to be taken
def reward_program(name, reward_list):
    if name in reward_list:
        print("Customer is already in the rewards program list")
    else:
        while True:
            register_reward_program = input("The customer is not in the reward program.Does the customer wants to join the reward program?[enter y or n]")   
            if register_reward_program == 'y':
                customer_reward_program_list.append(name)
                customer_list.append(name)
                print("Sucessfully added the customer to the reward program")
                break
            elif register_reward_program == 'n':
                customer_list.append(name)
                break
            else:
                print("Please only enter y or n ")


# Calculation of total ticket cost
def total_ticket_cost(type_, quantity):
    result = []
    for t in type_:
        result.append(availabale_ticket_types[t])

    final_list = []
    for index in range(0, len(result)):
        final_list.append(result[index]*quantity[index])
    return sum(final_list)

# Calculation of booking fee
def booking_fee(quantity):
    return quantity * 2

# Calculation of discount fees
def discount_fee(total_ticket_cost, name):
    if name in customer_reward_program_list:
        return total_ticket_cost * 0.2
    else:
        return 0

# Calculation of total cost
def total_cost(total_ticket_cost, discount_fee, booking_fee):
    return total_ticket_cost - discount_fee + booking_fee

# Storing the user input details
'''Initializing the values inside the dictionay to zero to take the count of
   the purchase for that particular type '''
def type_n_quantity_function(type, quantity):
    result = {
        "adult": 0,
        "senior": 0,
        "student": 0,
        "child": 0,
        "concession": 0
    }

    for index in range(0, len(type)):
        result[type[index]] = quantity[index]

    return result


# Function to display the popular movie among all the movies.
def display_popular_movie():
    highest_purchased_movie_cost = 0
    highest_purchased_movie = ""
    for movie_name in purchase_details:
        if purchase_details[movie_name]["overall_cost"] > highest_purchased_movie_cost:
            highest_purchased_movie_cost = purchase_details[movie_name]["overall_cost"]
            highest_purchased_movie = movie_name

    print("Movie Name:", highest_purchased_movie,
          "Total Cost:", highest_purchased_movie_cost)


# Printing Customer Receipt
def print_values(customer_name, movie, ticket_type, ticket_quantity, discount, fees_for_booking, total):
    print("-------------------------------------------------")
    print("        Reciept of  ",              customer_name )
    print("--------------------------------------------------")
    print("movie:                ",            movie)

    for index in range(0, len(ticket_type)):
        print("Ticket Type:          ",     ticket_type[index])
        print("Ticket Unit Price:    ",     availabale_ticket_types[ticket_type[index]])
        print("Ticket quantity:      ",     ticket_quantity[index])
        if len(ticket_type) > 1:
            print("             ------                ")

    print("-----------------------------------------------------")
    print("discount:              ", discount)
    print("Booking fee            ", fees_for_booking)
    print("Total cost             ",  total)


'''Function to purchase a new ticket
calling all the function that needs to be exeuted to purchase the ticket'''
def ticket_purchase():
    customer_name = get_name()
    movie = movie_choose()
    ticket_type = ticket()
    ticket_quantity = quantity(movie, ticket_type)
    available_movies[movie] = available_movies[movie] - sum(ticket_quantity)
    reward_program(customer_name, customer_reward_program_list)
    ticket_cost = total_ticket_cost(ticket_type, ticket_quantity)
    fees_for_booking = booking_fee(sum(ticket_quantity))
    discount = discount_fee(ticket_cost, customer_name)
    total = total_cost(ticket_cost, discount, fees_for_booking)
    type_n_quantity_dic = type_n_quantity_function(
        ticket_type, ticket_quantity)
    purchase_details[movie] = {
        "overall_cost": purchase_details[movie]["overall_cost"]+total,
        "type_n_quantity": {
            "adult": purchase_details[movie]["type_n_quantity"]["adult"] + type_n_quantity_dic["adult"],
            "student": purchase_details[movie]["type_n_quantity"]["student"] + type_n_quantity_dic["student"],
            "concession": purchase_details[movie]["type_n_quantity"]["concession"] + type_n_quantity_dic["concession"],
            "senior": purchase_details[movie]["type_n_quantity"]["senior"] + type_n_quantity_dic["senior"],
            "child": purchase_details[movie]["type_n_quantity"]["child"] + type_n_quantity_dic["child"],
        }
    }
    print_values(customer_name, movie, ticket_type,
                 ticket_quantity, discount, fees_for_booking, total)


# To add new movies to the list of movies which is already present
def add_new_movies():
    while True:
        y_or_n = input("Do you want to add a list of movies  [enter y or n]")
        if y_or_n == "y":
            print("Enter the list of movies")
            movies_input = input().strip()
            movies_list = movies_input.split(",")
            for movies in movies_list:
                movies = movies.strip()
                if movies in available_movies:
                    print("Movie:", movies, "already exists")
                else:
                    available_movies[movies] = 50
                    purchase_details[movies] = {
                        "overall_cost": 0,
                        "type_n_quantity": {
                            "adult": 0,
                            "child": 0,
                            "senior": 0,
                            "student": 0,
                            "concession": 0
                        }
                    }
                    print("Movies Added:",movies )
            break
        elif y_or_n == "n": 
            break
    
           
            



# Displayinng the customer information
def customer_information():
    for customer in customer_list:
        if customer in customer_reward_program_list:
            print(customer, ": In Reward Program")
        else:
            print(customer, ": Not in Reward Program")


# Displaying the movie information
def movie_information():
    print(available_movies)


# To display all movie records
# Reference: https://www.geeksforgeeks.org/python-program-to-print-the-dictionary-in-table-format/
def display_all_movie_records():
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        '', 'adult', 'child', 'senior', 'student', 'concession', 'Revenue'))
    for movie in purchase_details.keys():
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(movie, purchase_details[movie]["type_n_quantity"]["adult"],
                                                                        purchase_details[movie]["type_n_quantity"]["child"], purchase_details[movie][
                                                                            "type_n_quantity"]["senior"], purchase_details[movie]["type_n_quantity"]["student"],
                                                                        purchase_details[movie]["type_n_quantity"]["concession"], purchase_details[movie]["overall_cost"]))
        
# Program main function
if __name__ == "__main__":
    print("welcome to RMIT Ticketing sysytem!")
    print("######################################################################")

    while True:
        operation = menu()
        if operation == "1":
            ticket_purchase()
        if operation == "2":
            add_new_movies()
        if operation == "3":
            customer_information()
        if operation == "4":
            movie_information()
        if operation == "5":
            display_popular_movie()
        if operation == "6":
            display_all_movie_records()
        if operation == "0":
            print("Thank you for visiting RMIT Ticketing system")
            exit
            break


'''My Analysis/Reflection:
The first step of any program is to read the problem statement ,
understand the requirements say inputs of the program and the expected output.
Then break the problem statement into smaller pices and try to solve it one by one.

After gathering all the requirements I started writing a code part by part .
Initailly i started with Part A  which was just basic operations to take input and
perform some calculations and displaying the output.Likewise I moved on to next part. 
Part 2 was initially easy with handling the errorinputs moving on while taking the list of 
inputs from the user I was stuck a bit while stripping and spiltting. I dimt give up.
I watched all the lectures,practical videos to understand the concep better and try using 
it again and finally suceeded.Later on the third part, I had not created the purchase deatils 
dictyonary in fisrt place i created while doing the part 3. I felt part 3 was most difficult among all
I spent almost 2 days trying all the features and fixing all the errors.

Once the program is fully built,I noted down all the values that needs to be tested and tested all the inputs and outputs 
aacordingly.Meanwhile commented the whole program and finally wrote this analysis. '''
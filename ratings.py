"""Restaurant rating lister."""

# import argv from sys

def create_dictionary(filename):

    open_file=open(filename)

    restaurants_and_ratings={}

    for line in open_file: #adds the data from the file to our dictionary. 

        line=line.rstrip()

        restaurant,rating=line.split(':')
        
        restaurants_and_ratings[restaurant]=restaurants_and_ratings.get(restaurant, rating)

    open_file.close()

    return restaurants_and_ratings

    
    

def sort_restaurants_alphad(dictionary):

    alphad_restaurant_list=sorted([restaurant for restaurant in dictionary.items()])

    return alphad_restaurant_list


def print_restaurants_ratings(list):

    for restaurant, rating in list:

        print(f"{restaurant} is rated at {rating}.")

# print_restaurants_ratings(sort_restaurants_alphad(create_dictionary('scores.txt')))

def take_user_input(dictionary):

    user_restaurant=input("What restaurant are you rating? > ")

    user_rating=input(f"What rating are you giving {user_restaurant}? > ")

    dictionary[user_restaurant]=dictionary.get(user_restaurant, user_rating)

    return dictionary
    
def run_program(filename):
    print_restaurants_ratings(sort_restaurants_alphad(create_dictionary(filename)))

    restaurants_and_ratings=create_dictionary(filename)

    useradded_restaurants_and_ratings=take_user_input(restaurants_and_ratings)

    print('\nYour rating has been added.\n')

    print_restaurants_ratings(sort_restaurants_alphad(useradded_restaurants_and_ratings))
    

run_program('scores.txt')

places = ['Atlanta', 'Washington D.C.', 'New York City', 'Austin', 'Boston', 'Seattle', 'Los Angeles']

restaurants = ['Chick-fil-a', 'Poké Bar', 'Dominoes', 'Burger King', 'Zaxbys', 'Panda Express', 'Taco Bell']

mode_of_transportation = ['Private Car', 'Bus', 'Subway', 'Helicopter', 'Airplane', 'Limousine', 'Taxi']

entertainments = ['Karaoke', 'Movies', 'Top Golf', 'Bowling', 'Arcade', 'Concert', 'Muesum', 'Festival']

import random
valid_response = False
def get_destination():
    destination = random.choice(places)
    return destination

def get_restaurant():
    restaurant = random.choice(restaurants)
    return restaurant

def get_transportation():
    transportation = random.choice(mode_of_transportation)
    return transportation

def get_entertainment():
    entertainment = random.choice(entertainments)
    return entertainment

def run_day_trip_generator():
    destination = get_destination()
    print("Destination:",destination)
    restaurant = get_restaurant()
    print("Restaurant:",restaurant)
    transportation = get_transportation()
    print("Transporation:",transportation)
    entertainment = get_entertainment()
    print("Entertainment:",entertainment)
    while valid_response == False:
        satisfaction = input("Are you satisfied with your trip? Y or N ")
        if satisfaction == "N":
            user_input = input("Which option would you like to change? Destination, Restaurant, Transportation, or Entertainment? ")
            if user_input == "Destination":
                destination = get_destination()
                print("Destination:",destination)
                print("Restaurant:",restaurant)
                print("Transportation:",transportation)
                print("Entertainment:",entertainment)
            elif user_input == "Restaurant":
                restaurant = get_restaurant()
                print("Destination:",destination)
                print("Restaurant:",restaurant)
                print("Transportation:",transportation)
                print("Entertainment:",entertainment)
            elif user_input == "Transportation":
                transportation = get_transportation()
                print("Destination:",destination)
                print("Restaurant:",restaurant)
                print("Transportation:",transportation)
                print("Entertainment:",entertainment)
            elif user_input == "Entertainment":
                 entertainment = get_entertainment()
                 print("Destination:",destination)
                 print("Restaurant:",restaurant)
                 print("Transportation:",transportation)
                 print("Entertainment:",entertainment)
            else:
                print("I do not understand, please try again")
        elif satisfaction == "Y":
            print("Here if your final trip!")
            print("Destination:",destination)
            print("Restaurant:",restaurant)
            print("Transportation:",transportation)
            print("Entertainment:",entertainment)
            break
        else:
            print("Please type in Y or N. ")
       
run_day_trip_generator()


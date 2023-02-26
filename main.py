#Creating lists
places = ['Atlanta', 'Washington D.C.', 'New York City', 'Austin', 'Boston', 'Seattle', 'Los Angeles']
# print(place)

restaurants = ['Chick-fil-a', 'Poké Bar', 'Dominoes', 'Burger King', 'Zaxbys', 'Panda Express', 'Taco Bell']
# print(restaurants)

mode_of_transportation = ['Private Car', 'Bus', 'Subway', 'Helicopter', 'Airplane', 'Limousine', 'Taxi']
# print(mode_of_transportation)

entertainments = ['Karaoke', 'Movies', 'Top Golf', 'Bowling', 'Arcade', 'Concert', 'Muesum', 'Festival']
# print(entertainment)

import random

def get_destination():
    destination = random.choice(places)
    return destination

# destination = get_destination()
# # print("Destination:",destination)

def get_restaurant():
    restaurant = random.choice(restaurants)
    return restaurant

# restaurant = get_restaurant()
# # print("Restaurant:",restaurant)

def get_transporation():
    transporation = random.choice(mode_of_transportation)
    return transporation

# transporation = get_transporation()
# # print("Transporation:",transporation)

def get_entertainment():
    entertainment = random.choice(entertainments)
    return entertainment

# entertainment = get_entertainment()
# # print("Entertainment:",entertainment)

def run_day_trip_generator():
    destination = get_destination()
    print("Destination:",destination)
    restaurant = get_restaurant()
    print("Restaurant:",restaurant)
    transporation = get_transporation()
    print("Transporation:",transporation)
    entertainment = get_entertainment()
    print("Entertainment:",entertainment)

run_day_trip_generator()

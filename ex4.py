cars = 100                                                  # the number of cars
space_in_a_car = 4.0                                        # how many passengers can fit in a car
drivers = 30                                                # the number of drivers
passengers = 90                                             # the number of passengers
cars_not_driven = cars - drivers                            # the number of cars that are not driven
cars_driven = drivers                                       # the number of cars driven
carpool_capacity = cars_driven * space_in_a_car             # how many passengers can we carry
average_passengers_per_car = passengers / cars_driven       # the number of possible passengers per driven car

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

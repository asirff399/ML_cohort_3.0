# Video 9-10 Task 2: Tuples
# Write a program that:

# 1. Creates a tuple with the names of 5 cities.
city = ('Dhaka','Rajshahi','Khulna','Sylhet','Chattogram')

# 2. Prints the third city in the tuple.
print(city[2])

# 3. Converts the tuple into a list, adds a new city, and converts it back to a tuple.
city_list = list(city)
city_list.append('Barisal')
city_tuple = tuple(city_list)

# 4. Prints the modified tuple.
print(city_tuple)

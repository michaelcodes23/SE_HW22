# Exercise 1
# Create a list named students containing some student names (strings).
student_names = ['Michael', 'Jorge', 'Peiyi']
# Print out the second student's name.
print(student_names[1])
# Print out the last student's name.
print(student_names[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods 
# (strings) as there are names in the students list.
foods = 'pizza','gelato','sushi'
# Use a for loop to print out the string "food goes here is a good food".
for food_item in (foods):
    print(f'{food_item} is a good food')

'''
Exercise 3
Using a for loop, print just the last two food strings from foods.
'''
two = 2 

for food_item in (foods):
    if(two >= 1):
        print(foods[two])
        two -= 1

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
home_town = {
    "city": "NYC",
    "state": "New York",
    "population": "8.4MM"
}
# Print a string with this format:
# "I was born in city, state - population of population"
print(f'I live in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"
for key,val in home_town.items():
    print(f'{key} = {val}')

# Exercise 6
# Create an empty list named cohort.
cohort = []
# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#  	'student': 'Tina',
#  	'fav_food' 'Cheeseburger'
#  }
num = 0
for student in student_names:
    cohort.append({
        'student': student,
        'fav_food': foods[num]
    })
    num += 1
# Iterate over cohort printing out each element.
for item in cohort:
    print(item)

# Exercise 7
# Using the list of students and list comprehension, assign to a variable 
# named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
awesome_students = [f'{student} is aweomse!' for student in student_names]
# Iterate over awesome_students printing out each string.
for string in awesome_students:
    print(string)
# Exercise 8
# Using the tuple foods and list comprehension within a for loop, 
a_foods = [food_item for food_item in foods if'a' in food_item]
# print each food string that contains the letter a.
print(f"{a_foods} include the letter 'a' in the food name")
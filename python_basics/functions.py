#functions,parameter,arguments,the return statement

def trip_welcome():
   print("Welcome to TripApp!")
   print("Let's get you to your destination.")

print('Hello world!')
trip_welcome()

#functions,Positional arguments
def purple_pets(breed):
    print("Welcome to PurplePets!")
    print("Let's help you find the pets you will adore forever! A "+ breed+ " that completes you! Adopt a pet Today!")
purple_pets('Poodle')

def calculate_uber_ride(miles_to_travel,rate,discount):
    print(miles_to_travel * rate - discount)
calculate_uber_ride(30,1.0,10)

#functions,Keyword arguments     still has to be understood and worked on
# def calculate_uber_ride():
#     print(miles_to_travel * rate - discount)
# calculate_uber_ride(miles_to_travel=30,rate=1.0,discount=10)

#default arguments
def calculate_uber_ride(miles_to_travel,rate,discount=10):
    print(miles_to_travel * rate - discount)
calculate_uber_ride(30,1.0,5)

#Return statements
def calculate_exchange_usd(us_dollars,exchange_rate):
     return us_dollars * exchange_rate
naira_exchange = calculate_exchange_usd(1000,610)

print("1000 American dollars would give you "+ str(naira_exchange) + "Naira in Nigerian Currency")#a returned function value

#Multiple returns
food_timetable = ['pap and akara','beans and custard','bread and egg']
def threeday_food_timetable(food_timetable):
    first_day = "Breakfast for saturday will be "+ food_timetable[0]
    second_day="Breakfast for sunday will be "+ food_timetable[1]
    third_day="Breakfast for monday will be "+ food_timetable[2]
    return first_day,second_day,third_day
saturday,sunday,monday = threeday_food_timetable(food_timetable)
print(saturday)
print(sunday)
print(monday)

#assignment on functions
def max_of_two( x, y ):
    if x > y:
       return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(6, 10, -5))

#Python program to find the maximum number among any three input numbers from user using functions.

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

def max_num_1( x, y ):
    if x > y:
        return x
    return y
def max_num( x, y, z ):
    return max_num_1( x, max_num_1( y, z ) )
print(max_num(x,y,z))



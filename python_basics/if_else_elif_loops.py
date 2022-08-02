#Conditional/Decision-making Statements: IF, ELSE, ELIF. 
# IF Statement   
num = 5
if num > 2:
    print(num,"is equal and accurate.")
    print(num,"is GREATER THAN 2!")


#ELSE Statement
num =5
if num < 2:
    print(num,"is correct!")
else:
    print(num,"is not correct!")

#ELIF Statement
num = 5
if num < 2:
    print(num,"accurate or Accurate")
elif num > 2:
    print(num,"Definitely Accurate!")
else:
    print(num,"not correct!")


# LOOPS
#While loops

count=0
while(count<9):
    print('The count is:',count)
    count = count+1
    print("Goodbye!")

#A single statement while block
count =0
while(count ==0):print("Hello Geek") #A while loop can become an infinite loop if a condition never becomes false.

#For loops
#Syntax: for iterating_var in sequence: statement(s)
for letter in 'Awonaike':
   print("Current Letter:",letter) 

#Loop control statement
# Break Statement
for letter in 'Awonaike':
    if letter =='o' or letter =='i':
        break
print("Current Letter:",letter)

#Continue Statement
for letter in 'Awonaike':
    if letter =='o' or letter =='i':
        continue
print("Current Letter:",letter)

#Pass Statement
#An empty loop
for letter in 'Awonaike':
    pass





#Creating a dictionary called menu
menu ={'Avcocado toast':6,'Orange Juice':5,'Chocolate muffin':3}
#to add a single key:value pair to a dictionary, use this syntax
#dictionary[key]=value
menu['Popcorn'] = 2
#to add multiple keys:value pairs to a dictionary at once, you can use update() method
menu.update({'Icecream':10,'Watermelons':3,'Walnuts':1})
print(menu)

person ={"Name":"Tawakalt","Age":19,"Family":["Lawal","Awonaike"]}
print(person)

#Dictionary Comprehensiondents 
#wanting to combine two list into a dictionary, like list of students and their heights in inches
names = ['Shola','Tawa','Dara','Yeye']
heights = [61,70,63,64]
students ={key:value for key, value in zip(names,heights)}
print(students)
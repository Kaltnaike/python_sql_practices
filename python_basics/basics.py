#This is a python hello world program
print("Hello World!")

#Create a multi-line string
multi_line= """
This is a multi line string
"""
print(multi_line)

#declare variable
greeting="Hello T-baby Sexy"
print(greeting)

#data types
x=23
y=20.5
z="tawa"
a=1j
b=None
c=["love","pain","death"]
d={"love","pain","death"}
e=("love","pain","death")
f=True

print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#creating a list
beautyprep =['cream','cream','hairspray','sunscreen','hairoil','facial scrub']
list_len= len(beautyprep)
print(list_len)

beautyprep.append('hairbrush')
print(beautyprep)

beautyprep2 = ['hairgel','shavingstick','jewellries']
beautyprep.extend(beautyprep2)
print(beautyprep)

beautyprep.insert(3,'scarfs')
print(beautyprep)

beautyprep.remove('cream')
print(beautyprep)

beautyprep.pop(2)
print(beautyprep)

beautyprep.clear()
print(beautyprep)

index_=beautyprep.index('cream')
print(index_)

beautyprep.reverse()
print(beautyprep)

beautyprep.sort()
print(beautyprep)

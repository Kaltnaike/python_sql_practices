#manipulating files in python using "with" keyword context manager
with open('cool_document.txt') as cool_doc:
    fileContents = cool_doc.read()
print(fileContents);

#to read file line by line
with open('cool_document.txt') as cool_doc:
    for line in cool_doc.readlines(): 
     print(line);

#writing a file
with open('created_file.txt','w') as created_doc:
    created_doc.write('Here is the content for the new file')

#appending to a file
with open('created_file.txt','a') as created_doc:
    created_doc.write('Everything and Anything can be here')
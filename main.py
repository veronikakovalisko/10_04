'''
Task 1
Files
Write a script that creates a new output file called myfile.txt and writes the string "Hello file world!" in it.
Then write another script that opens myfile.txt, and reads and prints its contents.
Run your two scripts from the system command line.
Does the new file show up in the directory where you ran your scripts?
What if you add a different directory path to the filename passed to open?
Note: file write methods do not add newline characters to your strings;
add an explicit ‘\n’ at the end of the string if you want to fully terminate the line in the file.
'''
if __name__ == '__main__':
    my_file = open('my_file', 'w')
    my_file.write("Hello file world!")
    my_file.close()
    f = open('my_file', 'r')
    print(f.read())
    f.close()
    #TODO: доробити завдання з json

'''Task 2

Extend Phonebook application

Functionality of Phonebook application:

Add new entries 
Search by first name 
Search by last name 
Search by full name
Search by telephone number
Search by city or state
Delete a record for a given telephone number
Update a record for a given telephone number
An option to exit the program
 

The first argument to the application should be the name of the phonebook. Application should load JSON data, if it is present in the folder with application, else raise an error. After the user exits, all data should be saved to loaded JSON.

 '''
import json
class Phonebook:
    def __init__(self, name: str):
        self.persons = []
        self.name = name

    def addperson(self, person: "Person"):
        self.persons.append(person)
    def foundbyname(self, name):
        for i in self.persons:
             if i.name == name:
                 return i.name
    def addbylastname(self, lastname):
        for i in self.persons:
            if i.lastname == lastname:
                b = []
                b.append(i)
        return f'in this phonebook are {len(b)} people with lastname {lastname} this is return {b}'
    def addbynameandlastname(self, name, lastname):
        for i in self.persons:
             if i.name == name and i.lastname == lastname:
                 return f"Number of {i.name} {i.lastname} is {i.number}"
    def foundbynumber(self,number):
        for i in self.persons:
            if i.number == number:
                return f"this is number by {i.name} {i.lastname}"

class Person:
    def __init__(self, name, lastname, number):
        self.lastname = lastname
        self.number = number
        self.name = name


ppl = Person('ann', "franz", 125)
ph1 = Phonebook('ph1')
ph1.addperson(ppl)
print(ph1.foundbynumber(125))

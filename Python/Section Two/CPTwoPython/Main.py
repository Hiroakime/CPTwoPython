#Exercise 1
"""Width = float (input("Enter the value of width: "))
Length = float (input("Enter the value of length: "))

Area = Width * Length
print("The area of the rectangle is:", Area)"""

#Exercise 2
"""item = str (input("What item would you like to buy?"))
price = float (input("What is the price of theitem?"))
quantity = int (input("How many of this are you going to buy?"))

print("the price of", item, "is:", price)
print("the quantity of", item, "is:", quantity)

total = price * quantity
print("The total cost of", item, "is:", total)"""

""""age = int (input("What is your age?"))
Student = input("Are you a student? [y/n]")

if age <= 12 and Student == "y" or "Y":
    print("You are a child.")
    print("You are a student.")
elif age <= 12 and not Student == "y" or "Y":
    print("You are a child.")
    print("You are not a student.")
elif age > 12 and age <= 19 and Student == "y" or "Y":
    print("You are a teenager.")
    print("You are a student.")    
else:
    print("You are an adult.")
    print("Dm me shawty.")"""
    
'''number = 67

result = "Positive" if number > 0 else "Negative"

print(f"result: {result}")'''

#Example 2
'''numberOne = int (input("Enter the first number: "))
numberTwo = int (input("Enter the second number: "))

result = numberOne if numberOne < numberTwo else numberTwo

print(f"The result is: {result}")'''

#Example 3
#text = input("Enter a word: ")

#result = text.find("p")
#result = text.rfind("p")
#result = text.capitalize()
#result = text.upper()
#result = text.isdigit()
#result = text.isalpha()
#result = text.count()
#result = text.replace("p", "n")
#result = text.lower()
#print (result)

'''Username = input("Enter your username: ")

UserInput = Username.isalpha()
UserInput = Username.count(Username)
UserInput = Username.find(" ")
UserInput = len(Username)

if len(Username) <= 12 and Username.isalpha() == True:
    print(f"Your username is valid. Welcome {Username}.")
else:
    print("Your username is invalid. Please enter a valid username with only 12 characters or less and only alphabetic characters.")
    
if Username.find(" ") != -1:
    print("Your username is invalid. Please enter a valid username without spaces.")'''

'''if UserInput == True:
    print("Your username is valid.")
else:
    print("Your username is invalid. Please enter a valid username.")
    
UserInput = Username.count(12)
if UserInput == 12:
    print("Your username is valid.")
else: UserInput > 12:
    print("Your username is invalid. Please enter a valid username.")'''
    
'''ccnum = "1267-2456-7674-9672"

ccnum1 = ccnum[15:]
print(f"Credit card number: xxxx-xxxx-xxxx{ccnum1}")

rchar = ccnum[18:-1]
print(f"Credit card number in reverse: {rchar}")'''

#EXample
'''username = input("Enter your username: ")

while username = "";
    print ("Your username is invalid. Please enter a valid username.")
    username = input("Enter your username: ")

print(f"Your username is valid. Welcome {username}.")'''

'''number = int (input("Enter a number: "))

while number < 1 or number > 20:
    if number < 1:
        print("Your number should not be lower than 1.")
        number = int (input("Enter a number: "))
    elif number > 20:
        print("Your number should not be higher than 20.")
        number = int (input("Enter a number: "))
    else:
        print(f"Number is {number}.")'''

'''favfood = input("What is your favorite food(enter q to quit)? ")

while not favfood == "q":
    print(f"Your favorite food is {favfood}.")
    favfood = input("What is your favorite food(enter q to quit)? ")

print("thank you for giving your favorite food!")'''

'''for x in range(1, 10):
    if x == 5:
        break
    else:
        print(x)'''

#Example List

'''fruits = ["apple", "orange", "banana", "coconut"]
fruits.append("pineapple")'''

#list on while loop
'''index = 0
while index <len(fruits):
    print(fruits[index])'''

'''for x in range(len(fruits)):
    print(f"fruit: {fruits[x]}")
    
for x in fruits:
    print(f"fruit: {x}")'''

#example

'''def addition(num1, num2):
    sum = num1 + num2
    print(sum)
    
addition(50, 50)'''

'''def info(name, age, country):
    print(name)
    print(age)
    print(country)

info("Bucalabels", 67, "Iran")'''

class Students:

    def __init__(self, name, course, gpa):
        self.name = name
        self.course = course
        self.gpa = gpa

student1 = Students("John", "BSIS", 3.8)
student2 = Students("Robert", "BSCS", 3.5)
student3 = Students("Bucala", "BSCS", 3.9)

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

Username = input("Enter your username: ")

UserInput = Username.isalpha()
UserInput = Username.count(Username)
UserInput = Username.find(" ")
UserInput = len(Username)

if len(Username) <= 12 and Username.isalpha() == True:
    print(f"Your username is valid. Welcome {Username}.")
else:
    print("Your username is invalid. Please enter a valid username with only 12 characters or less and only alphabetic characters.")
    
if Username.find(" ") != -1:
    print("Your username is invalid. Please enter a valid username without spaces.")


    


'''if UserInput == True:
    print("Your username is valid.")
else:
    print("Your username is invalid. Please enter a valid username.")
    
UserInput = Username.count(12)
if UserInput == 12:
    print("Your username is valid.")
else: UserInput > 12:
    print("Your username is invalid. Please enter a valid username.")'''
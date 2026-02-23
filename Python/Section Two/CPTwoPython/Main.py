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

age = int (input("What is your age?"))
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
    print("Dm me shawty.")
#Activity Week 11

#Question One
class Q1:
    Test_Data = [10, 15, 20, 30]

    @classmethod
    def run_code(cls):
        avg = sum(cls.Test_Data) / len(cls.Test_Data)
        print(f"List values: {cls.Test_Data}")
        print(f"The average of {cls.Test_Data} is: {avg}")

def ActivityWeekEleven():
    qOne = Q1()
    qOne.run_code()

if __name__ == "__main__":
    ActivityWeekEleven()

 
#Question Two
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Q2:
    def __init__(self):
        self.new_person = []
    
    def run_code(self):
        self.new_person.append(Person("Kurt", 15))
        self.new_person.append(Person("Carl", 23))
        self.new_person.append(Person("Jk", 45))
        self.new_person.append(Person("James", 60))
        self.new_person.append(Person("Kelvin", 39))
        self.new_person.append(Person("Haze", 18))
        self.new_person.append(Person("Gaze", 10))
        self.new_person.append(Person("Soap", 20))
        self.new_person.append(Person("Price", 23))
        self.new_person.append(Person("McQueen", 80))
        self.new_person.append(Person("Bascreveil", 50))

        age_input = input("Enter an age: ")
        age_limit = int(age_input)

        print(f"People with lower age than {age_limit}: ")
        for p in self.new_person:
            if p.age < age_limit:
                print(f"Name: {p.name}, Age: {p.age}")

def ActivityWeekEleven():
    qOne = Q2()
    qOne.run_code()

if __name__ == "__main__":
    ActivityWeekEleven()

#Question Three

class Q3:
    list1 = [1, 20, 3, 6, 8, 9, 10, 7, 12, 21, 18]
    list2 = [10, 2, 30, 15, 8, 21, 13, 18, 28, 25, 16]
    
def same_numbers(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    same = set1.intersection(set2)

    print(f"List One: {list1}")
    print(f"List Two: {list2}")

    print(f"All same numbers on both lists: {same}")

def ActivityWeekEleven():
    qthree = Q3()
    same_numbers(qthree.list1, qthree.list2)

if __name__ == "__main__":
    ActivityWeekEleven()



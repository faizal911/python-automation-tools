# print("hello i am 45 faizal pathan")
# name = "faizal pathan"
# print(name)
# age=4.5
# print(age)
# hello=True
# print(hello)

# print(type("faizal pathan"))
# print(type(4.5))
# print(type(True))

# name = "faizal pathan"
# age =20

# print(f"my name is {name} and i am {age},years old")
# print("my name is ", name,"and i am ",age,"years old")

# age = 20      
# age = "20"    


# name= "faizal pathan"
# age= 20
# gpa= "8.5"
# Currently_studying= True


# print(f"name: {name}")
# print(f"age: {age}")
# print(f"gpa: {gpa}")
# print(f"Currently_studying:{Currently_studying}")

# a=10
# b=3

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


# first="faizal"
# last="pathan"

# full_name =first +" "+last
# print(full_name)

# line ="-"*20
# print(line)


# name ="faizal pathan is a good boy. hello"

# print(name.upper())
# print(name.capitalize())
# print(name.replace("faizal","faiz"))
# print(len(name))

# name =input("enter your name")
# age = int(input("enter your age:"))
# print(f"hello {name}")
# print(f"you are {age} years old .")



# a=int(input("enter first number: "))
# b=int(input("enter second number: "))

# print(f"sum: {a+b}")
# print(f"difference: {a-b}")
# print(f"product: {a*b}")

# score =int(input("enter your score : "))

# if score>=90:
#     print ("grade: A")
# elif score>=80:
#     print("grade: B")
# elif score>=60:
#     print ("grade: C")
# else:
#     print("grade: D")


# correct_username="faizal"
# correct_password="123"
# a=input("enter your username: ")

# if a==correct_username:
#     b=input("enter your password: ")
#     if b== correct_password:
#         print("access granted . welcome faizal")
#     else:
#         print("wrong password.")
# else:
#     print("user not found ")



# for i in range(100,0,-1):
#     print(i)


# count =1
# while count<=100000:
#     print(count)
#     count +=1

# n= int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")


# age =int(input("enter you age:"))

# if age>=18:
#     print("you can vote!")
# else:
#     print("too young to vote")


# import random

# secret = random.randint(1, 100)
# attempts = 0

# print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# while True:
#     guess = int(input("Your guess: "))
#     attempts += 1

#     if guess < secret:
#         print("Too low! Try higher.")
#     elif guess > secret:
#         print("Too high! Try lower.")
#     else:
#         print(f"Correct! You got it in {attempts} attempts!")
#         break


# import random

# def play_game():
#     secret = random.randint(1, 100)
#     attempts = 0
#     max_attempts = 10

#     print("\nWelcome to the Number Guessing Game!")
#     print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

#     while attempts < max_attempts:
#         guess = int(input("Your guess: "))
#         attempts += 1
#         remaining = max_attempts - attempts

#         if guess < secret:
#             print(f"Too low! {remaining} attempts left.")
#         elif guess > secret:
#             print(f"Too high! {remaining} attempts left.")
#         else:
#             print(f"Correct! You got it in {attempts} attempts! 🎉")
#             return

#     print(f"Game over! The number was {secret}.")

# while True:
#     play_game()
#     again = input("\nPlay again? (yes/no): ")
#     if again.lower() != "yes":
#         print("Thanks for playing. Goodbye!")
#         break



# fruits = ["apple", "banana", "mango"]
# numbers =[10,20,30,40,50]
# mixed = ["faizal", 20, True, 8.5]

# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# numbers = [10,20,30,40,50]

# print(numbers[::-1])

# name ="faizal pathan"
# print(name[1:4])


# fruit = ["apple", "banana", "mango"]

# fruit[1]= "pineapple"
# print(fruit)

# fruit.append("orange")
# print(fruit)

# fruit.remove("apple")
# print(fruit)

# fruit.pop()
# print(fruit)

# fruit.insert(1,"kiwi")
# print(fruit)

# numbers =[30,10,50,40,20]

# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sorted(numbers))

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)



# names = ["faizal", "ali", "sara","mohit"]

# for e in names:
#     print(f"hello, how are you all ,{e}!")


# fruits =["apple", "banana", "mango"]

# if "banana" in fruits:
#     print("found it")

# if "grapes" not in fruits:
#     print("grapes not found")    


# students = ["faizal", "ali", "sara","mohit"]

# print(students[0])
# print(students[3])

# students.append("rehan")
# print(students)

# students.insert(4,"rehan")
# print(students)

# students.remove("ali")
# print(students)

# print(students)

# print(len(students))



# cities = ["Delhi", "Jaipur", "Mumbai", "Chennai", "Kolkata"]
# print(cities[2:])
# print(cities[:2])


# student ={
#     "name":"faizal pathan",
#     "age":20,
#     "city":"jaipur",
#     "gpa":8.5
# }

# print(student["name"])
# print(student["age"])
# print(student["city"])
# print(student["gpa"])

# student["course"] = "BCA"
# print(student["course"])

# student["age"]=21
# print(student["age"])

# del student["gpa"]
# course = student.pop("course")
# print(course)


# students = {"name":"faizal pathan","age":20,"city":"jaipur"}

# for key in students:
#     print(key)

# for value in students.values():
#     print(value)

# for key, value in students.items():
#     print(f"{key}:{value}")


# contacts = {
#     "Faizal": "9461376369",
#     "Ali":    "9876543210",
#     "Sara":   "9123456789"
# }

# print("--- Phone Book ---")
# for name, phone in contacts.items():
#     print(f"{name}: {phone}")

# search = input("\nSearch contact: ")

# if search in contacts:
#     print(f"{search}'s number is {contacts[search]}")
# else:
#     print("Contact not found")


# def greet(name):
#     print(f"hello,{name}!")

# greet("faizal pathan")
# greet("ali")
# greet("rehan")    


# def add(a,b):
#     print(a+b)

# add(10,5)
# add(100,25)  



# def add(a,b):
#     return a+b

# def is_even(n):
#     return n%2==0

# def greet(name,city):
#     return f"hello {name} , welcomr from {city}!"

# print(f"Sum: {add(10, 5)}")
# print(f"Is 10 even? {is_even(10)}")
# print(f"Is 7 even? {is_even(7)}")
# print(greet("Faizal", "Jaipur"))















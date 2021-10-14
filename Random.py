#To create random numbers with Python code you can use the random module.
# To use it, simply type:

#import random

#This module has a several functions the most important one is just named random().
#The random() function generates a floating point number between 0 and 1 [0.0,1.0]

#The random module has pseudorandom number generators, this means they are not truly random.

#GENERATE RANDOM NUMBERS
#This example creates several random numbers. Type the program shown below and run it:

import random
#Create a random floating point number and print it.
print(random.random())

#pick a random whole number between 0 and 10
print(random.randrange(0,10))

#pick a random floating point number between 0 and 10
print(random.uniform(0,10))

#In alll of the cases we use the random module. Several random numbers are generated.
#If you want a random float betweeen 1 and 10 you can use this trick:

x = random.uniform(1,10)
print(x)

#For random integers either case them to integers or use the randrange function

#STUDY DRILL

#1. Make a program that creates a random number and stores it into x
x = random.uniform(1,10)
print(x)

#2. Make a program that prints 3 random numbers
number = 0
while number < 3:
    x = random.uniform(1, 10)
    print(x)
    number = number + 1

#3. Create a program that generates 100 random numbers and find frequency of each number
Fre = []
i = 0
while i < 99:
    x = random.randrange(0, 99)
    Fre.append(x)
    i = i + 1

print(Fre)

Freu = set(Fre) #Create a new list the principal and the only numbers

print(Freu) #List that the elements do not repeat

Repeat = []

for x in Freu:
    if (Fre.count(x)>1):
        Repeat.append(x)

print(Repeat)
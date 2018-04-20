from random import *

print("-----Guess your number game-----")
input("Now you think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")

print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller than your number")
print("'l' if my guess if 'L'arger than your number")

loop = True

n = randint(0,100)
print("Is ", n, "your number?", end =" ")

while loop:

    c = randint(0,n)
    d = randint(n,100)

    a = input()

    if a == 'c':
        print("Hura - I did it")
        loop = False

    elif a == 's':
        print("Is ", c, "your number?", end =" ")

    elif a == 'l':
        print("Is ", d, "your number?", end =" ")

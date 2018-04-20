from random import randint
print("guest my number?")
n = randint(0,100)
print(n)
wrong_cout=0
loop = True
while loop:
    x=int(input("what is your number?"))
    if x == n:
        print("bingo")
        loop = False
    elif n > x:
        print("x lon hon")
        wrong_cout +=1
    else:
        print("x be hon")
        wrong_cout +=1

        if wrong_cout > 3:
            loop = False

number = [1 ,2 ,3 ,4 , 5 , 6 , 7 , 8 , 9]
a = 0
b = int(input("Input a number: "))
for i in range(len(numbers)):

    if numbers[i] == b:
        a += 1

message=''' {0} appears {1} in my list'''.format(b, a)
print(message)

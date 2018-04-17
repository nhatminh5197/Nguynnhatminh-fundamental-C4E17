list = ["T-shirt","sweater"]

while True:
    option = input("what do you want (C, R, U, D)?")


    if option == "R":
        print(*list,sep=",")
    elif option == "C":
        creat = input("Enter new item:")
        list.append(creat)
        print(*list, sep=",")
    elif option == "U":
        position = int(input("Update position?"))
        new_item = input("New item:")
        list[position-1] = new_item
        print(*list,sep=",")
    elif option == "D":
        D_position = input("Delete position?")
        list.append(D_position)
        print(*list,sep=",")
    else:
        print("no information!")

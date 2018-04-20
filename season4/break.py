loop = True
wrong_cout=0
while True:
    print("welcome to superuser gateway!")
    username = input("Enter username:")
    password = getpass("Enter password:")

    if username != "c4e":
        print("No such user")
        wrong_count +=1
    else:
        if password != "codethechange":
            print("wrong password")
            wrong_cout +=1
        else:
            print("welcome, c4e")
            loop = False

            if wrong_cout > 3:
                loop = False

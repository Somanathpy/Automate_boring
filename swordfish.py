while True:
    name = input("Enter your Name: ")
    if name != 'Som':
        continue
    print("hello, Som. what is the Password? ( Its a fish)")
    password = input()
    if password == 'swordfish':
        print("Access has been granted!!")
        break
    else:
        print("Please enter password Again: ")
        password = input()
        if password == 'swordfish':
            print("Access has been granted!!")
            break
        else:
            print("Password is not correct")
            print("Access has been denied")
            break
            

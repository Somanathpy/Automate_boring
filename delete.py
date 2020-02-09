import sys
while True:
    print("Type Exit to Exit")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed "+ response)
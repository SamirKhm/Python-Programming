while(True):
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        print("What kind of operation you want to perform on these numbers?\n Press + for addition\n Press - for subtraction\n Press * for multiplication\n Press / for division\n Press quit to exit the program")
        operation = input("Enter the operation you want to perform: ")
        if operation=="+":
            print("The sum of the two numbers is: ", a+b)
        elif operation=="-":
            print("The difference of the two numbers is: ", a-b)
        elif operation=="*":
            print("The product of the two numbers is: ", a*b)
        elif operation=="/":
            if b!=0:
                print("The quotient of the two numbers is: ", a/b)
            else:
                print("Division by zero is not allowed.")
        elif operation=="quit":
            print("Exiting the program.")
            break
        else:        print("Invalid operation. Please choose a valid operation.")
    except Exception as e:
        print("Enter valid value of a and b")
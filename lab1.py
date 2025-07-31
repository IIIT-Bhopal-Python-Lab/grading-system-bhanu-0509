def grade():
    marks = input()
    if marks == "EXIT":
        print("Exit successfully.")  # if user enter EXIT then it will exit the program
        return  # code exit
    try:
        marks = int(marks)
        if 90 <= marks <= 100: # marks is greater then and equal to 90 and less then and equal to 100 then grade is A
            print("A")
        elif 75 <= marks <= 89:
            print("B")
        elif 60 <= marks <= 74:
            print("C")
        elif 40 <= marks <= 59:
            print("D")
        elif 0 <= marks < 40:
            print("F")
        else:
            print("Invalid input")
    except:
        print("Invalid input") # if user enter any other value then it will show invalid input
grade() # call function

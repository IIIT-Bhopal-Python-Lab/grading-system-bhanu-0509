marks = input("Enter your marks (0-100): ")

if marks.isdigit():
    marks = int(marks)
    if 90 <= marks <= 100:
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
        print("INVALID INPUT")
else:
    print("INVALID INPUT")

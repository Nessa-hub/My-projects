print("Welcome to KNUST's grading system")
print("Enter your score to check your grade")
print("Press x to exit")



def grades(user_input):

    if user_input > 80:
       print("A")
    elif user_input >= 65:
       print("B")
    elif user_input >= 55:
       print("C")
    else:
       print("E")



def grades2():
    user_input = int(input("Please enter the numeric grade: "))
    if user_input > 80:
       print("A")
    elif user_input >= 65:
       print("B")
    elif user_input >= 55:
       print("C")
    else:
       print("E")

while input("Press any key to continue ")!="x":
             grades2()


while(raw_input("X to exit"))!="x":
     grade2()

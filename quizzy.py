print(" *** WELCOME TO THE QUIZ SHOW ***")

playing = input("Do you want to play?").lower()

if playing != "yes":
    quit()

print("Okay! Let's play.\n")
#################################


while True:
    i = 0

    print(''' 1. Full form of CPU ''')
    choices = input(''' 
    a) Control Process Upper            b) Central Processing Unit
    c) Centrifugal Product Uniform      d) Centrified Process Understanding 
    
    Answer =>''')

    if choices == "b":
        print(f"Correct !!! Your score is {i+1}\n ")
        i += 1
    else:
        print(f"Incorrect Answer! The correct answer is b.\n")

    # *******************************************************************

    print(''' 2. IC chips used in computers are usually made of: ''')
    choices = input(''' 
    a) Lead                             b) Sillicon 
    c) Chromium                         d) Gold 
    
    Answer =>''')

    if choices == "b":
        print(f"Correct !!! Your score is {i+1}\n ")
        i += 1
    else:
        print(f"Incorrect Answer! The correct answer is b.\n")
    # *******************************************************************

    print(''' 3. Which of the following is an extension of a temporary file? ''')
    choices = input(''' 
    a) .tnt                             b) .txt
    c) .tmp                             d) .tar
    
    Answer =>''')

    if choices == "c":
        print(f"Correct !!! Your score is {i+1}\n ")
        i += 1
    else:
        print(f"Incorrect Answer! The correct answer is c.\n")

    # *******************************************************************

    print(''' 4. Which of the following is not an example of an Operating System? ''')
    choices = input(''' 
    a) Windows 98                       b) BSD Unix
    c) Microsoft Office XP              d) Red Hat Linux
    
    Answer =>''')

    if choices == "c":
        print(f"Correct !!! Your score is {i+1}\n ")
        i += 1
        break
    else:
        print(f"Incorrect Answer! The correct answer is c.\n")
        break

print(f"Thank you for playing. Your final score is {i}\n")
quit()
# *******************************************************************

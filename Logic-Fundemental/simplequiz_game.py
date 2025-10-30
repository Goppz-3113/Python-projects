print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": #.lower is used to convert all the input to lower case
                             #so that the entries can be not case sensitive
    quit()

print("Okay! Let's play ")
score = 0 # use to keep track of the score

answer = input("What does CPU stand  ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1 # increments every time the if statements is true
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!") 
                   # we cannot concat str to int so we convert int score to str()
                   # we can also just use "," to add score to the str 


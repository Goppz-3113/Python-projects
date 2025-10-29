import random #module 

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #isdigit() checks whether the input is a digit 
    top_of_range = int(top_of_range) #convert the input str into an integer

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range) # genarates a random number
guesses = 0                                     # for randrange(1,10)-only random number between 1-9 is generated excluding 10 
                                                # for random.int(1,10) 10 is also included
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")
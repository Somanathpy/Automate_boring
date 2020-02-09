import random

secretNumber = random.randint(1,20)
print(" I am thinking a number between 1 and 20.")

#Ask the player to guess the number for 6 times.

for guessesTaken in range(1,7):
	print("take a Guess")
	guess = int(input(":"))
	if guess < secretNumber:
		print(" Your Guess is lower than the secretNumber")
	elif guess > secretNumber:
		print("Your guess is bigger than the secretNumber")
	else:
		break # this condition is the correct Guess

if guess == secretNumber:
	print("Congratulations you guessed my number in "+ str(guessesTaken)+ " Guesses")
else:
	print("The number i was thinking was"+ secretNumber)

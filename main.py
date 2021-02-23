import time
import random
print("ROCK, PAPER, SCISSORS")
time.sleep(2)
print("Rock wins against scissors. Scissors win against paper. Paper wins against rock. Enter 'R' for rock, 'P' for paper and 's' for scissors. You get 1 point per win and earn no points if you lose.")
options = ["r", "p", "s"]
noofrounds = input("Enter the number of rounds you want to play: ")
try:
	 int(noofrounds)
except ValueError:
	idontneedthsi = input("Only enter an integer value: ")
noofrounds = int(noofrounds)
ppoints = 0
mypoints = 0
while noofrounds != 0:
	mychoice = random.choice(options)
	pinput = input("Enter your play: ")
	pinput = pinput.lower()
	while pinput not in options:
		pinput = input("Only enter 'R', 'P', or 'S': ")
		pinput = pinput.lower()
	if (pinput, mychoice) == ("p", "r") or (pinput, mychoice) == ("s", "p") or (pinput, mychoice) == ("r", "s"):
		ppoints += 1
	if (pinput, mychoice) == ("r", "p") or (pinput, mychoice) == ("p", "s") or (pinput, mychoice) == ("s", "r"):
		mypoints += 1
	if mychoice == "p":
		print("The Computer chose 'Paper'!")
	if mychoice == "s":
		print("The Computer chose 'Scissors'!")
	if mychoice == "r":
		print("The Computer chose 'Rock'!")
	print(f"Your points: {ppoints}")
	print(f"Computer's points: {mypoints}")
	noofrounds += -1
if mypoints > ppoints:
	print(f"The Computer has won by {mypoints - ppoints} points!")
if mypoints < ppoints:
	print(f"You have won by {ppoints - mypoints} points!")
if ppoints == mypoints:
	print("It is a draw!")
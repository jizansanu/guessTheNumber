print('Hello! What is your name?')
myName = input()
myName = str(myName)
gn = len(myName)
y = 0

print('Well, ' + myName + ', I am thinking of a number between 1 and 20. \n')
if gn < 21 :
    for i in range(3):
        print('Take a guess.') # There are four spaces in front of print.
        guess = input()
        guess = int(guess)
        if guess < gn:
            print('Your guess is  low.') # There are eight spaces in front of print.

        elif guess > gn:
            print('Your guess is  high.')

        else:
            y = gn
            print ("yes")
            break
if (y==gn):
    print ("your guess is right")
else:
    print ("you can guess 3 times, my guess was ")
    print (gn)

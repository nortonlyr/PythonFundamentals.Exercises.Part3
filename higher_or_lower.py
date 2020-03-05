from random import randrange

def guess(): 
    yourNum = int(input('Give me a number: '))
    return yourNum
yourNum = guess()

def generateRandomNum():
    randomNum = randrange(0,10)
    return randomNum
randomNum = generateRandomNum()

def checkYourNumber(yourNum, randomNum):
    if yourNum > randomNum:
        print('Too high')
        print('The random number was ' + str(randomNum))
        print('Your guess was: ' + str(yourNum))
    elif yourNum < randomNum:
        print('Too low')
        print('The random number was ' + str(randomNum))
        print('Your guess was: ' + str(yourNum))
    else:
        print('Congratulation')
        print('The random number was ' + str(randomNum))
        print('Your guess was: ' + str(yourNum))

checkYourNumber(yourNum, randomNum)
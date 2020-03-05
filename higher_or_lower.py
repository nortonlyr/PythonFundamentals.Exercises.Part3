from random import randrange

def guess(): 
    """
    Enter guess number
    """
    global yourNum
    yourNum = int(input('Give me a number: '))
    print('Your guess was: ' + str(yourNum))
    return yourNum

YourNum = guess()


def generateRandomNum():
    """
    Generate a random number
    """
    global randomNum
    randomNum = randrange(0,10)
    print('The random number was ' + str(randomNum))
    return randomNum

randomNum = generateRandomNum() 


def checkYourNumber(yourNum, randomNum):
    """
    Compare the guess number and radomn number
    """
    if yourNum > randomNum:
        print('Too high')  
    elif yourNum < randomNum:
        print('Too low')
    else:
        print('Congratulation')

checkYourNumber(yourNum, randomNum)
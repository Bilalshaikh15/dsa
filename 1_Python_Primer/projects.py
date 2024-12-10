from random import randint

# P-1.29 Write a Python program that outputs all possible strings formed by using
# the characters c , a , t , d , o , and g exactly once.
def stringPermutation():
    # nPr 
    return


# P-1.30 Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
def divRepeat(num):
    count = 0
    if not num < 2:
        while (num / 2) > 2:
            num = num / 2
            count += 1
            # print(num)
    print(count)

# P-1.31 Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.

def makeChange(amount,giveAmount):
    changeToGive = amount - giveAmount
    rupee = {'1':0,'2':0,'5':0,'10':0,'20':0,'50':0,'100':0,'200':0,'500':0,}
    changeList = [500,200,100,50,20,10,5,2,1] 

    i=0
    while changeToGive and i<len(changeList):
        charged = False
        if((changeToGive / changeList[i])  >= 1):
            changeToGive = changeToGive - changeList[i]
            rupee[str(changeList[i])] += 1
            charged = True
        if(charged):
            i = 0
        else:
            i += 1

    print(rupee)

# P-1.35 The birthday paradox says that the probability that two people in a room
# will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people find it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5,10,15,20,...,100.

def generateRandomBirthday():
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = randint(0,11)
    date = randint(1,(months[month]))
    
    return f"{date}-{month}"

def generateRandomBirthdays(n):
    birthDays = []
    for i in range(n):
        birthDays.append(generateRandomBirthday())
    return birthDays

def checkSameBirthday(n=50):
    sameBirthdayCount = 0
    for i in range(10000):
        birthdays = generateRandomBirthdays(n)
        if(len(birthdays) == len(set(birthdays))):
            sameBirthdayCount+=1
    probabilityOfSameBithday = n/sameBirthdayCount
    print(probabilityOfSameBithday)


# P-1.36 Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You
# need not worry about efficiency at this point, however, as this topic is
# something that will be addressed later in this book.

def wordCount(str):
    words = {}
    liststr = str.split(" ")
    for word in liststr:
        if(words.get(word)):
            words[word] += 1
        else:
            words[word] = 1
    print(words)
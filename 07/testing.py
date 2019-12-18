import random

def testFun(myList):
    random.shuffle(myList)
    print(f"myList: {myList}")


aList = [0, 1, 2, 3]
print(f"BEFORE: {aList}")
testFun(aList)
print(f"AFTER: {aList}")

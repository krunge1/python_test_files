print("reverse list")
def reverseList(int):
    x = int+1
    for y in reversed(range(1, x)):
        print(y)
    
reverseList(5)

print("print 2 numbers in list")

exampleList = [500, 300, 20, 41, 2, 65]

def printAndReturn(firstNum, secondNum, list):
    print(list[firstNum], list[secondNum])

printAndReturn (0,2,exampleList)





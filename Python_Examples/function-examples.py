
def joinName(first, second):
    return first + " " + second

myName = joinName("Alice", "Smith")

def printMyName(x, name):
    for i in range(x):
        print(name)

printMyName(10, myName)

def reverseString(name):
    string = ""
    for c in name:
        string = c + string
    print(string)


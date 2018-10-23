# Programming - The Cliché Recipe Analogy 
An old, but gold, analogy of what programming is all about (certainly at a non-academic, practical, 'let's-build-things viewpoint). When your baking, you follow a recipe. The recipe has two main constiuent parts - the ingredients and the instructions. This is almost directly translate to programming - variables and functions. Scary words, perhaps, but if you think about it it makes a lot of sense. We'll be coming back to this analogy to make sense of things later so hold on to it.

## Why Python
Because:
- It's quick and easy to get setup and write programs, you'd be surprised how often this isn't the case.
- A large amount of the 'industry' use it, so it looks good on a resume.
- It has a **massive** amount of online tutorials, support and documentation not to mention libraires for days!

Tread carefully:
- Python does some weird things as we will discover
- Some people look down at people who use it for this reason, don't let them get to you.

At the end of the day, programming (at least in my opinion) is about building things. If you can build-it in python then that's as good a reason as any to use it. If you go into production-standard code then it is still being used, you just need to know the potential pitfalls and how to avoid them (*AS WITH ALL LANGUAGES*).

## Let's learn some syntax
Okay enough words, analogies and ramblings, let's get coding. Python is a fairly "high-level" language which means it has (thankfully) abstracted away from the ones and zeros and headed straight for plain english. For example:

```python
if 10 in [9, 10, 11]:
    print("Yep, it certainly is")
else:
    print("Sad times, it's not")
```

And just like that, you're learning python! I'm not even sure I need to explain what's happening in the code, but let's dive into the syntax of python (time for that cake-making metaphor to come back).

### Variables in Python
When creating variables, you can liken this to writing out some ingredients for a recipe, or at the very least their quantities.

```python
#Comments are declared with the hashtag symbol
cakeType = "Victoria Sponge"
vegan = False
eggs = 2
flour = 300
milk = 100
water = 100
sugar = 125
#Defining variables in terms of others is possible too
totalLiquid = milk + water #200
```
Here we have variables of the three most common *types* in python: strings ("..."), booleans (True, False) and integers (-100, 10 ...)

![A Duck](markdown_images/duck.png)
*More on the duck later*

### Conditional Statements
Conditional statements are those which control the flow of our code, like branches on a tree. 

```     
                    +-D
                    |   
                +-B-+
                |   |   
                |   +-E      
Left or right? -+     
                |   +-F
                |   |   
                +-C-+
                    |   
                    +-G    
```
To accomplish this in python we use the `if...else` statements along with indentation to specifiy that if a certain *condition* holds then we should do `x` otherwise do `y`.

```python
if vegan == True:
    print("Replace the milk with oatmilk and the eggs with bananas")
else:
    print("Carry on baking!")
```

The `==` operator is checking for equality between the left and right arguments. To check for inequality we could use `!=`. In this case we could have simple written `if vegan:` but sometimes you might want to be more specific or use different types like `if eggs > 1:`.

There is also the possibility to check for multiple conditions by placing the words `and` and `or` after a condition, you can then use parenthese to enclose certain parts of the condition. Our statement could then become something like:

```python
if vegan and (eggs == 0 and milk == 0):
    print("Replace the milk with oatmilk and the eggs with bananas")
else if eggs == 0 or milk == 0:
    print("You're not vegan, but you need to buy some milk and eggs")
else:
    print("Carry on baking!")
```

Notice how we added an extra conditional branch to our if statement. We could do this for however many branches we want, and could even nest these. 

### Arrays
Arrays are like lists of things - integers, strings etc. To create a new one in python there are two common approaches, the first is using square-brackets. 

```python
myList = [1, 2, 3, 4, 4, 5, 6, "dog"]
```

Not many languages support different types within the same list... and I don't condone the use of it. It's fine for certain things and also for hacking things together but sometimes things can happen which shouldn't. Imagine trying to sum an array that you thought was just integers...

Accessing different elements in an array can be done by using square brackets and placing the number of the element you want in the brackets - **0 indexed!**

```
myList = [1, 2, 3, 4, 4, 5, 6]
print(myList[1]) # 2
print(myList[1:3]) # [2, 3]
print(myList[-2:]) # [5, 6]
```

### Loops

Repeating things is quite a common practice in programming - updating the screen, summing over an array... and there are quite a few ways to achieve this.

1. **The For-Loop**: A mighty tool in the developers arsenal, the for loop is probably the most common looping device there is. In python it's made even easier by it's high-level abstract syntax. 
```python
for i in range(10):
    print(i) #0, 1, ... 9
```

Notice how we have used this `for` and `in` syntax. The `i` is our reference to the elements of the thing we are looping over (the *iterable*). Here we create a built-in python object (more about these soon) using the `range` constructor and supply it with an upper bound. 


### Functions

By now it may seem that all this code is floating aimlessly in the middle of a document. What if we wanted to bundle together different statements into collections of statement that do something. Like a function. 

Functions are exactly this - they're more like components or building blocks than mathematical functions. They can return something or they can be void (imagine all the function did was brint something).

In python we can create a function using the `def` keyword. It takes a name, followed by the arguments wrapped up inside brackets. Again make sure you remember the semi-colon and propoer indentation. 

```python
#A function to join two strings with a gap - it return the string
def joinName(first, second):
    return first + " " + second

#Set a variable to "Alice Smith"
myName = joinName("Alice", "Smith")

#A function which takes a number and a string name to print
def printMyName(x, name):
    for i in range(x):
        print(name)

printMyName(10, myName)
```

Some Exercises: 
1. Write a function that takes an array as an argument and returns the sum of all the elements. What happens when you mix the types in the array? 
2. Build a python function which takes a string and returns the string only reversed

### Classes and Objects

Okay. The mega-boss battle at the end of all of that python. Classes and objects. We'll take it easy and start with definitions and see how they apply after that. 

1. Class - a way of writing some code which outlines the blueprints for building things (objects) which can be reused again and again.
2. Objects - a specific instance of the blueprint. Imagine building a house, the plans for the house are the class and the actual houses you build are the objects.

Okay great. So how does this work in python and why should we bother? Sometimes we might want to associate function and variables with a certain type of object and we might want multple versions of these. The classic example is the `Student` class which allows me to make lots of `Student()` objects.

```python
class Student:
    def __init__(self, name, age, catchPhrase):
        self.name = name
        self.age = age
        self.catchPhrase = catchPhrase
    def speak(self):
        print("Hi I am " + self.name + " and I am " + self.age + " years old, " + self.catchPhrase)

student = Student("Rick", 60, "Wubba lubba dub dub!")
student.speak()
```
As you can see we tell python we're building a class with the `class` keyword, then the name of the class. By convention we start the name with an upper-case letter. Then we have to make a special `method` (a function related to the class) called `__init__`. Why all those underscores I here you ask? Python is a bit of "we're-going-to-make-it-object-oriented-or-die-trying" kind of a language. For more info, check [this](https://hackernoon.com/understanding-the-underscore-of-python-309d1a029edc) link. 

Remember that duck from before. Well this is where hopefully things should start making some sense. In python we have vert lax rules about types and in fact very little type-checking. We have duck typing: *If it walks like duck, swims like duck and quacks like a duck. Then it probably is a [duck](https://devopedia.org/duck-typing).*

More practically if the thing we're working with has the right method, then let's just used it! A bit weird, and can cause all sorts of headaches but great for writing quick and useful code. 

## The Project: Rock, Paper, Scissors

Now that we've learned so much. Let's make a game! Rock, paper, scissors is a classic and if you are unfamiliar check out the [link](https://en.wikipedia.org/wiki/Rock%E2%80%93paper%E2%80%93scissors). 

What do we need to build this: 
1. A Class of `Computer` this will make moves on the computers behalf using the imported module `random`
2. A way of getting user input - for Python 3.* use `input`
3. Some `if...elif...else` statements for checking who won
4. Wrap it all up in a `while` loop to play for a predetermined number of rounds. 

First let's build the computer:

```python
# A rock-paper-scissors game
#Imports are like saying "I want somebody else's functions and classes so I can reuse them", python has a few standard ones"
import random

#The Computer Class
class Computer:
    #The special init method (constructor)
    def __init__(self, name):
        #Initialise the objects member variables
        self.name = name
        self.moves = ["r", "p", "s"]
        self.move = ""
    #A method for the computer to make a random move
    def makeMove(self):
        rn = random.randint(0, 2)
        self.move = self.moves[rn]
        return self.move
```

Now we want to initialise some global variables to keep track of scores, rounds etc.

```python
rounds = 3
current_round = 0
user_score = 0
computer_score = 0

#Initialise the computer
computer = Computer("Master")
```


Okay, now we want to run the gameloop. This is fairly simple for us because we know the `current_round` and the number of `round`

```python
while(current_round < rounds):
    #The Game Logic
```

We also want a way to get a user input so they can also make a move. Python let's us do that with the `input` function. 

```python
user_input = input("Your move (r, p or s?): ")
```

But what if they type "Wubba lubba dub dub!". Well we can check what they typed and just loop around until they get it right!

```python
while(user_input not in ["r", "p", "s"]):
    user_input = input("Please choose from (r, p or s): ")
```

Next the computer can make its move and we can print that.

```python
computer_move = computer.makeMove()
print(computer.name + "'s Move: " + computer_move)
```

And finally, the long-winded, but hopefully correct game logic for the different possible outcomes. Note how if they're equal we loop back to the beginning and don't increment any counters effectively replaying that point again.

```python
#The Game Logic
if(user_input == computer_move):
        print("Draw! Replay the move!")
    elif(user_input == "r"):
        if(computer_move == "p"):
            print(":( the computer won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
        else:
            print(":) You won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
    elif(user_input == "p"):
        if(computer_move == "s"):
            print(":( the computer won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
        else:
            print(":) You won that round!")
            current_round = current_round + 1
            user_score = user_score + 1
    else:
        if(computer_move == "r"):
            print(":( the computer won that round!")
            current_round = current_round + 1
            computer_score = computer_score + 1
        else:
            print(":) You won that round!")
            current_round = current_round + 1
            user_score = user_score + 1
```

And just like that we have ourselves a working game! 



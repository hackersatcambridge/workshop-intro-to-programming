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

### Loops

### Functions

### Classes

This is the actual instructional workshop content.
Do not put a title on this document, it will already have one on the website
You can include images from the `images` folder like this:
![Image Description](images/cat.png)
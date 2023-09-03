import generator
import random

notANumber = ["Try again, student, I don't think that's a number.",
              "Please use only the digits 0-9 in your answer. It's the most magical way of choosing a number!",
              "Take this seriously, magicks are serious! A real number, please!"]
              

spellPrompts = ["Enter the number of spells you want me to make: ",
                "How many spells would you like?: ",
                "How many pages from my enchiridion do you want me to tear out and throw at you?: ",
                "Give me a number, and I'll give you that many spells!: "]

def looper(Spells):
    for i in range(int(Spells)):
        generator.OutputSpell()

def getinput():
    Spells = input(random.choice(spellPrompts))
    try:
        #Spells = int(Spells)
        print("Ok!", int(Spells), "coming up!")
        looper(Spells)
    except ValueError:
        print(random.choice(notANumber))
        getinput()
        
getinput()




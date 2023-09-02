import generator

Spells = input("Enter the number of spells you want me to make: ")

try:
    Spells = int(Spells)
    print("Ok!", Spells, "coming up!")
except ValueError:
    print("Try again, I don't think that's a number.")
    




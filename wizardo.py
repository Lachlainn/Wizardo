import random

output = ""
newEndings = ["lamo!!","zaaam!!", "!!", "shwiz!", "kadabra!", "kazaam!"]


def Randomise(lines):
    ran = random.randint(1,lines)
    return ran


def LineCount(file):
    with open(file,'r') as f:
       li = f.readlines()
    total_line = len(li)
    return(total_line)


def Phoneme(file):
    lines = LineCount(file)
    with open(file) as f:        
        r = Randomise(lines)
        content = f.readlines()
#         print("i counted ",lines,"lines in that document")
#         print("the number I randomised was",r)
        return content[r].strip()
    
    
for i in range(random.randint(3, 7)):
    r = random.randint(0, 1)
    if r == 0:
        f = "conE.txt"
    else:
        f = "vowE.txt"
    output = output + Phoneme(f)
    

    
print((output + random.choice(newEndings)).capitalize())
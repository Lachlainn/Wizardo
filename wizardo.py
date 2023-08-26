import random

output = ""
newEndings = ["lamo!!","zaaam!!", "!!", "shwiz!", "kadabra!", "kazaam!"] #to be appended later. might make into a long text file later


def Randomise(lines): #apparently this helps with not rolling the name number over and over??
    r = random.randint(1,lines)
    return r

def LineCount(file): #counts the number of lines in the file to pass to the RNG in the Phoneme randomiser
    with open(file,'r') as f:
       li = f.readlines()
    total_line = len(li)
    return(total_line)


def Phoneme(file):
    lines = LineCount(file)
    with open(file) as f:         # reads the txt file for either a vowel or a consonant
        r = Randomise(lines)
        content = f.readlines()
#         print("i counted ",lines,"lines in that document")
#         print("the number I randomised was",r)
        return content[r].strip()
    
    
for i in range(random.randint(3, 7)): #puts the acutal word together!
    r = random.randint(0, 1)
    if r == 0:
        f = "conE.txt"
    else:
        f = "vowE.txt"
    output = output + Phoneme(f)
    

    
print((output + random.choice(newEndings)).capitalize()) #maybe i should make the txt files into big strings and just use random.choice?
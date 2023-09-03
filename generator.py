import random

output = ""
newEndings = ["lamo!!","zaaam!!", "!!", "shwiz!", "kadabra!", "kazaam!"] #to be appended later. might make into a long text file later


def Randomise(lines): #apparently this helps with not rolling the name number over and over??
    r = random.randint(1,lines)
    return r - 1

def LineCount(file): #counts the number of lines in the file to pass to the RNG in the Phoneme randomiser
    with open(file,'r', encoding="utf-8") as f:
        li = f.readlines()
    total_line = len(li)
    return(total_line)


def Phoneme(file):
    lines = LineCount(file)
    with open(file, encoding="utf-8") as f:         # reads the txt file for either a vowel or a consonant
        r = Randomise(lines)
        content = f.readlines()
#         print("i counted ",lines,"lines in that document")
#         print("the number I randomised was",r)
        return content[r].strip()
    
def OutputSpell():
    global output
    print((output + random.choice(newEndings)).capitalize()) #maybe i should make the txt files into big strings  and just use random.choice?
    output = ""
    
for i in range(random.randint(3, 7)): #puts the acutal word together!
    global output
    r = random.randint(0, 1)
    if r == 0:
        f = "conM.txt"
    else:
        f = "vowM.txt"
    output = output + Phoneme(f)
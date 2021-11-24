
# defining all the function required fot t
def enterVaccination():
    print("1")

def getDetails():
    print("2")

def getTillNowDone():
    print("3")

# A startUp Interface for the user
print(" \t!!!!! WELCOME TO THE VACCINATION PORTAL !!!! \n")

print("\t\tWHAT DO YOU WANT TO PERFORM ? \n")
print("\t      1. ENTER MY VACCINATION DETAILS          ")
print("\t       2. GET MY VACCINATION DETAILS           ")
print("     3. GET THE NUMBER OF VACCINATIONS DONE TILL NOW")

# taking input from the user
userChoices = int(input("\n\n\t     PLEASE ENTER YOUR SELECTION :- "))

if(userChoices == 1):
    enterVaccination()
elif(userChoices == 2):
    getDetails()
else:
    getTillNowDone()

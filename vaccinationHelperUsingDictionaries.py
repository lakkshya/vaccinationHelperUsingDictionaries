
# starting our dictionaries of dictionaries with a garbage value
# we will store information of people with their Aadhar Number as their keys
# and rest all the fields as a dictionary with all values in key-value pair

allDetails = {
    "Garbage" : {"Name": "Name", "Gender" : "Gender", "D.O.B": "D.O.B", "TYPE": "TYPE", "DOSE 1": "DOSE 1", "DOSE 2": "DOSE 2"}
}

# defining all the function required fot t
def enterVaccination():
    print("1")

def getDetails():
    print("2")

def getTillNowDone():
    print("3")

# A startUp Interface for the user
print(" \t    !!!!! WELCOME TO THE VACCINATION PORTAL !!!! \n")

while(True):
    print("\t\t   WHAT DO YOU WANT TO PERFORM ? \n")
    print("\t         1. ENTER MY VACCINATION DETAILS          ")
    print("\t          2. GET MY VACCINATION DETAILS           ")
    print("\t  3. GET THE NUMBER OF VACCINATIONS DONE TILL NOW")
    print("\t\t\t    4. EXIT")

    userChoices = int(input("\n\n\t     PLEASE ENTER YOUR SELECTION :- "))

    if(userChoices == 1):
        enterVaccination()
    elif(userChoices == 2):
        getDetails()
    elif(userChoices == 3):
        getTillNowDone()
    else:
        print("\n\n\t\t      !!! THANK YOU !!!!")
        break

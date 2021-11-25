
# starting our dictionaries of dictionaries with a garbage value
# we will store information of people with their Aadhar Number as their keys
# and rest all the fields as a dictionary with all values in key-value pair

allDetails = {
    "Name": "Name", "Gender" : "Gender", "D.O.B": "D.O.B", "TYPE": "TYPE", "DOSE 1": "DOSE 1", "DOSE 2": "DOSE 2"
}

# defining all the function required fot t
def enterVaccination():
    print("\n\n")
    name = input("NAME : ")
    gender = input("GENDER : ")
    dob = input("D.O.B. : ")
    doseType = input("DOSE TYPE : ")
    allDetails.update({"Name" : name})
    allDetails.update({"Gender" : gender})
    allDetails.update({"D.O.B" : dob})
    allDetails.update({"TYPE" : doseType})

def getDetails():
    print(allDetails)

def getTillNowDone():
    print("\n\n")
    print(" NO OF PEOPLES GOT VACCINATED TILL NOW ARE :- ", len(allDetails)-6)
    noOfFirstDose = 0
    noOfSecondDose = 0
    for aadhars, values in allDetails.items():
        for keys in values:
            if( keys == "DOSE 1" and values[keys] != "NA" ):
                noOfFirstDose = noOfFirstDose + 1
            elif( keys == "DOSE 2" and values[keys] != "NA" ):
                noOfSecondDose = noOfSecondDose + 1
    print(" NO OF PEOPLES GOT VACCINATED WITH I DOSE ARE :- ", noOfFirstDose)
    print(" NO OF PEOPLES GOT VACCINATED WITH II DOSE ARE :- ", noOfSecondDose)
        

# A startUp Interface for the user
print(" \n\t    !!!!! WELCOME TO THE VACCINATION PORTAL !!!! \n")

while(True):
    print("\n\t\t   WHAT DO YOU WANT TO PERFORM ? \n")
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

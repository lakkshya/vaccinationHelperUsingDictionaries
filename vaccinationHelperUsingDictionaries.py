
# starting our dictionaries of dictionaries with a garbage value
# we will store information of people with their Aadhar Number as their keys
# and rest all the fields as a dictionary with all values in key-value pair

allDetails = {
    "Garbage" : {"Name": "Name", "Gender" : "Gender", "D.O.B": "D.O.B", "TYPE": "TYPE", "DOSE 1": "DOSE 1", "DOSE 2": "DOSE 2"}
}

# defining all the function required fot t
def enterVaccination():
    print("\n")
    print("\t   !!!! WELCOME TO DETAILS ADDITION PORTAL !!!! \n")

    aadharNumber = input("\tPLEASE ENTER YOUR ADDHAR NUMBER :- ")
    while(len(aadharNumber) != 12):
        print("\t !!!! INVALID AADHAR NUMBER ENTERED PLEASE TRY AGAIN !!!! ")
        aadharNumber = input("\t PLEASE ENTER YOUR ADDHAR NUMBER :- ")
    
    if aadharNumber in allDetails:
        print("\n\t YOUR DETAILS ARE ALREADY IN OUR RECORDS ")
        userConcern = input("\t WANT TO UPDATE SECOND DOSE INFO ( YES / NO ) :- ")
        if( userConcern == "YES"):
            allDetails[aadharNumber]["DOSE 2"] = "COMPLETED"
        print("\n\t||    DETAILS OF SECOND DOSE ADDED SUCCESFULLY   ||")
    else:
        name = input("\tPLEASE ENTER YOUR FULL NAME :- ")
        gender = input("\tPLEASE SPECIFY YOUR GENDER :- ")
        dobEntered = input("\tPLEASE ENTER YOUR DATE OF BIRTH :- ")
        vaccinationType = input("\tPLEASE ENTER YOUR VACCINE TYPE / NAME :- ")
        print("\n\t|| YOU ARE GETTING VACCINATED FOR THE FIRST TIME ||")
        print("\t||    DETAILS OF FIRST DOSE ADDED SUCCESFULLY    ||\n")
        allDetails[aadharNumber] = {"Name": name, "Gender" : gender, "D.O.B": dobEntered, "TYPE": vaccinationType, "DOSE 1": "COMPLETED", "DOSE 2": "NA"}


def getDetails():
    showRecord = input("\n\tEnter your Aadhar Number to get details :- ")
    print("\n\t\tName : ", allDetails[showRecord]["Name"])
    print("\t\tGender : ", allDetails[showRecord]["Gender"])
    print("\t\tDate of Birth : ", allDetails[showRecord]["D.O.B"])
    print("\t\tVaccine Name : ", allDetails[showRecord]["TYPE"])
    print("\t\tDose 1 : ", allDetails[showRecord]["DOSE 1"])
    print("\t\tDose 2 : ", allDetails[showRecord]["DOSE 2"], "\n")

def getTillNowDone():
    print("\n")
    print(" NO OF PEOPLES GOT VACCINATED TILL NOW ARE :- ", len(allDetails)-1)
    noOfFirstDose = 0
    noOfSecondDose = 0
    for aadhars, values in allDetails.items():
        for keys in values:
            if( keys == "DOSE 1" and values[keys] == "COMPLETED" ):
                noOfFirstDose = noOfFirstDose + 1
            elif( keys == "DOSE 2" and values[keys] == "COMPLETED" ):
                noOfSecondDose = noOfSecondDose + 1
    print(" NO OF PEOPLES GOT VACCINATED WITH I DOSE ARE :- ", noOfFirstDose)
    print(" NO OF PEOPLES GOT VACCINATED WITH II DOSE ARE :- ", noOfSecondDose)
        

# A startUp Interface for the user
print("--------------------------------------------------------------------")
print("\n \t    !!!!! WELCOME TO THE VACCINATION PORTAL !!!! \n")

while(True):
    print("--------------------------------------------------------------------\n")
    print("\t\t   WHAT DO YOU WANT TO PERFORM ? \n")
    print("\t         1. ENTER MY VACCINATION DETAILS          ")
    print("\t          2. GET MY VACCINATION DETAILS           ")
    print("\t  3. GET THE NUMBER OF VACCINATIONS DONE TILL NOW")
    print("\t\t\t    4. EXIT")
    print("\n--------------------------------------------------------------------")

    userChoices = int(input("\n\t     PLEASE ENTER YOUR SELECTION :- "))

    if(userChoices == 1):
        enterVaccination()
    elif(userChoices == 2):
        getDetails()
    elif(userChoices == 3):
        getTillNowDone()
    else:
        print("\n\n\t\t      !!! THANK YOU !!!!")
        break

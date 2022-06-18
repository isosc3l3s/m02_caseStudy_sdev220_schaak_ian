#Name: Ian Schaak
#date modified: 06/18/2-22
#version: python 3.10.5
#purpose: program takes in student last name and GPA and returns whether or not they made honor roll or deans list

#declared variables
studentNameList = []
studentGpaList = []
DEANS_LIST = 3.5
HONOR_ROLL = 3.25
proceedWithProgram = ""
idex = 0

#while loop to take inputs and compare them to constantns DEANS_LIST and HONOR_ROLL
while proceedWithProgram != "zzz" :
  
    studentLastName = input("\n\nEnter the last name for this student\n")
    studentNameList.append(studentLastName)
    studentGpa = float(input("\nPlease enter the corresponding student's GPA.\n"))
    studentGpaList.append(studentGpa)
  
    if studentGpaList[idex] < HONOR_ROLL:
      print("\nEducation in and of itself has no accollades. This knowledge is yours to keep, regardless of any roll or dean.")
    if studentGpaList[idex] >= HONOR_ROLL:
      print ("\ncongratulations", studentNameList[idex],"you have made the Honor Roll!")
    if studentGpaList[idex] >= DEANS_LIST:
      print ("FORGET ABOUT THE HONOR ROLL",studentNameList[idex],"YOU'VE MADE THE DEAN'S LIST!")
      
#print ("FORGET ABOUT THE HONOR ROLL",studentNameList[idex].upper,"YOU'VE MADE THE DEAN'S LIST!")
#this line gave the result on the next line. Why doesnt .upper work on repl?
#FORGET ABOUT THE HONOR ROLL <built-in method upper of str object at 0x7f5fac134930> YOU'VE MADE THE DEAN'S LIST!
      
    idex = idex+1
    proceedWithProgram = input("\nto end the program enter zzz. Press enter for information on next student\n")
    
  


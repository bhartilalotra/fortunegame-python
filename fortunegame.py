#GUESS THE FORTUNE DAY GAME


print("....................PANASONIC COMPANY.......................")
#details of the employee.

username = input("Enter the username: ")
Empid = int(input("Enter the empid: "))
contact = int(input("Enter the contact number: "))
emailid = input("Enter the email ID: ")
Dept = input("Enter the department: deo , intern or hr")

#  employee information
print(f"...Username is: {username}....")
print(f"...Employee ID is: {Empid}...")
print(f"...Contact is: {contact}....")
print(f"...Email ID is: {emailid}....")
print(f"...Department is: {Dept}....")

# Department tasks
def deo():
    print("Enter your guess number:")
    guess = int(input("Enter a number between 1 and 7: "))
    if guess == 1:
         print("You have a lot of workload.")
         print("You have to complete 40 files.")
    elif guess == 2:
        print("Your task is to complete 30 files before 2 PM.")
    elif guess == 3:
        print("Your task is to complete 40 files before 1 PM.")
        print("Next, you need to load the data from these files into a single Excel sheet.")
    elif guess == 4:
        print("Today's work is to complete Excel sheets.")
        print("You need to complete 20 files and submit them after 12 PM.")
    elif guess == 5:
        print("Today's workload is light.")
        print("You only need to complete 10 files.")
    elif guess == 6:
        print("Great news! You have a half day today.")
    elif guess == 7:
        print("Today is a holiday. Enjoy your day off!")
    else:
        print("Invalid guess. Please enter a number between 1 and 7.")
def intern():
    
    print("Enter your guess number:")
    guess = int(input("Enter a number between 1 and 7: "))
    if guess == 1:
        print("You have a lot of workload.")
        print("You have to complete 40 files with your senior .")
    elif guess == 2:
        print("Your task is to reserch on our company and write about it till 2 pm.")
    elif guess == 3:
        print("Your task is to attend project meeting with your senior.")
        print("Next, you need to load the data from these files into a single Excel sheet.")
    elif guess == 4:
        print("You have to attend workshops and  learning sessions.")
    elif guess == 5:
        print("Today's workload is low.")
        print("You only need to create social media template about company.")
    elif guess == 6:
        print("Great news! You have a half day today.")
    elif guess == 7:
        print("Today is a holiday. Enjoy your day off!")
    else:
        print("Invalid guess. Please enter a number between 1 and 7.")
        
def hr():        
    
    print("Enter your guess number:")
    guess = int(input("Enter a number between 1 and 7: "))
    if guess == 1:
        print("You have a lot of workload.")
        print("You have to conduct 50 interviews tody and select 20 employ .")
    elif guess == 2:
        print("ypo have to manage orientation process for new hires including their paperworks,selection createria all.")
    elif guess == 3:
        print("you have to ensure that the all emplo who assignes for their jobs have skills to manage their manage or not.")
    elif guess == 4:
        print(" you have to identify training needs and organizing programs to enchance employe skills.")
    elif guess == 5:
        print("Today's workload is low.")
        print("your have to mantain accurate and confidential empl records,incl contracts ,performance and reviews.")
    elif guess == 6:
        print("Great news! You have a half day today.")
    elif guess == 7:
        print("Today is a holiday. Enjoy your day off!")
    else:
        print("Invalid guess. Please enter a number between 1 and 7.")

userdesignation=input("enter the userdesignation : ") 
print(f".....The userdesignation is :  {userdesignation}") 
if(userdesignation=="DEO"):
    deo()
elif(userdesignation=="INTERN"):
    intern()
elif(userdesignation=="HR"):
    hr()
else:
    print("...........NO SPECIFIC DESIGNATION......")
    


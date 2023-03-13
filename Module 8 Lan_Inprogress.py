# Alberto Alcaide-Morales
# 3/12/2023
#Problem #1: isEqual function determines if both prameters x and y are equal or not
print("\n\nProblem 1: ")
x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))
def isEqual(x, y):
    if x == y: 
        print("x and y are equal")
    else:
        print("x and y are NOT equal")

isEqual(x, y)

#Problem 2: Relationalvar function contains to parameters and determines if the sum of x and y are greater, equal to, or less than 10
print("\n\nProblem 2: ")
x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))
def Relationalvar(x, y):
    z = 10
    if x + y > z:
        print("The sum is greater than 10. ")
    elif x + y < z:
        print("The sum is less than 10")
    else:
        print("The sum equals 10")

Relationalvar(x, y)

#Problem 3: Function contains to arguments x and my_list and determines if x exist on my_list or not
print("\n\nProblem 3: ")

my_list = [69, 420, 5, 14]
x = 5

def Existance(x , mylist_):
    if x in my_list:
        print("Value of 5 exist on the list")
    else:
        print("Value of 5 does NOT exist on the list")

Existance(x, my_list)


Existance(x, my_list)

#Problem 4:  funtion takes 1 argument: year
#Depending on the input from user it will determine if year is leap year or not
print("\n\nProblem 4: ")
def is_leap(year):
    leap = False
    
    
    if year%4==0 :
        leap = True
    elif year%400 == 0 and year%100 != 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))

#Problem:5
print("\n\nProblem 5: ")

listOfItems = ['pan', 'paper', 'idea', 'rope', 'groceries']
listOfDebuffs = ['slow']

# currentTask fuction takes 3 arguments: listOfItems, listOfDebuffs, and a taskNum. 
#When choosing the taskNum the function determines if you are able to perform the task given the items needed and checking for debuffs.
def currentTask( listOfItems, listOfDebuffs, taskNum): 
    if taskNum == 1:
        print("You choose to climb a mountain!")
        r = "rope"
        c = "coat" 
        f = "first aid kit"
        s = "slow"
        rope_b = False
        coat_b = False # Boolean False means item | status is not present
        firstaidkit_b = False
        slow_b = False
        
        if r in listOfItems:
            #print("You have a rope!Move on to the next step.") 
            rope_b = True   
     
        if c in listOfItems:
            #print("blank")
            coat_b = True
        if f in listOfItems:
            #print("You have a first aid kit!Move on to the next step.")
            firstaidkit_b = True
        if s in listOfDebuffs:
            #print("Remove debuff before climbing moutain.")
            slow_b = True
            
        if rope_b == True and coat_b == True and firstaidkit_b == True and slow_b == False:
            print("You meet all the criteria, you can finally climb the mountain!")
        else:
            print("You cannot climb the mountain you do NOT meet the criteria!")
    
    if taskNum == 2:
        print("You choose to cook a meal!")
        p = "pan"
        g = "groceries"
        sm = "small"
        pan_b = False
        groceries_b = False
        small_b = False
        if p in listOfItems:
           # print("You have a pan! Move on to the next step.")
            pan_b = True
        
        if g in listOfItems:
            #print("You have a groceries!Move on to the next step.")
            groceries_b = True

        if sm in listOfDebuffs:
            #print("Remove debuff before cooking a meal.")
            small_b = True 
        if pan_b == True and groceries_b == True and small_b == False:
            print("You meet all the criteria, you can cook a meal")
        else:
            print("You cannot cook a meal, you do NOT meet the criteria")
    if taskNum == 3:
        print("You choose to write a book!")
        pe = "pen"
        pap = "paper"
        id = "idea"
        co = "confusion"
        pe_b = False
        pap_b = False
        id_b = False
        co_b = False
        if pe in listOfItems:
           # print("You have a pen! Move on to the next step")
            pe_b = True
        if pap in listOfItems:
            #print("You have paper! Move on to next step!")
            pe_b = True
        if id in listOfItems:
            #print("You have an Idea! Move on to next step!")
            id_b = True
        if co in listOfDebuffs:
            #print("Remove debuff before writing a book!")
            con_b = True
        if pe_b == True and pap_b == True and id_b == True and co_b == False:
            print("You meet al the criteria, you can write a book!")
        else:
            print("You cannot write a book, you do NOT meet the criteria!")




currentTask(listOfItems, listOfDebuffs, taskNum) #To test other taskNum, change and chose either 1, 2, or 3
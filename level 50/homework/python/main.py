#                             დავალება 1

#Python Lists

#1) Write a script to create and print a list.
#2) Create a script to add and remove elements from a list.
#3) Write a script to sort a list.
#4) Demonstrate the use of list comprehension.
#5) Create a script to find the length of a list.
#===========================================================================

#                                 1

animals = ["Dog", "Cat", "Sheep", "Pig"]
print(animals)


#============================================================================

#                                 2

animals= ["Dog", "Cat", "Sheep", "Pig", "Chicken"]
animals.pop(4)
animals.append("Hippo")
print(animals)


#==============================================================================

#                                  3

animals= ["Dog", "Cat", "Sheep", "Pig", "Chicken"]
animals.sort()
print(animals)


#============================================================================== 

#                                  4




#===============================================================================

#                                  5

animals= ["Dog", "Cat", "Sheep", "Pig", "Chicken"]
animals.count(4)
print(animals)


#===============================================================================

#                                  დავალება 2

#Python If...Else

# 1) Write a script that uses an if statement to check a condition.
# 2) Create a script that uses an if-else statement.
# 3) Write a script that uses an if-elif-else statement.
# 4) Demonstrate nested if statements.
# 5) Write a script that uses the ternary operator.


#===============================================================================

#                                 1

if 10 >= 9:
    print("Check")

#===============================================================================

#                                 2

ask_year = int(input("Enter Youre Age:      "))
if ask_year >= 18:
    print("Alowed")
else:
    print("Not Alowed")


#===============================================================================

#                                 3

ask_bank = int(input("Enter Your Balance: "))
if ask_bank >= 10000:
    print("You Can Buy Gum In 2120")
elif ask_bank < 10:
    print("In 2120 You Cant Even Buy Air")
else: 
    print("Please Type Corectly!!")

#===============================================================================

#                                  4




#===============================================================================



#                                  5






#===============================================================================

#                                   დავალება 3

# Python While Loops

# 1) Write a script to demonstrate a while loop.
# 2)Create a script that uses a while loop with a break statement.
# 3) Write a script that uses a while loop with a continue statement.
# 4) Demonstrate an infinite loop and how to stop it.
# 5) Create a script that uses a while loop to iterate over a list.


#===============================================================================

#                                   1

count = 1
while count <= 5:
    print("რიცხვი არის:", count)
    count += 1


#===============================================================================

#                                   2



count = 1
while count <= 5:
    if count == 3:
        break
    print("რიცხვი არის:", count)
    count += 1


#===============================================================================

#                                  3



count = 1
while count <= 5:
    if count == 3:
        count += 1
        continue
    print("რიცხვი არის:", count)
    count += 1






#===============================================================================

#                                  4


while True:
    print("დააჭირეთ Ctrl+C შესაჩერებლად.")

    ask = input("Do you want to stop?: (yes or no)")
    if ask == "yes":
        break
    else:
        print("OK")




#===============================================================================

#                                  5


my_list = ["ვაშლი", "ბანანი", "ატამი"]
index = 0
while index < len(my_list):
    print("ხილი არის:", my_list[index])
    index += 1


#===============================================================================

#                                   დავალება 4

#Python For Loops

#Write a script to demonstrate a for loop.#
#Create a script that uses a for loop to iterate over a list.
#Write a script that uses a for loop with the range() function.#
#Demonstrate nested for loops.
#Create a script that uses a for loop with an else clause.

#===========================================================================

#                                 1




for number in [1, 2, 3, 4, 5]:
    print("რიცხვი არის:", number)


#===========================================================================

#                                 2



fruits = ["ვაშლი", "ბანანი", "ატამი"]
for fruit in fruits:
    print("ხილი არის:", fruit)

#===========================================================================

#                                 3


for number in range(5):
    print("რიცხვი არის:", number)


#===========================================================================

#                                 4


#===========================================================================

#                                 5


for number in range(3):
    print("რიცხვი არის:", number)
else:
    print("ციკლი დასრულდა!")



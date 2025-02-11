import os
import random
import time

def clear():
    os.system('clear')


print("you are playing against tit for tat")
balance = 0
balance2 = 0
rounds = 1
print("you can defect of cooperate")
print("if you defect and the opponent cooperates you win 5 points and him 0")
print("if you both cooperate you both get 3")
print("start y or n")
action = input()
if action == "y":
    clear()
else:
    exit()
print("the game has started choose if you will cooperate (c) or defect (d): ")
def titfor():
    if rounds == 1:
        action2 = "c"
    else:
        action2 = action

while rounds < 50:
     
     if rounds == 1:
        action2 = "c"
     else:
        action2 = action
     action = ""
    
     if rounds == 1:
        action = "d"
     else:
        action = action2
     
       
     
    
     print(" ")
     #action = input("choose  c or d: ")
    


     if action == "c" and action2 == "c":
          balance += 3
          balance2 +=3
     elif action == "c" and action2 == "d":
           balance2 += 5
     elif action == "d" and action2 == "c":
           balance += 5
     elif action == "d" and action2 == "d":
         balance  += 1
         balance2 += 1
     else:
         print("there has been an error in the responses " + action + " and " + action2 )
         exit()

     
     print("your balace is: " + str(balance) + " and his balance is: " + str(balance2) )
     print(" ")
     print("you choose: " + action + " he chose: " + action2)
     int(balance2)
     int(balance)
     rounds = rounds + 1
     time.sleep(0.5)
     clear

     
if balance > balance2:
    print("you won")
elif balance == balance2:
    print("you got a draw")
else:
    print("you lost")






    


import random
'''
-1 for water
1 for snake
0 for gun
'''
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
while True:
    try:
        youStr=input("Enter your choice :")
        if youStr not in youDict:
            print("Invalid choice! Please enter 's', 'w', or 'g'.")
            # exit()

        you=youDict[youStr]
        computer=random.choice([-1,0,1])
        print(f"You choose {reverseDict[you]} ")
        print(f"Computer choose {reverseDict[computer]}")

        # if(computer == you):
        #     print("It's draw... ")
        # else:
        #     if(computer == -1 and you == 1):
        #         print("You win !")
        #     elif(computer == 1 and you == 0):
        #         print("You win !")
        #     elif(computer == 0 and you ==-1):
        #         print("You win !")
        #     elif(computer == -1 and you == 0):
        #         print("You lose !")
        #     elif(computer == 1 and you == -1):
        #         print("You lose !")
        #     elif(computer == 0 and you == 1):
        #         print("You lose !")
        #     else:
        #         print("Something went wrong !")
        if(computer == you):
            print("It's draw... ")
        else:
            if((computer-you) == 2 or (computer-you)== -1):
                print("You lose !")
            else:
                print("You win !")
    except Exception as e:
        print("Try again !")

import random
exit = False
user_points = 0
computer_points = 0
while exit == False:

    options = ["rock", "paper", "scissors"]
    user_inputs = input("choose rock, paper, scissors or exit: ")
    computer_inputs = random.choice(options)

    if user_inputs == "exit":
        print("game ended")
        print("you won a total score of "+str(user_points)+" and the computer total score is "+str(computer_points))
        exit = True
    if user_inputs == "rock":
        if computer_inputs =="rock":
            print("your input is rock")
            print("computer input is rock")
            print("it is a tie")
        elif computer_inputs =="paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer win")
            computer_points +=1
        elif computer_inputs =="scissors":
            print("your input is rock")
            print("computer input is scissors")
            print("you win")
            user_points +=1
    elif user_inputs == "paper":
        if computer_inputs =="rock":
            print("your input is paper")
            print("computer input is rock")
            print("you win")
            user_points +=1
        elif computer_inputs =="paper":
            print("your input is paper")
            print("computer input is paper")
            print("it is a tie")
           
        elif computer_inputs =="scissors":
            print("your input is paper")
            print("computer input is scissors")
            print("computer win")
            computer_points +=1       
    elif user_inputs == "scissors":
        if computer_inputs =="rock":
            print("your input is scissors")
            print("computer input is rock")
            print("computer win")
            computer_points +=1
        elif computer_inputs =="paper":
            print("your input is scissors")
            print("computer input is paper")
            print("you win")
            user_inputs +=1
        elif computer_inputs =="scissors":
            print("your input is scissors")
            print("computer input is scissors")
            print("it is a tie")

    elif user_inputs != "rock" or user_inputs != "paper" or user_inputs != "scissors" :
        print("invalid input")      
            
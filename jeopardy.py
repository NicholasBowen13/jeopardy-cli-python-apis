import requests
import random
response = requests.get('http://jservice.io/api/clues?category=139').json()
score = 0
while True:
    user_input = input("Type P to play and Q to quit" + "\n") 
    if user_input.upper() == "P":
        num = random.randint(0,len(response))
        user_response = input(response[num]["question"] + "\n" )
        if user_response == response[num]["answer"]:
            print("Congratulations!") 
            score += response[num]["value"]
        else: 
            print("Wrong! The correct answer was " + response[num]["answer"]) 
            score -= response[num]["value"]
        print("Your current score is " + str(score))
    elif user_input.upper() == "Q":
        print("Thanks for playing! Your score was " + str(score))
        break
    else: 
        print("Invalid input, please try again.")

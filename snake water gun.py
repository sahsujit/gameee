
import random
print("Welcome to snake water gun game")
print("you will play with computer. 's' for snake, 'w' for water, 'g' for gun.")
options=['s','w','g']
user_score=0
compuetr_score=0
while True:
   user_choice=input("Enter your choice: ").lower()
   if user_choice not in options:
      print("invalid input.please try again.")
      continue
   computer_choice=random.choice(options)
   print("computer_choose: ", computer_choice)
   if user_choice==computer_choice:
      print("It's tie!")
   elif (user_choice == 's' and computer_choice == 'w') or (user_choice == 'w' and computer_choice == 'g') or (user_choice == 'g' and computer_choice == 's'):
      print("you win!")
      user_score+=1
   else:
      print("computer win!")
      compuetr_score+=1
   print("your score: ", user_score)
   print("computer score: ", compuetr_score)
   play_again=input("do you want to pay again?(y/n):")
   if play_again !='y':
      break

import random

def get_choices():
  player_choice = input("Enter a choice (Rock, Paper, Scissors): ").capitalize()
  options = ["Rock", "Paper", "Scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice} 
  return choices

def check_win(player, computer):
  print(f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie"
  elif player == "Rock":
    if computer == "Scissors":
      return "Rock smashes Scissors, You Win!"
    else:
      return "Paper cover Rock, You Lose!"
  
  elif player == "Paper":
    if  computer == "Scissors":
      return "Scissors cut Paper, You Lose!"
    else:
      return "Paper cover Rock, You Win!"
  
  elif player == "Scissors":
    if  computer == "Rock":
      return "Rock smashes Scissors, You Lose!"
    else:
      return "Scissors cut Paper, You Win!"
  else: 
    return "That's not Rock, Paper, Scissors anymore!"
  
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
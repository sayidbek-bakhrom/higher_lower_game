from art import logo, vs
from game_data import data
import random




def format_data(account):
  """"Format the account data into printable format."""
  account_name = account["name"]
  account_info = account["description"]
  account_country = account["country"]

  return f"{account_name}, a {account_info} from { account_country}"


print(logo)

score = 0
game_is_on = True
account_b = random.choice(data)

while game_is_on:


# generate a random account from the game data.
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
      return guess == "a"
    else:
      return guess == "b"
        



  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  # ask user for a guess
  guess = input("Who has more followers? Type 'A' or 'B'").lower()

  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]


  # chek if user is right
  is_correct = check_answer(guess, a_follower_count, b_follower_count)


  
  # give user feedback on their guess
  
  if is_correct:
    print(f"You're right! Current score is {score}")
    score += 1
  else:
    print(f"Sorry, that's wrong. Final score is {score}")
    game_is_on = False

# date 1/15/2022
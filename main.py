import random
from replit import clear
from art import logo
def deal_card():
  """ bu fonk. rasgele bir kart döndürür"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card

def calculate_score(cards):  
  """bu fonk.kartları toplar,başlangıçta blackjack varsa 0 döndürür,as başlangıçta gelirse 11 ileride el 21 i geçerse 1 olur"""
  if sum(cards)==21 and len(cards)==2:
    return 0

  if 11 in cards and sum(cards)>21:
      
    cards.remove(11)
    cards.append(1)
      
      
  return sum(cards)
  
def Compare(user_score,computer_score):
  """bu fonk. eldeki kartların toplamını karşılaştırır"""
  
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0 or user_score==21:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
def Game(): 
  print(logo)
  user_cards = []
  computer_cards = []
  should_continue=True
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())  
  while should_continue: 
      
    user_score=calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"your hand {user_cards} your score: {user_score}")
    print(f"computer's first card {computer_cards[0]} ")
    
    if user_score > 21 or user_score==0 or computer_score==0:
      
      
      should_continue=False
    elif input("Type 'y' to get another card, type 'n' to pass: ")=="y":        
    
      user_cards.append(deal_card())
    else:
      should_continue = False
  
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"your hand {user_cards} your score: {user_score}")
  print(f"computer's first card {computer_cards} computer's score:{computer_score} ")
  print(Compare(user_score,computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':")=="y":
  clear()
  Game()

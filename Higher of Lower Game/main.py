from art import logo, vs
from game_data import data

game = True
points = 0 
empty_block = 0

print(logo)
while game is True:
  for i in range(0, len(data)):
    
    person1 = data[i]
    person2 = data[i + 1]
    
    name1 = person1['name'],
    description1 = person1['description'],
    country1 = person1['country'],
    followers1_unconverted = int(person1['follower_count']),
    followers1 = followers1_unconverted[0]
  
    name2 = person2['name'],
    description2 = person2['description'],
    country2 = person2['country'],
    followers2_unconverted = int(person2['follower_count']),
    followers2 = followers2_unconverted[0]
    
    print(f"Compare A: {''.join(name1)}, a {''.join(description1)}, from {''.join(country1)}.")
    print(vs)
    print(f"Compare B: {''.join(name2)}, a {''.join(description2)}, from {''.join(country2)}.")
    
    answer = input("Who was more followers? Type 'A' or 'B': ")
    if answer == "a":
      if followers1 > followers2:
        points += 1
        print(f"You're right! Current score is: {points}.")
      elif followers1 < followers2:
        print(f"You're wrong! Current score is: {points}.")
        game = False
        break
    if answer == "b":
      if followers2 > followers1:
        points += 1
        print(f"You're right! Current score is: {points}.")
      elif followers2 < followers1:
        print(f"You're wrong! Current score is: {points}.")
        game = False
        break
    
  

  



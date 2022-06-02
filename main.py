from random import randint
player = input('rock (rock), paper(paper), or scissors(scissors)? ')
print(player, 'vs ', end = '' )
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
  computer = 'rock'
elif chosen ==2:
  computer = 'paper'
else:
  computer ='scissors'
print(computer)
if player == computer:
  print('DRAW! ')
elif player == 'rock' and computer == 'scissors':
  print('Player wins! ')
elif player =='rock' and computer == 'paper':
  print('Computer wins! ')
  
elif player == 'paper' and computer == 'rock':
  print('Player wins! ')
elif player =='paper' and computer == 'scissors':
  print('Computer wins! ')

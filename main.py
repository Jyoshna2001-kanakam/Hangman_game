#Hangman game
import random

word_list=['apple','banana','mango','cherry']
lives=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in range(len(chosen_word)):
     display+='-'
print(display)

game_over=False
while not game_over:
     guessed_letter=input("Guess the letter:").lower()
     for position in range(len(chosen_word)):
          letter=chosen_word[position]
          if letter==guessed_letter:
               display[position]=guessed_letter
     print(display)
     if guessed_letter not in chosen_word:
          lives-=1

     n=10
     for i in range(1,n+1):
          for j in range(1,n+1):
               if i==1:
                    print('-',end=' ')
          
               elif lives==6 and j==n and i==1:
                    print('         |',end=' ')
               elif lives==5 and i==2 and j==n:
                    print('         |')
                    print('        ( )')
               elif lives==4 and i==3 and j==n:
                    print('         |')
                    print('        ( )')
                    print('        / ')
               elif lives==3 and i==3 and j==n:
                    print('         |')
                    print('        ( )')
                    print('        /| ')
               elif lives==2 and i==3 and j==n:
                    print('         |')
                    print('        ( )')
                    print('        /|\ ')
               elif lives==1 and i==4 and j==n:
                    print('         |')
                    print('        ( )')
                    print('        /|\ ')
                    print('        / ')
                    
               elif lives==0 and i==4 and j==n:
                    print('         |')
                    print('        ( )')
                    print('        /|\ ')
                    print('        / \ ')
                    print("you lose")
                    game_over=True
                    break
                    
               # else:
               #      print('',end=' ')
          print()

     if '-' not in display:
          game_over=True
          print("you win...!")
#Hangman stages
lives=int(input("Enter lives:"))
# lives=0
n=10
for i in range(1,n+1):
     for j in range(1,n+1):
          if i==1 or i==n:
               print('-',end=' ')
          elif lives==6 and j==n and i==1:
               print('|',end=' ')
          elif lives==5 and i==2 and j==n:
               print('|')
               print('        ( )')
          elif lives==4 and i==3 and j==n:
               print('|')
               print('        ( )')
               print('        / ')
                 
          elif lives==3 and i==3 and j==n:
               print('|')
               print('        ( )')
               print('        /| ')
          elif lives==2 and i==3 and j==n:
               print('|')
               print('        ( )')
               print('        /|\ ')
          elif lives==1 and i==4 and j==n:
               print('|')
               print('        ( )')
               print('        /|\ ')
               print('        /')
                
          elif lives==0 and i==4 and j==n:
               print('|')
               print('        ( )')
               print('        /|\ ')
               print('        / \ ')
                
          else:
               print('',end=' ')
     print()

#-----------------
#          |
#         ( ) 
#         /|\    
#         / \
#
#
#-----------------

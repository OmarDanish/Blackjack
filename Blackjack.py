import time
import random

flag=True
sleep=1

print('\nWelcome to blackjack')
time.sleep(sleep)

#user cards
uc=[]
#user hidden 
uh=random.randint(1,11)
#computer cards
cc=[]
#computer hidden
ch=random.randint(1,11)
#user total
ucsum=sum(uc)
ut=ucsum+uh
#computer total
ccsum=sum(cc)
ct=ccsum+ch


def computer_bust():
    print ('\nThe computer went over 21, you win!')
    print (' ')

def user_bust():
    print('\nYou went over 21, you lose')
    print (' ')
    
while flag:
    uc.append(random.randint(1,11))
    while ct<18:
        cc.append(random.randint(1,11))
    
    print ('\nYour card(s): ')
    print (uc)
    time.sleep(sleep)
    print ('\nYour facedown card: ')
    print (uh)
    time.sleep(sleep)
    
    print ('\nThe computers card(s): ')
    print (cc)
    time.sleep(sleep)
    print ('\nThe computers facedown card: ')
    print ('?')
    time.sleep(sleep)
    
    print('\nDo you want to draw?')
    user_input=input('Yes/No\n\n')
    
    user_input.lower()
    
    if user_input=='yes':
        continue
    
    if user_input=='no':
        break

#user total
ucsum=sum(uc)
ut=ucsum+uh
#computer total
ccsum=sum(cc)
ct=ccsum+ch


print ('\nYour card(s): ' )
print (uc)
time.sleep(sleep)
print ('\nYour facedown card: ' )
print (uh)
time.sleep(sleep)
print ('\nYour total: ')
print (ut)
time.sleep(sleep)


print ('\nThe computers card(s): ' )
print(cc)
time.sleep(sleep)
print ('\nThe computers facedown card: ' )
print (ch)
time.sleep(sleep)
print ('\nThe computers total: ' )
print (ct)
time.sleep(sleep)

if ut>21:
    user_bust()
    
if ct>21:
    computer_bust()
    
if ct>ut:
    print ("\nThe computer had the higher number, you lose...")

elif ut>ct:
    print ('\nYou had the higher number, you win!')
    
elif ut==ct:
    print('\nYou and the computer had the same number, its a draw.')
    



    
    
    
    
    
    
print ('Python Programming')
myname=str(input('Enter your name:  '))
myage=int(input('Enter your age:    '))
print("--------------------")
print(f"Welcome mr {myname}")
print(f'You are {myage} years old')
if myage<18:
    print(f'{myname} is not eligible to vote')
else :
    print(f'{myname} is eligible to vote')
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_name = (name1+name2).lower()
t = combine_name.count('t')
r = combine_name.count('r')
u = combine_name.count('u')
e = combine_name.count('e')

true = t+r+u+e

l = combine_name.count('l')
o = combine_name.count('o')
v = combine_name.count('v')
e = combine_name.count('e')

love = l+o+v+e

true_love = str(true) + str(love)
true_love = int(true_love)

if true_love < 10 or true_love > 90:
    print (f"Your score is {true_love}, you go together like coke and mentos.")

elif true_love > 40 and true_love < 50:
    print (f"Your score is {true_love}, you are alright together.")

else:
    print (f"Your score is {true_love}")


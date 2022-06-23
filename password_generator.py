import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(' ,')' ]

print("RANDOM PASSWORD GENERATOR")

password=""

a=int(input("Put number of letters you want to insert in password:"))
b=int(input("Put number of numbers you want to insert in password:"))
c=int(input("Put number of symbols you want to insert in passwords:"))

for i in range(a):
    random_letters=random.choice(letters)
    password+=random_letters
for i in range(b):
    random_number=random.choice(numbers)
    password+=random_number
for i in range(c):
    random_symbol=random.choice(symbols)
    password+=random_symbol
      
print(f"Easy version of password is : {password}")

#hard password
hard_password=[]
for i in password:
    hard_password.append(i)
random.shuffle(hard_password)
password_hard=""
for passw in hard_password:
    password_hard+=passw
print(f"hard version of password is : {password_hard}")

    
      
import string, random

#password check

count = 0
good_things = ['%','$','#','@','!','^','&','?']
user_password = input('\nType your password: ')

for letter in user_password:
    if letter in good_things:
        count += 1
    else:
        continue
        
if len(user_password) > 7 and count >= 1:
    print('\npassword is good :)') 
else:
    print('password is bad, change that one, you can use randomly generated below') 

#password generator

password = []
for i in range(0,25):
    password.append(random.choice(string.ascii_letters))

random_int = random.randint(1,25)
random_int2 = random.randint(1,25)
password[random.randint(0,24)] = "%"
password[random.randint(0,24)] = "$"
password[random.randint(0,24)] = "*"
password[random.randint(0,24)] = "@"
password[random.randint(0,24)] = "#"
password[random.randint(0,24)] = "!"

password.append(str(random.randint(1,1000)))
password.append(str(random.randint(1,1000)))

passw = ' '
for letter in password:
    passw += '' + letter

passw[random.randint(1,25)].upper
passw[random.randint(1,25)].upper
passw[random.randint(1,25)].lower

print("\n",'Generated password: ',"\n",passw,'\n')


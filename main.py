# name = input('What is your name?')
# print('Hellloooooooo ' + name)

#Playing in Python Basics
# birth_year = input('What year were you born')
#
# age = 2022 - int(birth_year)
#
# print(f'your age is: {age}')


#Checking password

username = input('Whats your username?')

password = input('Whats your password?')

password_length = len(password)

hidden_password = '*' * password_length

print(f'{username}, your password {hidden_password} is {password_length} letters long')

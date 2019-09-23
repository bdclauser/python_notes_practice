name = ''
age = 0

while name != 'Alice':
    print('Enter your name:')
    name = input()
if name == 'Alice':
    print('Hi, Alice.\nPlease enter your age:')
    age = int(input())
if age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
from random import random, randint, randrange, choice
import sys
from utils import helper
from utils.help2 import very_useful_function as useful

print(sys.platform)

print(random())
print(f'Your price is {int(random() * 100)}')
print(randint(0, 1))
print(randrange(0, 10, 2))
users = ['user11', 'user12', 'user100']
print(choice(users))

helper.assist()
print(helper.variable)
while 'sldkjfl' == 'sdsdfsdf':
    if 'sldkjfl' == 'sdsdfsdf':
        print(f'skadflkasdjfhalsdkjhlaksdfjhlaksjdfh {useful()}')
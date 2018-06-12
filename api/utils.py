import random

def shuffle(input):
    list = input[:]
    random.shuffle(list)
    return list

# Testing
# list = list(range(0, 5))
# print(shuffle(list))
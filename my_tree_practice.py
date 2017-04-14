import math

variable = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

x_count = variable.count(0)
y_count = variable.count(1)


def entropy(x, y):
    e = - x/(x + y) * math.log(x/(x + y), 2) - y/(x + y) * math.log(y/(x + y), 2)
    return e

def fraction_of_

if __name__ == '__main__':
    print(entropy(x_count, y_count))








# entropy of the children is gonna be the weighted average of two branches 3/4 of my children going to my steep branche with an entropy of 0.

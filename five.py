# This is a python copy of the original five.js
# Found at https://github.com/jackdcrawford/five.git

import random
import math
import time

#misc

def five():
    print 5
def roman():
    print 'V'
def string():
    print "five"

#maths

def plus(int):
    sum = 5 + int
    print sum
def minus(int):
    sum = 5 - int
    print sum
def times(int):
    sum = 5 * int
    print sum
def divide(int):
    sum = 5 / int
    print sum
def power(int):
    power = math.pow(5,int)
    print power

# checks

def isfive(int):
    if int == 5:
        print "%d is equal to five" % int
    else:
        print "%d is not equal to five" % int

def greater(int):
    if int > 5:
        print "%d is greater than five" % int
    else:
        print "%d is less than five"

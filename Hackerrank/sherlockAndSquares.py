#square integer: every number n that n** = m. Find number of square numbers
#in a range that goes from a to b.
#MATH FACT: the number of square numbers in an interval is the difference
#between the sqrt of the higher humber nad the sqr of the lower number

from math import *

def squares(a,b):
    return floor(sqrt(b))-ceil(sqrt(a))
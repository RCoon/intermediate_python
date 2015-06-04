##: The Russian Peasant's Algorithm 
##: Been around for a long time. (Seventeenth Century B.C.)

##: Multiply two numbers together.
##: Requirements: multiply by 2, divide by 2, and Add numbers

##: AKA = Mediation and Duplication method 

# 24 X 16 = ?
# 
# X 12   32
# X 6    64
# 3    128
# 1    256
# ----------
#      384
#      
# 238 X 13 = ?
# 
# 119    26
# 59     52
# 29    104
# X 14    208
# 7     416
# 3     832
# 1    1664
# -----------
#     3094
    
##:
##: Inputs -> two numbers
##: Output -> the solution to those two numbers
##:           multiplied together using the Russian Peasant Algorithm 

import timeit
import time

CACHE = {}

def russian_peasant(a,b):
    largest = max(a, b)
    smallest = min(a, b)
    sum = 0
    while largest // 2 != 1:
        left_col = largest // 2
        right_col = smallest * 2
        if left_col % 2 != 0:
            sum += right_col
        largest = left_col
        smallest = right_col
    sum += smallest * 2
    return sum


def russian(a,b):
    key = (a, b)
    if key in CACHE:
        z = CACHE[key]
    else:
        x = a; y = b                     # Semicolon -> Compound Statement
        z = 0                            # Accumulator
        while x > 0:
            if x % 2 == 1: z = z + y     # Modulo operator
            y = y << 1                   # Shift Binary over to left
            x = x >> 1                   # Shift Binary over to right
            CACHE[key] = z
    return z

a = 357
b = 16

# def test_russian():
#     assert russian(357,16) == 5712
#     
#     start_time = time.time()
#     print(russian(357,16))
#     print("Russian Algorithm took {0:f} seconds.".format(time.time() - start_time))

def test_russian():
    russian(a, b)
    
def test_peasant():
    russian_peasant(a, b)
    
russian_peasant_timer = timeit.Timer(stmt='russian_peasant(a,b)', setup='from __main__ import russian_peasant,a,b')
russian_timer = timeit.Timer(stmt='russian(a,b)', setup='from __main__ import russian,a,b')

min_peasant_result = min(russian_peasant_timer.repeat(3,1000))
min_russian_result = min(russian_timer.repeat(3,1000))

print('Peasant time: {0:f}.'.format(min_peasant_result))
print('Russian time: {0:f}.'.format(min_russian_result))

# 17 in base 2:   10001 = 17         10001
#                  >> 1               << 1
#                  1000 = 8         100010 = 34
    
# print(russian_peasant(238, 13))
# print(russian(238, 13))    
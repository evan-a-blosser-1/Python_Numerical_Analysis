""" 42.py
    Author: Evan Blosser
    Based on the mathematics of:
    Andrew Sutherland (MIT)
        & Andrew Booker (Bristol Univ.)

    Three cubes whose sum is: 42 

    expressed as x^3 + y^3 + z^3 = k
    
    for a number range of: 1 to 100
    
    Smaller numbers are easier such as 29, 
    but numbers like 32 & 33 are far more challenging.
    
    42, the answer to life, is unsolvable until 
    2017, when a supercomputer of 580,000 cores
    computed the answer to life's 
    great question...
    42 = (-80538738812075974)^3 + 80435758145817515^3 + 12602123297335631^3
    
    https://news.mit.edu/2019/answer-life-universe-and-everything-sum-three-cubes-mathematics-0910
    
    Also See: Hitchhikers Guide to the Galaxy
"""

import numpy as np


def Answer (x,y,z):
    return x**3 + y**3 + z**3




def find_xyz_for_k(k, range_min=1, range_max=100):
    # Create a set to store cubes of numbers in the given range
    cubes = {x**3: x for x in range(range_min, range_max + 1)}
    
    solutions = []
    for x in range(range_min, range_max + 1):
        for y in range(range_min, range_max + 1):
            remaining = k - (x**3 + y**3)
            if remaining in cubes:
                z = cubes[remaining]
                solutions.append((x, y, z))
    return solutions

# Define the range of numbers to check
Number_Range = np.linspace(1, 100, 100, dtype=int)

target_values = [3, 29, 42]  
for k in target_values:
    solutions = find_xyz_for_k(k)
    if solutions:
        print(f"Solutions for k={k}:")
        for solution in solutions:
            print(f"x={solution[0]}, y={solution[1]}, z={solution[2]}")
    else:
        print(f"No solutions found for {k}")
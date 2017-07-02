# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 23:28:02 2017

@author: Srinivas Bhaskar
Reference: https://www.youtube.com/watch?v=BfS2H1y6tzQ&t=62s
Question: What is the longest walk you can take so that,
          'on average' you will end up 'n' blocks or fewer from home
"""
import random

##Perform a random walk and return final co-ordinates
def Random_Walk(num_steps):
    x = 0
    y = 0
    for i in range(num_steps):
        choice = random.choice(['N','S','E','W'])
        if choice == 'N':
            x = x+1
        elif choice == 'S':
            x = x-1
        elif choice == 'E':
            y = y-1
        elif choice == 'W':
            y = y+1
    ##return final co-ordinates after the walk
    return (x, y)

##Alternate menthod to perform a random walk and return final coordinates
def Random_Walk_2(num_steps):
    x,y = 0,0
    for i in range(num_steps):
        dx, dy = random.choice([(0,1),(0,-1),(-1,0),(1,0)])
        x = dx+x
        y = dy+y
    return (x,y)

num_iterations = 10000
no_transport = 4
max_num_steps = 40

for num_steps in range(max_num_steps):
    no_transport_counter = 0
    for i in range(num_iterations):
        walk = Random_Walk_2(num_steps)
        distance = abs(walk[0]) + abs(walk[1])
        if distance <= no_transport:
            no_transport_counter += 1
    no_transport_percentage = no_transport_counter/num_iterations
    print("Num Steps: " + str(num_steps) + "; Percentage Not Needing Transport = " + str(round(no_transport_percentage,2)))
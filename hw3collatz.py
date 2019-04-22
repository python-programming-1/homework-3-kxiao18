# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:20:40 2019

@author: Karen(Hui) Xiao
"""

    
def collatz(num):
    while num >1:
        if (num%2) == 0:
            num = num//2      
        elif (num%2) == 1:
            num = num * 3 + 1 
        print(num)
        collatz(num)
        return num


while True:
    userInput=input('Please enter an ingeter: ')
    try:
        collatz(int(userInput))
        break
    except ValueError:
        print('Invalid Input. Please enter an integer')
        continue


  


    


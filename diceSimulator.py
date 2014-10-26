#!/usr/bin/env python
"""
	This is a program written by Adam used to simulate dice with different sides.
"""
import random
import input

dice = input.int_input("How many dice would you like to roll?")
sides = input.int_input("How many sides on your die?")

diceInit = 1

while diceInit <= dice:
	print("The die #{} shows: {}".format(diceInit,random.randint(1,sides)))
	diceInit +=1
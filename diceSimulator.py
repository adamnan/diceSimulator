#!/usr/bin/env python
"""
	This is a program written by Adam used to simulate dice with different sides.
"""
import random
import input

print("This program simulates rolling several dice.\nThe user can choose how many dice are rolled.")

dice = input.int_input("How many dice would you like to roll?")

diceInit = 1

while diceInit <= dice:
	while True:
		sides = input.int_input("How many sides on die #{}?".format(diceInit))
		if sides < 2:
			print("A dice should have at least two sides.")
			continue
		else:
			break
	print("The die #{} shows: {}".format(diceInit,random.randint(1,sides)))
	diceInit +=1
import random
import input

sides = input.int_input("How many sides on your die?")

print("The die shows: {}".format(random.randint(1,sides)))
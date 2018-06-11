"""
Creating a dynamic LIFO stack as Python list
and animating it on Jupyter Notebook ;)
""" # A7!

from IPython.display import clear_output
import time

teststring = "This is a test string, and I am about to do magic with it !"

sol = 5 #stack of length 5
stack = [None] * sol


for character in teststring:
    clear_output(wait=True)
    
    stack.append(character)
    stack = stack[-sol:]
    
    print(stack)
    
    time.sleep(1)

import os, glob, string, time, sys
import numpy as np
import pandas as pd, pandas.io.common
import cv2 as cv2
import matplotlib, matplotlib.pyplot as plt
from IPython.display import display, Image
%matplotlib inline 

print("┌┬┐┌─┐┌┬┐┌─┐  ┌─┐┌─┐┬┌─┐┌┐┌┌─┐┌─┐")
time.sleep(1)
print(" ││├─┤ │ ├─┤  └─┐│  │├┤ ││││  ├┤ ")
time.sleep(1)
print("─┴┘┴ ┴ ┴ ┴ ┴  └─┘└─┘┴└─┘┘└┘└─┘└─┘")

for char in "Welcome to Data Sciences with A7™":
    time.sleep(0.1)
    print(char, end='', flush=True)

print ("\nusing Pandas version:",pandas.__version__)
print("using Python version:", sys.version)

print("Libraries and other tools have been imported...")

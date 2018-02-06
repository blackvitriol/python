'''
this is to analyze data and its properties, acquire metadata for planning
load your variable as sample
'''

sample = lbl

print(id(sample))
print(type(sample))
print(len(sample))
print(repr(sample))

if type(sample).__module__ == "numpy":
    print("The variable selected is a Numpy Array with size: ",sample.size, )
    
print("this is a work in progress")

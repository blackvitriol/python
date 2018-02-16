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
    print("This is a Numpy N-Dimension Array with",'\n'
          "size:",sample.size,'\n'
          "shape:",sample.shape,'\n'
          "strides:",sample.strides,'\n'
          "data type:", sample.dtype,'\n'
          "flags:",'\n', sample.flags
         )
    
print("this is a work in progress")

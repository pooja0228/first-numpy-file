import numpy as np                 #for numerical python
import matplotlib.pyplot as plt    #for plotting graphs

a = np.array([(10,20,30),(40,50,60)])  #To create array or matrix

print(a.ndim)                   #for dimension
print(a.itemsize)               #bytesize
print(a.dtype)                  #datatype
print(a.size)                   #total no of elements

a = a.reshape(3,2)              #to change the dimension
a = a.reshape(2,3)

#slicing : to extract few elements
print(a[0:1,1:3])  # before comma rows element are slicesd 

#numbers between two integers
a = np.linespace(1,3,5) #this doesnt work in spyder

#arithmatic operations on single matrix

print(a.max())          #for maximum value
print(a.min())          #for mininmum value
print(a.sum())          #for sum of each element in array

print(a.sum(axis=0))    #sum of each column
print(a.sum(axis=1))    #sum of each row

#arithmatic operations on multiple matrix

b = np.array([(10,80,30),(20,50,70)])
c = np.array([(10,20,30),(40,50,60)])
d = np.array([(70,80,90),(10,20,50)])

print(b+c+d)             #sum of all three matrix
print(b-c-d)             #subtraction
print(b*c*d)             #multiplication
print(b/c/d)             #division

#In case of list "+" works as a concatenation function

#concatenation in numpy can be done in two ways:

# 1) vertical stacking : on the top of one another

print(np.vstack((a,b)))
 
# 2) horizontal stacking : beside one another

print(np.hstack((a,b)))

#To convert it into a single row or to make dimension 1*n

print(a.ravel())

#other operators

print(np.sqrt(a))    #square root
print(np.std(a))    #standard deviation : when element varies from its mean value

#special functions

# 1) cosine and sine that are used to plot graphs of our elements

x = np.arange(0,3*np.pi,0.1)  #it returns evenly spaced value
y = np.sin(x)
plt.plot(x,y)
plt.show()

# 2) exponential function(e^x))    e=2.71  

print(np.exp(a))  #It gives the exponential value for each element

# 3) logarithmic functions (ln x) : natutal log with base e

print(np.log(a))    #log with base e

print(np.log10(a))  #log with base 10

#--------*---------*----------*----------*---------*-------*-------*--------*--------*-----*

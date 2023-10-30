import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
data = np.genfromtxt("iris.data",delimiter=",")
print (data)
print ("Data type :", type(data))
print ("Data shape : ", data.shape)
print (data[:10])
data1 = np.genfromtxt("iris.data",delimiter=",",dtype=None)
print(data1.shape)
print(type(data1))
print(type(data1[0]))
print(type(data1[0][4] ))
print(data1[:10])
dt = np.dtype("f8,f8,f8,f8,U30")
data2= np.genfromtxt("iris.data",delimiter=",",dtype=dt)
print(data2.shape)
print(type(data2))
print(type(data2[0]))
print(type(data2[0][4]))
print(data2[:10])
sepal_length=[]
sepal_width=[]
petal_length=[]
petal_width=[]
for dot in data2:
    sepal_length.append(dot[0])
    sepal_width.append(dot[1])
    petal_length.append(dot[2])
    petal_width.append(dot[3])
plt.figure(1)
setosa,=plt .plot(sepal_length[:50],sepal_width[:50],'ro',label='Setosa')
versicolor,= plt.plot(sepal_length[50:100], sepal_width[50:100],'g^',label='Versicolor')
virginica,=plt.plot(sepal_length[100:150],sepal_width[100:150],'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2,borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('sepal_width')

plt.figure(2)
setosa,=plt .plot(sepal_length[:50],petal_width[:50],'ro',label='Setosa')
versicolor,= plt.plot(sepal_length[50:100], petal_length[50:100],'g^',label='Versicolor')
virginica,=plt.plot(sepal_length[100:150],petal_length[100:150],'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2,borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('sepal_width')

plt.figure(3)
setosa,=plt .plot(sepal_length[:50],petal_width[:50],'ro',label='Setosa')
versicolor,= plt.plot(sepal_length[50:100], petal_width[50:100],'g^',label='Versicolor')
virginica,=plt.plot(sepal_length[100:150],petal_width[100:150],'bs', label='Verginica')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2,borderaxespad=0.)
plt.xlabel('Sepal Length')
plt.ylabel('sepal_width')

plt.show()


plt.show









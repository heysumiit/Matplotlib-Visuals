import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[8,5,7,90]
a=[90,20,30,45]
b=[15,10,60,40]
c=[18,45,16,49]

l=["Area-1","Area-2","Area-3","Area-4"]

plt.stackplot(x,y,a,b,c,colors=["k","r","b","c"],labels=l)
plt.legend(loc=2)
plt.show()

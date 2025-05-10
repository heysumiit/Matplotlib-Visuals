import matplotlib.pyplot as plt
x=[4,2,3,1]
y=["Python","C","Java","C++"]

c=["c","y","b","k"]

ex=[0.0,0.0,0.0,0.1]

plt.title("Pie Plot",fontsize=20)
plt.legend(y)
plt.pie(x,labels=y,autopct="%0.4F%%",explode=ex,shadow=True,startangle=0,rotatelabels=False)
plt.show()

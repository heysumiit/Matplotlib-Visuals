import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
plt.title("Box Plot",fontsize=20)
plt.boxplot(x,labels=["python"],showmeans=True,sym="r+")
plt.show()

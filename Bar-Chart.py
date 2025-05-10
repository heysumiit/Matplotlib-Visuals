import matplotlib.pyplot as plt
x=[1,2,3,4,5,7]
y=[7,4,6,8,5,3]
c=["c","y","b","k"]

plt.title("Bar Chat",fontsize=20)

plt.xlabel("Programing Language")
plt.ylabel("Score")
plt.bar(x,y,color=c,width=0.5,edgecolor="r",linewidth=1,alpha=1,label="Popularity")
plt.legend()
plt.show()

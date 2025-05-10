import matplotlib.pyplot as plt
x=[1,2,3,4,5,7]
y=[7,4,6,8,5,3]

plt.title("Stem Plot",fontsize=20)

plt.stem(x,y,linefmt=":",markerfmt="r+",label="Python")
plt.legend()
plt.show()

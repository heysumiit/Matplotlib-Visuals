import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[10,20,30,40,20,80,10,90]

plt.title("Step Plot",fontsize=20)
plt.step(x,y,marker="o",ms=10,mfc="c")
plt.grid()
plt.show()

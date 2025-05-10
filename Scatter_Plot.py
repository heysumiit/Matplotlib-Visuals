import matplotlib.pyplot as plt
day=[1,2,3,4,5,7]
no=[7,4,6,8,5,3]
c=["r","b","y","c","k","g"]
size=[300,100,400,250,160,290]

plt.title("Scatter Plot",fontsize=20)
plt.scatter(day,no,color=c,s=size,marker="*")
plt.xlabel("Day")

t=plt.colorbar()
t.set_label("Colorbar",fontsize=20)
plt.ylabel("Number")
plt.show()

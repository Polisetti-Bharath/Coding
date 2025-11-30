import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5])
y=x*2
plt.plot(x,y)
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
plt.figure()
x1=[2,4,6,8,10]
y1=[1,3,5,7,9]
plt.plot(x1,y1,linestyle='dotted')
plt.show()
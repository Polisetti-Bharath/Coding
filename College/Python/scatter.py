import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([5,7,4,6,5,8,7,9,6,10])
colours=np.array([4,5,6,7,8,9,10,11,12,13])
plt.scatter(x,y,c=colours,cmap='viridis')
plt.title("Scatter Plot Example")   
plt.show() 
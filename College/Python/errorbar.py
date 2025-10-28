import numpy as np
import matplotlib.pyplot as plt
x=['A','B','C','D']
means=[5,7,6,8]
std_devs=[0.5,1.2,0.8,1.0]
plt.bar(x,means,yerr=std_devs,capsize=5)
plt.xlabel('Category')
plt.ylabel('Mean Value')
plt.title('Error Bar')
plt.show()
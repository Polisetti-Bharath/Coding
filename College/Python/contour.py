import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-3,3,100)
y=np.linspace(-3,3,100)
x,y=np.meshgrid(x,y)
z=np.sin(np.sqrt(x**2+y**2))
plt.contourf(x,y,z,levels=20,cmap='viridis')
plt.colorbar(label='Z value')
plt.title('Contour Plot')
plt.xlabel('X axis') 
plt.ylabel('Y axis') 
plt.show()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

z= np.array([-1j,1j])
p= np.array([-0.5,0])

ax = plt.subplot(111)
plt.axvline(0,color='grey') #Adding axes
plt.axhline(0,color='grey')

plt.plot(z.real, z.imag, 'o', color='black') #Adding poles and zeros
plt.plot(p.real, p.imag, 'x', color='black')

plt.axis('scaled') #Setting x axis and y axis limits
plt.axis([-2, 2, -2, 2])
plt.grid()

# Add unit circle and zero axes 
x = np.linspace(-2,2,1000)  
    
#Coloring the ROC viz. the entire z plane except poles      
y1 = np.sqrt(16-x**2)
y2 = -np.sqrt(16-x**2)
plt.fill_between(x, y1, y2, color='cyan')

#Plotting circles
unit_circle = patches.Circle((0,0), radius=1, fill=False,color='grey', ls='dashed')
ax.add_patch(unit_circle)
boundary = patches.Circle((0,0), radius=0.5, fill=False, color='black', ls='solid')
ax.add_patch(boundary)
inner_circle = patches.Circle((0,0), radius=0.5,color='white', ls='solid')
ax.add_patch(inner_circle)

#Adding annotations
plt.text(0,0.1,"z=0")
plt.text(-0.7,0.1,"z=-0.5")
plt.text(0,1.1,"z=1j")
plt.text(0,-1.2,"z=-1j")
plt.text(0.7,0.1,"|z|>0.5")
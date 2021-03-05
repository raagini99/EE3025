import numpy as np
import matplotlib.pyplot as plt

#Input signal
x = np.array([1.0,2.0,3.0,4.0,2.0,1.0])
k = 20

#Computing output signal
y = np.zeros(20)
y[0] = x[0]
y[1] = -0.5*y[0]+x[1]

for n in range(2,k-1):
    if n < 6:
        y[n] = -0.5*y[n-1]+x[n]+x[n-2]
    elif n > 5 and n < 8:
        y[n] = -0.5*y[n-1]+x[n-2]
    else:
        y[n] = -0.5*y[n-1]

#Displaying x(n) lollipop plot
plt.figure(1)
plt.stem(range(0,6),x)
plt.xlabel('$n$')
plt.ylabel('$x(n)$')
plt.grid()

#Displaying y(n) lollipop plot
plt.figure(2)
plt.stem(range(0,k),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

print("Maximum value of |x(n)| = ",max(abs(x)))
print("Maximum value of |y(n)| = ",max(abs(y)))
print("Both x(n) and y(n) are bounded. ")
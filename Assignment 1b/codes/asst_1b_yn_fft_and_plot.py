import numpy as np
import math
import matplotlib.pyplot as plt

x_n = np.array([1,2,3,4,2,1],dtype='complex')


#Recursive function that computes FFT of a sequence of length which is a power of 2
def FFT_2n(x_n):
    length = len(x_n)
    if(length==1):
        return x_n
    X_k = np.zeros((length,),dtype='complex')
    half_length = int(length/2)
    x_n_odd = np.zeros((half_length,),dtype='complex')
    x_n_even = np.zeros((half_length,),dtype='complex')
    for i in range(half_length): #Separating odd and even halfs of the sequence
        x_n_even[i] = x_n[2*i]
        x_n_odd[i] = x_n[2*i+1]
    O_k = FFT_2n(x_n_odd) #Recursively calling the function for each half
    E_k = FFT_2n(x_n_even)
    for i in range(half_length):
        z = np.exp((2*np.pi*i/length)*1j) #Computing the values for the sequence from the values of sub-halfs
        X_k[i] = O_k[i] + z*E_k[i]
        X_k[i+half_length] = O_k[i] - z*E_k[i]
    return X_k
    
#Function that computes FFT of a sequence
def FFT(x_n):
    length = len(x_n)
    exp = math.log(length,2)
    exp_ceiled = math.ceil(exp)
    if exp!=exp_ceiled: #Padding with zeros to make length of sequence a power of 2
        x = np.zeros((2**exp_ceiled,),dtype='complex')
        x[0:length] = x_n
        x_n = x
    return FFT_2n(x_n)

#Function that computes IFFT of a sequence
def IFFT(X_k):
    return np.conjugate(FFT(np.conjugate(X_k)))/len(X_k)


#Computing h(n)
h_n = np.zeros((1000,),dtype='complex')
h_n[0] = 1
h_n[1] = -0.5
for n in range(2,1000):
    h_n[n] = (-0.5)**n + (-0.5)**(n-2)

#Padding x(n) with zeros to make it the same length as h(n) so that frequencies match
x = np.zeros((1000,),dtype='complex')
x[0:len(x_n)] = x_n
x_n = x

#Computing X(k) and H(k) via FFT
X_k = FFT(x_n)
H_k = FFT(h_n)

#Time domain convolution is frequency domain multiplication
Y_k = X_k*H_k

#Finding IFFT of Y(k)
y_n = IFFT(Y_k)


#Displaying y(n) lollipop plot
plt.stem(range(0,20),y_n[0:20])
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.show()


print("Maximum absolute value of y(n) = ",max(abs(y_n)))
#Result matches with previously computed value

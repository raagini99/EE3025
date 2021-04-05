#include <stdio.h>
#include <complex.h>
#include <math.h>

//Recursive function that computes FFT of a sequence of length which is a power of 2
void FFT_2n(double complex* x_n,double complex* X_k,int N)
{
    if(N==1)
    {
        X_k[0] = x_n[0];
        return;
    }
    int half_N = N/2;  
    
    double complex x_n_odd [half_N];
    double complex x_n_even [half_N];
    for(int i=0;i<half_N;i++) //Separating odd and even halfs of the sequence
    {
        x_n_even[i] = x_n[2*i];
        x_n_odd[i] = x_n[2*i+1];
    }
    
    double complex O_k [half_N];
    double complex E_k [half_N];
    FFT_2n(x_n_odd,O_k,half_N); //Recursively calling the function for each half
    FFT_2n(x_n_even,E_k,half_N);
    
    for(int i=0;i<half_N;i++)
    {
        //Computing the values for the sequence from the values of sub-halfs
        double complex z = cos(M_PI*i/half_N)+sin(M_PI*i/half_N)*I;
        X_k[i] = O_k[i] + z*E_k[i];
        X_k[i+half_N] = O_k[i] - z*E_k[i];
    }
}

//Function that computes FFT of a sequence
void FFT(double complex* x_n,double complex* X_k,int N)
{
    int new_N = pow(2,ceil(log(N)/log(2)));
    if(new_N==N)
        FFT_2n(x_n,X_k,N);
    else
    {
        double complex x_n_prime [new_N]; 
        for(int i=0;i<N;i++)
            x_n_prime[i] = x_n[i];
        for(int i=N;i<new_N;i++) //Padding with zeros to make length of sequence a power of 2
            x_n_prime[i] = 0;
        FFT_2n(x_n_prime,X_k,new_N);
    }
}

//Function that computes IFFT of a sequence
void IFFT(double complex* X_k,double complex* x_n,int N)
{
    double complex X_k_prime [N];
    for(int i=0;i<N;i++)
        X_k_prime[i] = conj(X_k[i]);
        
    FFT(X_k_prime,x_n,N);
    for(int i=0;i<N;i++)
        x_n[i] = conj(x_n[i])/N;
}

int main ()
{
    double complex x_n [6] = {1,2,3,4,2,1};
    
    int len = 1000;
    
    //Computing h(n)
    double complex h_n [len];
    h_n[0] = 1;
    h_n[1] = -0.5;
    for(int n=2;n<len;n++)
        h_n[n] = pow(-0.5,n) + pow(-0.5,n-2);
        
    double complex x_n_prime [len];
    for(int i=0;i<6;i++)
        x_n_prime[i] = x_n[i];
    for(int i=6;i<len;i++)
        x_n_prime[i] = 0;
    
    //Computing X(k) and H(k) via FFT
    int new_len = pow(2,ceil(log(len)/log(2)));
    double complex X_k [new_len];
    FFT(x_n_prime,X_k,len);
    
    double complex H_k [new_len];
    FFT(h_n,H_k,len);
    
    //Time domain convolution is frequency domain multiplication
    
    double complex Y_k [new_len];
    for(int i=0;i<new_len;i++)
        Y_k[i] = X_k[i]*H_k[i];
    
    //Finding IFFT of Y(k)
    double complex y_n [new_len];
    IFFT(Y_k,y_n,new_len);
    
    //Computing maximum absolute value of y(n)
    double max_val = 0;
    double temp;
    for(int i=0;i<new_len;i++)
    {
        temp = fabs(creal(y_n[i]));
        if(temp>max_val)
            max_val = temp;
    }
    printf("Maximum absolute value of y(n) = %.5f",max_val);
    //Result matches with previously computed value
    
    printf("First 20 values of y(n): \n");
    //Printing first 20 values of y(n)
    for(int i=0;i<20;i++)
    {
        printf("%.5f \n",creal(y_n[i]));
    }
    //Result matches with python program result
    
    return 0;
}

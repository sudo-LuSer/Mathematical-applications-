import math 
pi = math.pi
epsilon = 10**(-3)
inf = 10 * 32 
#Calculus
def f(x):
    return 1/(1+ x**2)
def derivative(x0):
    fx = f(x0 + epsilon) - f(x0)
    return fx/epsilon 
def integral(a,b):
    i = a 
    bigS = 0 
    while(i<=b): 
        bigS+=f(i)
        i+=epsilon 
    bigS  *= epsilon 
    return bigS 
def limite(x0) :
    return f(x0 + epsilon) 
#NumberTheory 
def FindTheInverse(prime,a):
    p = prime
    for i in range(1,p-1) :
        if((a*i)%p == 1):
            return i 
    return str(prime) + "is not a prime"
def CheckPrime(n):
    p = 2 
    while (p*p<=n):
        if(n%p==0):
            return False
        p+=1
    return True
def PrimeFactorisation(n):
    Primes=[]
    p = 2 
    while(True): 
        if(n<2):
            break
        if(n%p==0 and CheckPrime(p)):
            Primes.append(p) 
            n = n/p 
            p=2
            continue 
        p+=1
    return Primes 
def EulerTotient(n):
    EulerProduct = 1.0 
    for i in range(2,n):
        if(CheckPrime(i)):
            EulerProduct *= float(i-1)/float(i) 
    return EulerProduct*n 

def count(n):
    c=0
    n=n/2
    c+=1
    if n==1:
        return c
    else:
        count(n)
        
def fib(x):
    a,b=0,1
    for i in range(x):
        temp=a+b
        a=b
        b=temp
        print(temp)
    
T=int(input())
for j in range(T):
    N=int(input())
    A=2**count(N)
    fib(A)
    

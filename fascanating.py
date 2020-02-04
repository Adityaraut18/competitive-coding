T=int(input())
for t in range(T):
    A,c=[],0
    a=int(input())
    b=a*2
    c=a*3
    def rem(x):
        while(x>=1):
            A.append(int(x%10))
            x=x/10
    rem(a)
    rem(b)
    rem(c)
    print(A)
    for i in range(1,10):
        if A.count(i)>0:
            c=0
        else:
            print("0")
            c+=1
            break
    if (c==0):
        print("1")
 

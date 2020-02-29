T=int(input())
for i in range(T):
    N,K=input().split()
    K=int(K)
    count=0
    A=list(map(str,input().split(" ")))
    for j in A[::-1]:
        if K==0:
            break
        else:
            K-=1
            if(j=='H'):
               count+=1
               A.remove(j)
            else:
                A.remove(j)
    if (count%2==0):
        print(A.count('H'))
    else:
        print(A.count('T'))

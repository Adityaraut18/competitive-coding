X=list(map(int,input().split(",")))
A,B,sum,c=[],[],0,0
for i in range(len(X)):
    if X[i] in A:
        print("Y")
    else:
        A.append(X[i])
        x=X.count(X[i])
        B.append(x)
B.sort()
for j in range(len(X)):
    sum+=B[j]
    c+=1
    if sum>=len(X)/2:
        break
if len(X)%2==0:
    print(c)
else:
    print(c-1)
    
    
    

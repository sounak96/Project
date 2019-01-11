def modularinverse(a,m):
    a=a%m;
    for num in range(1,m):
        if((a*num)%m==1):
            return num
        #num+=1;
    return -1;
    

t=int(input())
for i in range(t):
    a,m=map(int,input().split())
    x=modularinverse(a,m)
    print(x)

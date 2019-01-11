def maxvalue(value,rem,k):
    num=1
    while(True):
        i=0;
        while(i<k):
            if(num%value[i]!=rem[i]):
                break
            i+=1;

        if(i==k):
            return num;
        num+=1;
    return num;



value=list(int(n) for n in input().split())
rem=list(int(n) for n in input().split())
#print(value)
#print(rem)
k=len(value)
x=maxvalue(value,rem,k)
print(x)


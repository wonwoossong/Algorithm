num=int(input())
for i in range(num):
    a=input()
    b=list(a)
    sum=0
    count=1
    for i in b:
        if i=='O':
            sum+=count
            count+=1
        else:
            count=1
    print(sum)
    
        
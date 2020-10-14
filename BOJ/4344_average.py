c=int(input(""))

for i in range(c):
    N=list(map(int,input("").split(" ")))
    cnt=0
    ave=sum(N[1:])/N[0]
    for j in range(N[0]):
        j+=1
        if ave<N[j]:
            cnt+=1
    print(str("%.3f" %round((cnt/N[0])*100, 3))+"%")
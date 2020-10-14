num=int(input(""))
max=0
avg=0
lst=list(map(float,input().split(" ")))#float 형 리스트 만드는법
for i in range(num):
    if max<lst[i]:
        max=lst[i]#이렇게 하면 max 랑 리스트 다 뽑아줘 
for i in range(num):
    lst[i]=lst[i]/max*100
    avg+=lst[i]
print(round(avg/num,6))
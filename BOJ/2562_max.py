b=[]
for i in range(9):
    b.append(int(input()))#이런 형식으로 하나씩 리스트 만들수 있고
print(max(b))#이 형식으로 최댓값 구할수있고
print(b.index(max(b))+1)#이 형식으로 최솟값 구할수 있다 

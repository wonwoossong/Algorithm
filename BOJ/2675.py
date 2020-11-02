a=int(input())
for i in range(a):
    R,S=input().split(" ")
    R=int(R)
    S=list(str(S))
    for x in range(len(S)):
        print(R*S[x],end='')
    print()


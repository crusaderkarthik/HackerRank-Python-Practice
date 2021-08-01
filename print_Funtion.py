##Solution1

n=int(input())
for i in range(1,n+1):
    print(i,end="")

##Soluiton2

n = int(input())
print(*range(1,n+1),sep="") ##The * is used to unpack a iterable(list, string,tuple etc) in python


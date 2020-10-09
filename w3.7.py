n=int(input())
a=set()
for i in range(n):
    a|=set(input().split())
l=len(a)
print(l)
a=set([int(x) for x in input().split()])
b=set([int(x) for x in input().split()])
c=(set(a.intersection(b)))

c=list(c)
c.sort()

print(*c)
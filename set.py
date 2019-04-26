n = int(input())
s = set(map(int, input().split()))
N=int(input())
for x in range(N):
    str=input().split()
    cmd=str[0]
    if cmd=="pop":
        s.pop()
    elif cmd=="remove":
        val=int(str[1])
        s.remove(val)
    elif cmd=="discard":
        val=int(str[1])
        s.discard(val)
print(sum(s))
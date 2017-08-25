N = int(input())
for _ in range(N):
    s = input()
    l = list(s)
    length = len(l)
    if (length % 2 == 0):
        k = int(length/2)
        a = []
        b = []
        for i in range(k):
            a.append(l[2*i])
            b.append(l[2*i+1])
    else:
        k = int((length+1)/2)
        a = []
        b = []
        a.append(l[0])
        for i in range(1,k):
            a.append(l[2*i])
            b.append(l[2*i-1])
    print("".join(a),"".join(b))

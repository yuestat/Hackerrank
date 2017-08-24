if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        method = s[0]
        detail = s[1:]
        if (method != "print"):
            cmd = method + "(" + ",".join(detail) + ")"
            eval("l."+cmd)
        else:
            print(l)

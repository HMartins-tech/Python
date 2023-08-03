N = int(input())
v = [None, None]
for i in range(N):
    v = input().split(" ")
    a = v[0]
    b = v[1]
    if len(b) > len(a):
        print("nao encaixa")
    elif a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")
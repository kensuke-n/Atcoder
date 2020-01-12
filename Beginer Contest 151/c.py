#TLE 未解決
n,m=map(int,input().split())
sum_ok,sum_miss=0,0
former_ok=[0]*n
for i in range(m):
    p, s=input().split()
    p=int(p)
    if p not in former_ok:
        if s == 'AC':
            former_ok[sum_ok] = p
            sum_ok += 1
            if sum_ok == n:
                break
        else:
            sum_miss += 1
    else:
        continue
print(sum_ok, sum_miss)

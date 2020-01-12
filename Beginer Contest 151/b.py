n, k, m = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
goal = m * n
for i in range(n-1):
    sum += a[i]

far_goal = goal - sum
if far_goal > k:
    print('-1')
elif far_goal <= 0:
    print('0')
else:
    print(far_goal)

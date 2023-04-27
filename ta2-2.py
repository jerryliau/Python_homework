a = input().split()
i = 0
list = []
while i < len(a):
  list.append(str(int(a[i])+1))
  i += 1
print(' '.join(list))
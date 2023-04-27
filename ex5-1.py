a = input() 
lists = []
for i in range(0,len(a)):
  if a[i:len(a)].count(a[i]) == 1:
    lists.append(a[i])
print(''.join(lists))
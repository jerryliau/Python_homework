a = input().split(',')
a1 = a[0].split()
a2 = a[1].split()
x = 0
for i in range(0,5):
  if(a1[i] in a2):
    x+=1
if x == 3:
  print(100)
elif x == 4:
  print(1000)
elif x == 5:
  print(10000)
else:
  print(0)
  
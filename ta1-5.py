a = input()
f = str(ord(a[0])-55)
f_t = int(f[0])+int(f[1])*9
x = 0
for i in range(1,9):
  x+=int(a[i])*(9-i)
x+=int(a[9])
if (f_t + x) % 10 == 0:
  print('合法')
else:
  print('不合法')
a = int(input())
if a % 4 != 0:
  print('false')
elif a % 100 != 0:
  print('true')
elif a % 400 != 0:
  print('false')
else:
  print('true')
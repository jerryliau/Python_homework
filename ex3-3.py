a = int(input())
if a % 4 != 0:
  print('a normal year')
elif a % 100 != 0:
  print('a leap year')
elif a % 400 != 0:
  print('a normal year')
else:
  print('a leap year')
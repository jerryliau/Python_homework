a = input()
b = list(map(int, a.split(' ')))
if b[1] >= b[0]:
  print(b[1] - b[0])
else:
  print(200 - b[0] + b[1])

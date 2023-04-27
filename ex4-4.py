a = input()
u = a.count('U')
d = a.count('D')
l = a.count('L')
r = a.count('R')
if u == d and l == r:
  print ("Y")
else:
  print("N")
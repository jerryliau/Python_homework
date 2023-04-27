import sys
a = sys.stdin.read().splitlines()
for i in range(0,len(a)):
  print(str(a[i])+str(i+1))
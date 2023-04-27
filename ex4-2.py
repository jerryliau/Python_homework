a = int(input())
i = 0
while i < a:
  str = ''
  j = 0	
  while j <= i:
    str = str + '*'
    j += 1
  print(str)
  i += 1
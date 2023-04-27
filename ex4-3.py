a = int(input())
i = 3
x = 2
if a != 2:
  while i <= a:
    j = 2
    bool = 1
    while j < i:
      if i % j == 0:
        bool = 0 
        break
      j += 1
    if bool == 1:
      x = i
    i += 1
  print(x)
else:
  print(x)  
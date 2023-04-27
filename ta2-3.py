a = int(input())
i = 0
list = [0,1]
if a == 1:
  print ("0")
elif a == 2:
  print("1")
else:
  while i < a:
    list.append(list[i]+list[i+1])
    i += 1
  print(list[a-1])
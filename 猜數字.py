import random
r = random.randint(1,100)
min = 1
max = 100
while True:
  x = int(input(f'請{min}~{max}猜一個數字:'))
  if x == r:
    print('猜中喇!!')
    break
  else:
    if x < r:
      min = x
    else:
      max = x
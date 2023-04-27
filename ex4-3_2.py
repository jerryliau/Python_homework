import math
def is_prime_number(n: int) -> bool:
  if n == 2:
    return True
  for i in range(2, math.floor(n**1/2)+1):
    if n % i == 0:
      return False
  return True

q = int(input())

for i in range(q, 1, -1):
  if is_prime_number(i) == True:
    print(i)
    break
    






  
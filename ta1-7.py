import re
a = input()
if '+' in a:
  b = a.split('+')
  print(int(int(b[0])+int(b[1])))
elif '-' in a:
  b = a.split('-')
  print(int(int(b[0])-int(b[1])))
elif '*' in a:
  b = a.split('*')
  print(int(int(b[0])*int(b[1])))
else:
  b = a.split('/')
  print(int(int(b[0])/int(b[1])))
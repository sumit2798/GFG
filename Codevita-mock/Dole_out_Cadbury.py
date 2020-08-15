dct = {}
def f(x,y):
  global counts, maxs
  counts += 1
  if x<y:
    x, y = y,x
  if x==0 or y==0:
    return 0
  if x==y:
    return 1
  else:
    if (x,y) not in dct:
      dct[(x,y)] = 1+f(x-y,y)
      if len(dct)>maxs: maxs = len(dct)
      if ((x-y,y) in dct): del dct[(x-y,y)]
    return dct[(x,y)]
res = 0
if __name__ == "__main__":
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())

  maxs = 0
  counts = 0
  for i in range(a,b+1):
    for j in range(c,d+1):
      res += f(i,j)
  print(res)
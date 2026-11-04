a = [8, 6, 7,10,0]
def median(a):
   a.sort()

   if len(a) % 2 == 0:
      x =int( len(a) // 2)
      print((a[x - 1] + a[x]) / 2)
   else:
      x = int(len(a) // 2)
      print(a[x])
median(a)





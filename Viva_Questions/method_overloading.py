class Mathematics:
   def add(self, *args):
      sum = 0
      for a in args:
         sum = sum + a
      print(sum)
 
obj = Mathematics()
obj.add(8, 9, 12)
obj.add(8, 9)
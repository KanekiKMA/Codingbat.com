def lone_sum(a, b, c):
 if(a==b and b==c):
   return 0
 elif(a==b):
   return c
 elif(c==a):
   return b
 elif(c==b):
   return a
 else:
   return a+b+c
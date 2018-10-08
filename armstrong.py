def armstrong_number(num):
 sum=0
 c=num
 while c>0:
   digit=c%10
   sum+=digit**3
   c=c//10
 return(sum)


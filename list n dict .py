n=input("enter your name-")
r=input("enter your roll no-")
gr=input("enter your gr no-")
e=input("enter your english marks-")
m=input("enter your maths marks-")
s=input("enter your sci marks-")
 
x=["name","roll no","gr no","english","maths","sci"]
y=[n,r,gr,e,m,s]
t=dict(zip(x,y))
print(t)
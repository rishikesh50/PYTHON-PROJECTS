n=int(input('enter no.of list to  write:'))
while n<1 or n>7:
    n=int(input('enter a valid number:'))
mul=int(input('enter value of m:'))
while mul<1 or mul>1000:
    mul=int(input('enter a valid number:'))
m=[]
l=[]
sum,i,k=0,0,0
for i  in range(n):
    l1,j=0,1
    print('enter list ',i+1,':')
    while int(l1)<10**9:
        if  j>7 or j<1:
            break
        l1=input()
        if l1=='':
            break
        l.append(int(l1))
        j+=1
    m1=max(l) 
    m.append(m1)
for i in range(0,n):
    sum=sum+m[i]*m[i]
ans=sum%mul
print('maximized number is:',ans)
           
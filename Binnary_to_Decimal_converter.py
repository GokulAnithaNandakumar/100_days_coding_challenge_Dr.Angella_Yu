a=input()
a=a[::-1]
b=len(a)-1
sum=0
while b>-1:
    c=int(a[b])*2**b
    sum+=c
    b-=1
print(sum)
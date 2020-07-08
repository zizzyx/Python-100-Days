
a=1
b=1

print(a)
for x in range(1,10000) :
    sum=0
    for y in range(1,x):
        if x%y==0 :
            sum+=y
    if sum == x :
        print(x)
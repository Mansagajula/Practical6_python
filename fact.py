fh=open('output6.txt','w')
a=int(input("Enter number:"))
fact=1
while(a>1):
    fact=fact*a
    a=a-1

print(fact)
fh.write(f'factorial is {fact}')
fh.close()
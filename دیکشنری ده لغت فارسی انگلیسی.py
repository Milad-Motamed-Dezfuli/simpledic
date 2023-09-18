a=input("enter a list :").split()
b={}
k=0
for i in a:
    m=""
    t=""
    for j in i:
        if "a" <=j <= "z" or "A"<= j <= "Z":
            m=m+j
        if "الف"<=j<="ی":
            t=t+j 
    b[m]=t
print(b)
c=input("enter a word :")
for x in b.keys():
    if x==c:
        k=1
        print(b[x]) 
        break
    if k==0:
        print("do you know the meaning?")
        h=input("enter yes or no:")
        if h=="yes":
            l=input("enter meaning:")
        b[c]=l
        print(b)
        break
            
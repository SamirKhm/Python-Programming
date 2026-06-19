n=int(input("Enter a password(numbers)"));
l=list(str(n))
#securiy key
temp=n
count=0
repeating=0
while temp>0:
    digit=temp%10
    for i in range(len(l)):
        if digit==int(l[i]):
            count+=1
    if count>1:
        repeating+=1
    count=0
    temp//=10
    l.remove(str(digit))
print("Number of repeating digits:", repeating)

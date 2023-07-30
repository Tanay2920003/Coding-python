num=int(input("Enter a number:"))
n=num
res=0
while num>0:
    rem=num%10
    res=rem+rem*10
    num=num//10

if res==n:
    print(n,"is a Palindrome")

else:
    print(n,"is not a Palindrome")

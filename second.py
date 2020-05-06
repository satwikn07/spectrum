num=int(input('Enter a number: '))
sum=0
for x in range(1,num+1):
    sum=sum+x

print("The sum of digits between 1 to {} is : {}".format(num,sum))

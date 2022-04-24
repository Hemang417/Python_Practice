lst = []
sum=0
num=0
a=0
total = int(input('Total numbers in List: '))

# use while loop to iterate until zero
while a < total:
    num = int(input('Enter number '))
    lst.append(num)
    sum += num
    a=a+1
print("The sum is", sum)
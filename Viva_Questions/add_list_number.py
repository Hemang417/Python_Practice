lst = []
sum=0
total = int(input('Total numbers in List: '))

for num in range(total):
    num = int(input('Enter number '))
    lst.append(num)
    sum+=num
print("Sum of elements in given list is :", sum)
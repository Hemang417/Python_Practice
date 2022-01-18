def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while(first <= last):
            mid = (first + last) // 2

            if list[mid] == target:
                return mid
            elif list[mid] < target:
                first = mid + 1
            else: 
                last = mid - 1
            
    return None

def verify(index):
    if index is not None:
        print("Target value is found at index ", index , "and position ", index + 1)
    else:
        print("Target value not found")
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 8)
verify(result)


        
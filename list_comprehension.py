def list_comprehension(n):
    odd_list = [x for x in range(1, n) if x%2 != 0]
    print(odd_list)

list_comprehension(10) # Output Expected: [1, 3, 5, 7, 9]
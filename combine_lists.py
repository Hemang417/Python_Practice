def combine_lists(list1, list2):
    final_list = []
    list1 = list1[::-1]
    final_list.append(list2 + list1)
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
    return final_list

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

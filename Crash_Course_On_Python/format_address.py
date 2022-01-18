from curses.ascii import isdigit


def format_address(address_string):
    # Declare variables
    house_number = ' '
    street_address = " "
    # Separate the address string into parts
    x = address_string.split(" ")

    # Traverse through the address parts
    for y in x:
        if y.isdigit():    #Checking if the splitted string contains a number, 
                            #if yes then house_number would save the value
            house_number += y
        else:
            street_address += y
            street_address += ' '
            # as the other things that are present in the address_string is a string so we'll save that 
            # value in street_address

            # Return the formatted string as asked in the question
    return "house number{} on street named{}".format(house_number, street_address)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

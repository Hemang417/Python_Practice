#The highlight_word function changes the given word in a sentence to its upper-case version. 
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
# Can you write this function in just one line?

def highlight_word(sentence, word):
	return " ".join([x.upper() if x.lower() == word.lower() else x for x in sentence.split()])

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

#Output:
# Have a NICE day
# Shhh, don't be so loud!
# Automating with Python is FUN

import re
search_word = re.search(r"[a-z]way", "The end of the highway")
print(search_word)

"""OUTPUT"""
# <re.Match object; span=(18, 22), match='hway'>

search_word_with_space = re.search(r"[a-z]way", "This is the way to hell")
print(search_word_with_space)

"""OUTPUT"""
# None
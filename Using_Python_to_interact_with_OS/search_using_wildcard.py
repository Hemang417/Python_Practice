import re
search_word = re.search(r"[a-z]way", "The end of the highway")
print(search_word)

"""OUTPUT"""
# <re.Match object; span=(18, 22), match='hway'>
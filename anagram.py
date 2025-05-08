# s = "rat"
# t = "car"
# s = "anagram"
# t = "nagaram"


# def anag(s,t):
#     return sorted(s)==sorted(t)
# s = "anagram"
# t = "nagaram"
# print(anag(s,t))

from collections import Counter

def anag(s, t):
    return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"

print(anag(s,t))

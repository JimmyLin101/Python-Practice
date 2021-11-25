"""
Excerpt from docs.python.org/3/library
"""
import re

print("[ ]\n  Used to indicate a set of characters")

orig_str = "0abcxyAZ-01239_"
print("Example String: {}".format(orig_str))

re_str = "[a0]"
match_str = re.findall(re_str, orig_str)
print("match a or 0, RE {}\n  {}".format(re_str, match_str))

re_str = "[A-z]"
match_str = re.findall(re_str, orig_str)
print("match A to z, RE {}\n  {}".format(re_str, match_str))

re_str = "[-Z]"
match_str = re.findall(re_str, orig_str)
print("match - and z, RE {}\n  {}".format(re_str, match_str))

re_str = "[\w]" # this is equivalent to [a-zA-Z0-9]
match_str = re.findall(re_str, orig_str)
print("match String, RE {}\n  {}".format(re_str, match_str))

re_str = "[^a-z]"
match_str = re.findall(re_str, orig_str)
print("match any character except a-z , RE {}\n  {}".format(re_str, match_str))

re_str = "abc|012"
match_str = re.findall(re_str, orig_str)
print("match abc or 012, RE {}\n  {}".format(re_str, match_str))

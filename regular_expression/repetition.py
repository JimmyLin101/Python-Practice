"""
Excerpt from docs.python.org/3/library
"""
import re

orig_str = "<a> b <c>"
print("Example String: {}".format(orig_str))
re_str = "<.*>"
match_str = re.findall(re_str, orig_str)
print("match in greedy, RE {}\n  {}".format(re_str, match_str))

"""
Adding ? after the qualifier makes it perform the match in non-greedy.
"""
print("?\n  Causes the resulting RE to match 0 or 1 repetitions.")
re_str = "<.*?>"
match_str = re.findall(re_str, orig_str)
print("match in non-greedy, RE {}\n  {}".format(re_str, match_str))

orig_str = "abbbbbc"
print("Example String: {}".format(orig_str))
re_str = "ab{2,3}c"
m_to_n = re.findall(re_str, orig_str)
print("m to n, RE {}\n  {}".format(re_str, m_to_n))

re_str = "ab{2,5}c"
m_to_n = re.findall(re_str, orig_str)
print("m to n, RE {}\n  {}".format(re_str, m_to_n))

re_str = "ab{2,}c"
m_to_n = re.findall(re_str, orig_str)
print("m to n, RE {}\n  {}".format(re_str, m_to_n))

print("+\n  Causes the resulting RE to match 1 or more repetitions.")
re_str = "ab+c"
match_str = re.findall(re_str, orig_str)
print("match in non-greedy, RE {}\n  {}".format(re_str, match_str))

re_str = "ab+cd+"
match_str = re.findall(re_str, orig_str)
print("match in non-greedy, RE {}\n  {}".format(re_str, match_str))

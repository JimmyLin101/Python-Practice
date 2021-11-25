"""
Excerpt from docs.python.org/3/library
"""
import re

print("[ ]\n  Used to indicate a set of characters")

orig_str = "0abcxyAZ-01239_"
print("Example String: {}".format(orig_str))

re_str = "[a0](...)"
match_str = re.findall(re_str, orig_str)
print("match a.. or 0.., RE {}\n  {}".format(re_str, match_str))

re_str = "[a0](?:...)" # A non-capturing version parentheses.
match_str = re.findall(re_str, orig_str)
print("match a.. or 0.., RE {}\n  {}".format(re_str, match_str))

re_str = "abc(?=xy)"
match_str = re.findall(re_str, orig_str)
print("(?=...) match abc if xy matches next RE {}\n  {}".format(re_str, match_str))

re_str = "abc(?=xyz)"
match_str = re.findall(re_str, orig_str)
print("lookahead assettion, match abc if xyz matches next RE {}\n  {}".format(re_str, match_str))

re_str = "abc(?!xy)"
match_str = re.findall(re_str, orig_str)
print("negative lookahead assertion, match abc if xy doesn't match next RE {}\n  {}".format(
	re_str, match_str))

re_str = "abc(?!xyz)"
match_str = re.findall(re_str, orig_str)
print("match abc if xyz doesn't match next RE {}\n  {}".format(re_str, match_str))

re_str = "(?<=0).."
match_str = re.findall(re_str, orig_str)
print("positive lookbehind assertion, match 0.. {}\n  {}".format(re_str, match_str))

re_str = "(?<!0ab)..."
match_str = re.findall(re_str, orig_str)
print("negative lookbehind assertion, match 0.. {}\n  {}".format(re_str, match_str))


#(?(id/name)yes-pattern|no-pattern)

import re

fm="({a}+{b})*{c}"
pattern = r"(\{.*?\})"
guid=re.findall(pattern,fm)

for x in guid:
    rs = x.replace('[','').replace(']','')
    print(rs)



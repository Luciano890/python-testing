"""..."""
import re

TOTEST = "011+22=33"
print(re.search(r'([^\d]|\b)0\d+', TOTEST))
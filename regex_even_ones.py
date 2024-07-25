# even ones
import re

regex = re.compile(r'^(0*(10*10*)*)*$')

input_str = '1010'
print(f"Does the string '{input_str}' match the regular expression? {bool(regex.match(input_str))}")

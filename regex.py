import re
input_string = input()
vow_pattern = r'\b[aeiou]\w+'
cons_pattern = r'\b[^aeiou0-9 ]\w+'
vow_result = re.findall(vow_pattern, input_string)
cons_result = re.findall(cons_pattern, input_string)
print(vow_result)
print(cons_result)

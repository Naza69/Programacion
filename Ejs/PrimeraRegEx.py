import re
string="^[a-zA-Z]{1,6}$"
comparator=re.compile(string)
print(comparator.match("Nazareno"))
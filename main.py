import re

file = open("sample.txt", encoding="utf-8")

informacion = file.read()
file.close()
print(informacion)

print(re.search(r"was", informacion))

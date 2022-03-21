import json
import re
#кодировка?
periodic_table = json.load(open('periodic_table.json', encoding='utf-8'))
#periodic_table = json.load(open('periodic_table.json'))

i = 0 #counter
with open("output_file_3.txt", "w") as new_file:
    with open("import_file_3.txt", "r") as file:
        data = file.read()
        pattern ='(?:[A-Z]{1}[a-z]|[A-Z])'
        #{1}
        chemical= re.findall(pattern, data)
        print(chemical)